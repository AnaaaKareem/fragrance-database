from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
import pymysql

def home(request):
    return render(request, 'store/homepage.html')

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Example: Save to external DB using PyMySQL
            connection = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='Pass0-lap123',
                db='fragrance_schema',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )

            try:
                with connection.cursor() as cursor:
                    sql = """
                            INSERT INTO customer (
                                first_name, middle_name, last_name, DOB, email_address, password, gender
                            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """
                    cursor.execute(sql, (
                        data['first_name'], data.get('middle_name'), data['last_name'], data.get('DOB'),
                        data['email_address'], make_password(data['password1']), data.get('gender')
                    ))
                    # Get customer_id
                    customer_id = cursor.lastrowid
                    # Get phone_numbers table
                    phone_number = data.get('phone_numbers')
                    if phone_number:
                        phone_sql = "INSERT INTO phone_numbers (customer_id, phone_number) VALUES (%s, %s)"
                        cursor.execute(phone_sql, (customer_id, phone_number))

                        # Insert address
                        house = data.get('house')
                        street_name = data.get('street_name')
                        town_city = data.get('town_city')
                        county = data.get('county')
                        postcode = data.get('postcode')
                        country = data.get('country')

                        if house and street_name and town_city and county and postcode and country:
                            address_sql = """
                                INSERT INTO addresses (
                                    customer_id, house, street_name, town_city, county, postcode, country
                                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                            """
                            cursor.execute(address_sql, (
                                customer_id, house, street_name, town_city, county, postcode, country
                            ))
                    connection.commit()
                    messages.success(request, "User registered successfully!")
                    return redirect(home)
            except pymysql.MySQLError as e:
                connection.rollback()
                messages.error(request, f"Database error: {e}")
                return redirect('signup')
            finally:
                connection.close()
    else:
        form = UserRegistrationForm()

    return render(request, 'store/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        try:
            customer = Customer.objects.get(email_address=email)
            if check_password(password, customer.password):
                # Manually start session
                request.session['customer_id'] = customer.customer_id
                request.session['first_name'] = customer.first_name
                request.session['middle_name'] = customer.middle_name
                request.session['last_name'] = customer.last_name
                request.session['email_address'] = customer.email_address
                if customer.DOB:
                    request.session['DOB'] = customer.DOB.isoformat()
                request.session['gender'] = customer.gender

                # Get the first address of the customer (if any)
                address = customer.addresses.first()
                if address:
                    request.session['house'] = address.house
                    request.session['street_name'] = address.street_name
                    request.session['town_city'] = address.town_city
                    request.session['county'] = address.county
                    request.session['postcode'] = address.postcode
                    request.session['country'] = address.country

                # Get the customer's phone numbers
                phone_numbers = customer.phonenumbers.all()
                request.session['phone_numbers'] = [phone.phone_number for phone in
                                                    phone_numbers] if phone_numbers.exists() else []

                # Redirect to homepage after successful login
                return redirect('homepage')
            else:
                messages.error(request, 'Invalid email or password')
        except Customer.DoesNotExist:
            messages.error(request, 'Invalid email or password')

    return render(request, 'store/signin.html')


def signout(request):
    request.session.flush()
    return redirect('signinAccount')

def account(request):

    first_name = request.session.get('first_name')
    middle_name = request.session.get('middle_name', '')
    last_name = request.session.get('last_name')
    email_address = request.session.get('email_address')
    DOB = request.session.get('DOB')
    gender = request.session.get('gender')
    house = request.session.get('house')
    street_name = request.session.get('street_name')
    town_city = request.session.get('town_city')
    county = request.session.get('county')
    postcode = request.session.get('postcode')
    country = request.session.get('country')
    phone_numbers = request.session.get('phone_number', [])
    context = {
        'first_name': first_name,
        'middle_name': middle_name,
        'last_name': last_name,
        'email_address': email_address,
        'DOB': DOB,
        'gender': gender,
        'house': house,
        'street_name': street_name,
        'town_city': town_city,
        'county': county,
        'postcode': postcode,
        'country': country,
        'phone_numbers': phone_numbers,
    }

    return render(request, 'store/accountInfo.html', context)

def store(request):
    products = Products.objects.all()
    images = ProductImages.objects.all()

    if request.method == "POST" and "add_basket" in request.POST:
        product_id = request.POST.get("product_id")
        quantity = int(request.POST.get("quantity", 1))
        customer_id = request.session['customer_id']

        basket_item, created = Basket.objects.get_or_create(
            customer_id=customer_id, product_id=product_id,
            defaults={'quantity': quantity}
        )

        if not created:  # If item already exists, update quantity
            basket_item.quantity += quantity
            basket_item.save()

        return redirect('store')

    return render(request, 'store/storepage.html', {'products': products, 'images': images})

def basket(request):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('signin')

    items = Basket.objects.filter(customer_id=customer_id)
    subtotal = sum(item.product.price * item.quantity for item in items)
    discount_rate = 0  # Define your discount logic
    discount = subtotal * (discount_rate / 100)
    total = subtotal - discount

    context = {
        'items': items,
        'subtotal': subtotal,
        'discount_rate': discount_rate,
        'discount': discount,
        'total': total
    }

    return render(request, 'store/basket.html', context)


def delete_from_basket(request, product_id):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('signin')

    basket_item = get_object_or_404(Basket, customer_id=customer_id, product_id=product_id)
    basket_item.delete()
    return redirect('basket')


def update_basket(request, product_id):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('signin')

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        basket_item = Basket.objects.filter(customer_id=customer_id, product_id=product_id).first()
        if basket_item:
            if quantity > 0:
                basket_item.quantity = quantity
                basket_item.save()
            else:
                basket_item.delete()
    return redirect('basket')