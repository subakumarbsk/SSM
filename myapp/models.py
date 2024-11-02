from django.db import models

# Create your models here.
# Form classes
#Dealer Add
class Dealer_Details(models.Model):
    dealer = models.CharField(max_length=40)
    gst_no = models.CharField(max_length=20)
    dd = models.DateField()
    d_category = models.CharField(max_length=30)
    d_address = models.CharField(max_length=300)
    d_mobile_no = models.IntegerField()
    contact_name = models.CharField(max_length=20)
# Medicine Add Form
class Medi(models.Model):
    medicine_name = models.CharField(max_length=30)
    med_combination = models.CharField(max_length=100, null=True, blank=True)
    med_dealer = models.CharField(max_length=50)
    med_category = models.CharField(max_length=20)
    med_mrp = models.IntegerField()
    med_up  =   models.IntegerField()
    med_u_gst = models.IntegerField()
    med_gst = models.IntegerField()
    med_qty = models.IntegerField()
    med_unit = models.CharField(max_length=6)
#Medicine Bill
class Medicine_Bill(models.Model):
    med_dealer = models.CharField(max_length=50)
    med_invoice = models.CharField(max_length=50)
    med_invoice_d = models.DateField(null=True, blank=True)
    med_amt = models.IntegerField()
    med_payment = models.CharField(max_length=20)
    med_amt1  =   models.IntegerField(null=True, blank=True)
    med_bill_no = models.CharField(max_length=10, null=True, blank=True)
    med_b1_d = models.DateField(null=True, blank=True)
    med_amt2 = models.IntegerField(null=True, blank=True)
    med_bill_no2 = models.CharField(max_length=10, null=True, blank=True)
    med_b2_d = models.DateField(null=True, blank=True)
#Veg_dhal Add Form
class Grains(models.Model):
    veg_name = models.CharField(max_length=30)
    veg_dealer = models.CharField(max_length=100)
    veg_mar = models.IntegerField()
    veg_category = models.CharField(max_length=20)
    veg_mrp = models.IntegerField()
    veg_up  =   models.IntegerField()
    veg_mar_Price  =   models.IntegerField()
    veg_gst = models.IntegerField()
    with_gst = models.IntegerField()
    veg_qty = models.IntegerField()
    veg_unit = models.CharField(max_length=6)
# Veg _ Dhal Bill
class veg_dhal_bill(models.Model):
    veg_dealer = models.CharField(max_length=50)
    veg_invoice = models.CharField(max_length=50)
    veg_invoice_d = models.DateField()
    veg_amt = models.IntegerField()
    veg_payment = models.CharField(max_length=20)
    veg_amt1  =   models.IntegerField()
    veg_bill_no = models.CharField(max_length=10)
    veg_b1_d = models.DateField()
# Product Add
class AllProduct(models.Model):
    pro_name = models.CharField(max_length=30)
    pro_dealer = models.CharField(max_length=100)
    pro_type = models.CharField(max_length=30)
    pro_cat = models.CharField(max_length=30)
    pro_mrp = models.IntegerField()
    pro_up  =   models.IntegerField()
    pro_gst = models.IntegerField()
    pro_gst_price = models.IntegerField()
    pro_qty = models.IntegerField()
    pro_unit = models.CharField(max_length=6)
# Product Bill
class Product_Bill(models.Model):
    pro_dealer = models.CharField(max_length=50)
    pro_invoice = models.CharField(max_length=50)
    pro_invoice_d = models.DateField()
    pro_amt = models.IntegerField()
    pro_payment = models.CharField(max_length=20)
    pro_amt1  =   models.IntegerField()
    pro_bill_no = models.CharField(max_length=10)
    pro_b1_d = models.DateField()
# EC Bill
class EC_Bill(models.Model):
    sim_name = models.CharField(max_length=50)
    ec_paid = models.IntegerField()
    ec_b1_d = models.DateField()
# Medicine ORDER
class Medicine_Order(models.Model):
    name = models.CharField(max_length=30)
    dealer = models.CharField(max_length=100)
    cat = models.CharField(max_length=50)
    mrp = models.IntegerField()
    up = models.IntegerField()
    gst_price = models.IntegerField()
    qty = models.IntegerField()
    unit = models.CharField(max_length=20)
class Grain_Order(models.Model):
    name = models.CharField(max_length=30)
    dealer = models.CharField(max_length=100)
    cat = models.CharField(max_length=50)
    mrp = models.IntegerField()
    up = models.IntegerField()
    gst_price = models.IntegerField()
    qty = models.IntegerField()
    unit = models.CharField(max_length=20)
class Grocery_Order(models.Model):
    name = models.CharField(max_length=30)
    dealer = models.CharField(max_length=100)
    cat = models.CharField(max_length=50)
    mrp = models.IntegerField()
    up = models.IntegerField()
    gst_price = models.IntegerField()
    qty = models.IntegerField()
    unit = models.CharField(max_length=20)
class Stationary_Order(models.Model):
    name = models.CharField(max_length=30)
    dealer = models.CharField(max_length=100)
    cat = models.CharField(max_length=50)
    mrp = models.IntegerField()
    up = models.IntegerField()
    gst_price = models.IntegerField()
    qty = models.IntegerField()
    unit = models.CharField(max_length=20)