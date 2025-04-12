# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addresses(models.Model):
    objects = models.Manager()
    address_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', models.DO_NOTHING, related_name='addresses')
    house = models.CharField(max_length=100)
    street_name = models.CharField(max_length=100)
    town_city = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    postcode = models.CharField(max_length=20)
    country = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'addresses'


class Basket(models.Model):
    objects = models.Manager()
    pk = models.CompositePrimaryKey('customer_id', 'product_id')
    customer = models.ForeignKey('Customer', models.DO_NOTHING, related_name='baskets')
    product = models.ForeignKey('Products', models.DO_NOTHING, related_name='basket_items')
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'basket'
        unique_together = (('customer', 'product'),)


class Customer(models.Model):
    objects = models.Manager()
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    DOB = models.DateField(db_column='DOB')  # Field name made lowercase.
    gender = models.CharField(max_length=10)
    email_address = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'customer'


class DiscountRate(models.Model):
    member_type = models.CharField(primary_key=True, max_length=50)
    discount_rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'discount_rate'


class Favourite(models.Model):
    objects = models.Manager()
    pk = models.CompositePrimaryKey('customer_id', 'product_id')
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'favourite'
        unique_together = (('customer', 'product'),)


class GiftCards(models.Model):
    objects = models.Manager()
    gift_card_num = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    amount = models.FloatField()
    issue_date = models.DateField()
    exp_date = models.DateField()
    redeemed_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gift_cards'


class HomeFragrances(models.Model):
    objects = models.Manager()
    product = models.OneToOneField('Products', models.DO_NOTHING, primary_key=True, related_name='home_fragrance')
    product_type = models.CharField(max_length=50)
    bundle = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'home_fragrances'


class Instalments(models.Model):
    objects = models.Manager()
    pk = models.CompositePrimaryKey('order_id', 'instalment_number')
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    instalment_number = models.IntegerField()
    instalment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_due = models.DateField(blank=True, null=True)
    payment_status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'instalments'
        unique_together = (('order', 'instalment_number'),)


class Inventory(models.Model):
    objects = models.Manager()
    inventory_id = models.AutoField(primary_key=True)
    store = models.ForeignKey('Store', models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    quantity = models.IntegerField()
    restocking_threshold = models.IntegerField()
    last_restocking_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'inventory'


class Membership(models.Model):
    objects = models.Manager()
    member_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    membership_type = models.ForeignKey(DiscountRate, models.DO_NOTHING, db_column='membership_type')
    end_ren_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'membership'


class OrderItems(models.Model):
    objects = models.Manager()
    pk = models.CompositePrimaryKey('order_id', 'ordered_product')
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    ordered_product = models.ForeignKey('Products', models.DO_NOTHING, db_column='ordered_product')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'order_items'
        unique_together = (('order', 'ordered_product'),)


class OrderRef(models.Model):
    objects = models.Manager()
    order_id = models.ForeignKey('Orders', models.DO_NOTHING)
    product_selected = models.ForeignKey('Products', models.DO_NOTHING, db_column='ordered_product')

    class Meta:
        managed = False
        db_table = 'order_ref'
        unique_together = (('order_id', 'product_selected'),)


class Orders(models.Model):
    objects = models.Manager()
    order_id = models.AutoField(primary_key=True)
    gift_card_num = models.ForeignKey(GiftCards, models.DO_NOTHING, db_column='gift_card_num', blank=True, null=True)
    order_date = models.DateTimeField()
    order_status = models.CharField(max_length=50)
    order_type = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    installment = models.IntegerField()
    total_payment = models.FloatField()

    class Meta:
        managed = False
        db_table = 'orders'


class PersonalFragrances(models.Model):
    objects = models.Manager()
    pk = models.CompositePrimaryKey('product_id', 'size')
    product = models.ForeignKey('Products', models.DO_NOTHING, related_name='personal_fragrance')
    size = models.CharField(max_length=20)
    fragrance_family = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    strength = models.CharField(max_length=20)
    engraving = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'personal_fragrances'
        unique_together = (('product', 'size'),)


class PhoneNumbers(models.Model):
    objects = models.Manager()
    customer = models.ForeignKey(Customer, models.DO_NOTHING, related_name='phonenumbers')
    phone_number = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'phone_numbers'


class Places(models.Model):
    objects = models.Manager()
    pk = models.CompositePrimaryKey('customer_id', 'product_id', 'order_id')
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    order = models.ForeignKey(Orders, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'places'
        unique_together = (('customer', 'product', 'order'),)


class ProductImages(models.Model):
    objects = models.Manager()
    image_id = models.AutoField(primary_key=True)
    product = models.ForeignKey('Products', models.DO_NOTHING, related_name='product_images')
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'product_images'


class ProductInventory(models.Model):
    objects = models.Manager()
    pk = models.CompositePrimaryKey('inventory_id', 'product_id')
    inventory = models.ForeignKey(Inventory, models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_inventory'
        unique_together = (('inventory', 'product'),)


class Products(models.Model):
    objects = models.Manager()
    product_id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    gift = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'products'


class Store(models.Model):
    objects = models.Manager()
    store_id = models.AutoField(primary_key=True)
    branch_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store'
