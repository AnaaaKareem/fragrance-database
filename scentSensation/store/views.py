from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
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
                            customer_id = cursor.lastrowid
                            member = data.get('membership')
                        if member:
                            member_sql = """
                                INSERT INTO membership (
                                    customer_id, membership_type, end_ren_date
                                ) VALUES (%s, %s, %s)
                            """
                            cursor.execute(member_sql, (
                                customer_id, member, timezone.now() + timedelta(days=30)
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
    if request.method == 'GET':
        customer_id = request.session.get('customer_id')
        try:
            connection = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='Pass0-lap123',
                db='fragrance_schema',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM customer WHERE customer_id = %s", (customer_id,))
                customer = cursor.fetchone()
                if customer:
                    request.session['first_name'] = customer['first_name']
                    request.session['middle_name'] = customer['middle_name']
                    request.session['last_name'] = customer['last_name']
                    request.session['email_address'] = customer['email_address']
                    request.session['DOB'] = str(customer['DOB'])
                    request.session['gender'] = customer['gender']

                cursor.execute("SELECT * FROM addresses WHERE customer_id = %s", (customer_id,))
                address = cursor.fetchone()
                if address:
                    request.session['house'] = address['house']
                    request.session['street_name'] = address['street_name']
                    request.session['town_city'] = address['town_city']
                    request.session['county'] = address['county']
                    request.session['postcode'] = address['postcode']
                    request.session['country'] = address['country']

                cursor.execute("SELECT membership_type FROM membership WHERE customer_id = %s", (customer_id,))
                membership = cursor.fetchone()
                if membership:
                    request.session['membership'] = membership['membership_type']


        finally:
            connection.close()

    if request.method == 'POST':
        customer_id = request.session.get('customer_id')
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            try:
                connection = pymysql.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password='Pass0-lap123',
                    db='fragrance_schema',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )
                with connection.cursor() as cursor:
                    # --- Customer fields ---
                    if data.get('first_name'):
                        cursor.execute("UPDATE customer SET first_name = %s WHERE customer_id = %s",
                                       (data['first_name'], customer_id))

                    if data.get('middle_name'):
                        cursor.execute("UPDATE customer SET middle_name = %s WHERE customer_id = %s",
                                       (data['middle_name'], customer_id))

                    if data.get('last_name'):
                        cursor.execute("UPDATE customer SET last_name = %s WHERE customer_id = %s",
                                       (data['last_name'], customer_id))

                    if data.get('DOB'):
                        cursor.execute("UPDATE customer SET DOB = %s WHERE customer_id = %s",
                                       (data['DOB'], customer_id))

                    if data.get('email_address'):
                        cursor.execute("UPDATE customer SET email_address = %s WHERE customer_id = %s",
                                       (data['email_address'], customer_id))

                    if data.get('password'):
                        cursor.execute("UPDATE customer SET password = %s WHERE customer_id = %s",
                                       (make_password(data['password']), customer_id))

                    if data.get('gender'):
                        cursor.execute("UPDATE customer SET gender = %s WHERE customer_id = %s",
                                       (data['gender'], customer_id))

                    # --- Phone number ---
                    if data.get('phone_numbers'):
                        cursor.execute("""
                            INSERT INTO phone_numbers (customer_id, phone_number)
                            VALUES (%s, %s)
                            ON DUPLICATE KEY UPDATE phone_number = VALUES(phone_number)
                        """, (customer_id, data['phone_numbers']))

                    # --- Address fields ---
                    if data.get('house'):
                        cursor.execute("UPDATE addresses SET house = %s WHERE customer_id = %s",
                                       (data['house'], customer_id))

                    if data.get('street_name'):
                        cursor.execute("UPDATE addresses SET street_name = %s WHERE customer_id = %s",
                                       (data['street_name'], customer_id))

                    if data.get('town_city'):
                        cursor.execute("UPDATE addresses SET town_city = %s WHERE customer_id = %s",
                                       (data['town_city'], customer_id))

                    if data.get('county'):
                        cursor.execute("UPDATE addresses SET county = %s WHERE customer_id = %s",
                                       (data['county'], customer_id))

                    if data.get('postcode'):
                        cursor.execute("UPDATE addresses SET postcode = %s WHERE customer_id = %s",
                                       (data['postcode'], customer_id))

                    if data.get('country'):
                        cursor.execute("UPDATE addresses SET country = %s WHERE customer_id = %s",
                                       (data['country'], customer_id))

                    # --- Membership ---
                    if data.get('membership'):
                        cursor.execute("""
                            UPDATE membership 
                            SET membership_type = %s, end_ren_date = %s
                            WHERE customer_id = %s
                        """, (data['membership'], timezone.now() + timedelta(days=30), customer_id))

                    connection.commit()
                    messages.success(request, "Your account information has been updated.")
                    return redirect('account')

            except pymysql.MySQLError as e:
                connection.rollback()
                messages.error(request, f"Database error: {e}")
            finally:
                connection.close()

    context = {
        'first_name': request.session.get('first_name'),
        'middle_name': request.session.get('middle_name', ''),
        'last_name': request.session.get('last_name'),
        'email_address': request.session.get('email_address'),
        'DOB': request.session.get('DOB'),
        'gender': request.session.get('gender'),
        'house': request.session.get('house'),
        'street_name': request.session.get('street_name'),
        'town_city': request.session.get('town_city'),
        'county': request.session.get('county'),
        'postcode': request.session.get('postcode'),
        'country': request.session.get('country'),
        'membership': request.session.get('membership')
    }

    return render(request, 'store/accountInfo.html', context)


def store(request):
    all_products = Products.objects.all()
    images = ProductImages.objects.all()

    paginator = Paginator(all_products, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    if request.method == "POST" and "add_basket" in request.POST:
        product_id = request.POST.get("product_id")
        quantity = int(request.POST.get("quantity", 1))
        customer_id = request.session['customer_id']

        basket_item, created = Basket.objects.get_or_create(
            customer_id=customer_id,
            product_id=product_id,
            defaults={'quantity': quantity}
        )

        if not created:
            basket_item.quantity += quantity
            basket_item.save()

        return redirect('store')

    context = {
        'products': page_obj,            # This contains the paginated products
        'images': images,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages()
    }
    return render(request, 'store/storepage.html', context)

def basket(request):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('signin')

    items = Basket.objects.select_related('product').filter(customer_id=customer_id)

    item_list = []
    for item in items:
        product = item.product

    basket_items = Basket.objects.filter(customer_id=customer_id)

    items = []
    subtotal = 0

    for item in basket_items:
        product = Products.objects.filter(product_id=item.product_id).first()
        image = ProductImages.objects.filter(product_id=item.product_id).first()
        personal = PersonalFragrances.objects.filter(product_id=item.product_id).first()
        home = HomeFragrances.objects.filter(product_id=item.product_id).first()

        total_price = product.price * item.quantity
        subtotal += total_price

        items.append({
            'product': product,
            'quantity': item.quantity,
            'image': image,
            'personal': personal,
            'home': home,
        })

    # Get membership discount
    discount_rate = 0
    membership = Membership.objects.filter(customer_id=customer_id).first()
    if membership:
        discount_obj = DiscountRate.objects.filter(member_type=membership.membership_type.member_type).first()
        discount_rate = discount_obj.discount_rate

    discount = subtotal * (discount_obj.discount_rate / 100)
    total = subtotal - discount

    # Use context to send data
    context = {
        'items': items,
        'subtotal': round(subtotal, 2),
        'discount': round(discount, 2),
        'total': round(total, 2),
        'discount_rate': discount_rate
    }

    return render(request, 'store/basket.html', context)


def delete_from_basket(request, product_id):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('signin')

    basket_item = get_object_or_404(Basket, customer_id=customer_id, product_id=product_id)
    basket_item.delete()
    return redirect('basket')


def checkout(request):
    customer_id = request.session.get('customer_id')
    basket_items = Basket.objects.filter(customer=customer_id)

    if not basket_items.exists():
        messages.error(request, "Your basket is empty.")
        return redirect('basket')

    # Step 1: Delete the basket items
    basket_items.delete()

    messages.success(request, "Your basket has been cleared and order removed if in progress.")
    return redirect('basket')