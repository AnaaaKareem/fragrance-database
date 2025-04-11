from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.hashers import make_password
from .forms import UserRegistrationForm
import pymysql

def home(request):
    return render(request, 'store/homepage.html')

def signinout(request):
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
            finally:
                connection.close()
    else:
        form = UserRegistrationForm()

    return render(request, 'store/account.html', {'form': form})

def account(request):
    return render(request, 'store/accountInfo.html')

def store(request):
    products = Products.objects.all()
    images = ProductImages.objects.all()
    return render(request, 'store/storepage.html', {'products': products, 'images': images})

def basket(request):
    basket = Basket.objects.all()
    return render(request, 'store/basket.html',{'basket': basket})