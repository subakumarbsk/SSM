from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Dealer_Details,Medi,Grains,AllProduct,Medicine_Bill,veg_dhal_bill,Product_Bill,EC_Bill,Medicine_Order,Grain_Order,Grocery_Order,Stationary_Order

# Create your views here.
# Titles and Ksy Words
SHOP_NAME = 'Saravana Medicals',
# category datas

#HOME PAGE
def index(request):
    return render(request, "dynamic/index.html")

# FORM PAGES
#Dealer Add
def dealer_add(request):
    if request.method == 'POST':
        dealer = request.POST['dealer']
        gst_no = request.POST['gst_no'] 
        dd =  request.POST['dd']
        d_category = request.POST['d_category']
        d_address = request.POST['d_address']
        d_mobile_no = request.POST['d_mobile_no'] 
        contact_name = request.POST['contact_name']

        d_info = Dealer_Details()
        d_info.dealer = dealer
        d_info.gst_no = gst_no
        d_info.d_address = d_address
        d_info.dd = dd
        d_info.d_category = d_category
        d_info.d_mobile_no = d_mobile_no
        d_info.contact_name = contact_name
        d_info.save()

        all_dealer = Dealer_Details.objects.all()
    return render(request, "form/dealer.html")
#Medicine_add
def med_add_form(request):
    if request.method == 'POST':
        medicine_name = request.POST['medicine_name']
        med_combination = request.POST['combination'] 
        med_dealer =  request.POST['med_dealer']
        med_category = request.POST['med_category']
        med_mrp = request.POST['med_mrp'] 
        med_up = request.POST['med_up']
        med_gst = request.POST['med_gst']
        med_qty = request.POST['med_qty']
        med_unit = request.POST['med_unit']

        med_data = Medi()
        med_data.medicine_name = medicine_name
        med_data.med_combination = med_combination
        med_data.med_dealer = med_dealer
        med_data.med_category = med_category
        med_data.med_mrp = med_mrp
        med_data.med_up = med_up
        med_data.med_u_gst = (int (med_up)*int(med_gst)/100)+int(med_up)
        med_data.med_gst = med_gst
        med_data.med_qty = med_qty
        med_data.med_unit = med_unit
        med_data.save()

        medi_data = Medi.objects.all()
    all_dealer = Dealer_Details.objects.all()
    return render(request,"form/med_add.html",{'dealers':all_dealer})
#Medicine_BILL
def med_bill(request):
    if request.method == 'POST':
        med_dealer =  request.POST['med_dealer']
        med_invoice = request.POST['med_invoice']
        med_invoice_d = request.POST['med_invoice_d'] 
        med_amt = request.POST['med_amt']
        med_payment = request.POST['med_payment'] 
        med_amt1 = request.POST['med_amt1']
        med_bill_no = request.POST['med_bill_no']
        med_b1_d = request.POST['med_b1_d']
        med_amt2 = request.POST['med_amt2']
        med_bill_no2 = request.POST['med_bill_no2']
        med_b2_d = request.POST['med_b2_d']

        med_bill_data = Medicine_Bill()
        med_bill_data.med_dealer = med_dealer
        med_bill_data.med_invoice = med_invoice
        med_bill_data.med_invoice_d = med_invoice_d
        med_bill_data.med_amt = med_amt
        med_bill_data.med_payment = med_payment
        med_bill_data.med_amt1 = med_amt1
        med_bill_data.med_bill_no = med_bill_no
        med_bill_data.med_b1_d = med_b1_d
        med_bill_data.med_amt2 = med_amt2
        med_bill_data.med_bill_no2 = med_bill_no2
        med_bill_data.med_b2_d = med_b2_d
        med_bill_data.save()

        medi_bill_data = Medicine_Bill.objects.all()
    all_dealer = Dealer_Details.objects.all()
    return render(request,"form/med_bill.html",{'dealers':all_dealer})
#Dhal_add
def veg_dhal_add_form(request):
    if request.method == 'POST':
        veg_name = request.POST['veg_name']
        veg_mar = request.POST['veg_margin'] 
        veg_dealer =  request.POST['vd_name']
        veg_category = request.POST['veg_cat']
        veg_mrp = request.POST['veg_mrp'] 
        veg_up = request.POST['veg_up']
        veg_gst = request.POST['veg_gst']
        veg_qty = request.POST['veg_qty']
        veg_unit = request.POST['veg_unit']

        veg_data = Grains()
        veg_data.veg_name = veg_name
        veg_data.veg_mar = veg_mar
        veg_data.veg_dealer = veg_dealer
        veg_data.veg_category = veg_category
        veg_data.veg_mrp = veg_mrp
        veg_data.veg_mar_Price = (int(veg_mar/100)*int(veg_up))+int(veg_up)
        veg_data.veg_up = veg_up
        veg_data.veg_gst = veg_gst
        veg_data.with_gst = (int(veg_gst/100)*int(veg_up))+int(veg_up)
        veg_data.veg_qty = veg_qty
        veg_data.veg_unit = veg_unit
        veg_data.save()

        vegi_data = Grains.objects.all()
    all_dealer = Dealer_Details.objects.all()
    return render(request,"form/veg_dhal.html",{'dealers':all_dealer} )
#Dhal_BILL
def dhal_bill(request):
    if request.method == 'POST':
        veg_dealer =  request.POST['vd_name']
        veg_invoice = request.POST['veg_invoice']
        veg_invoice_d = request.POST['veg_invoice_d'] 
        veg_amt = request.POST['veg_amt']
        veg_payment = request.POST['veg_payment'] 
        veg_amt1 = request.POST['veg_amt1']
        veg_bill_no = request.POST['veg_bill_no']
        veg_b1_d = request.POST['veg_b1_d']


        veg_bill_data = veg_dhal_bill()
        veg_bill_data.veg_dealer = veg_dealer
        veg_bill_data.veg_invoice = veg_invoice
        veg_bill_data.veg_invoice_d = veg_invoice_d
        veg_bill_data.veg_amt = veg_amt
        veg_bill_data.veg_payment = veg_payment
        veg_bill_data.veg_amt1 = veg_amt1
        veg_bill_data.veg_bill_no = veg_bill_no
        veg_bill_data.veg_b1_d = veg_b1_d
        veg_bill_data.save()
        veg_bill = veg_dhal_bill.objects.all()
    all_dealer = Dealer_Details.objects.all()
    return render(request,"form/dhal_bill.html",{'dealers':all_dealer})
#Product_add
def product_add_form(request):
    if request.method == 'POST':
        pro_name = request.POST['pro_name']
        pro_type = request.POST['pro_type'] 
        pro_dealer =  request.POST['pd_name']
        pro_cat = request.POST['pro_cat']
        pro_mrp = request.POST['pro_mrp'] 
        pro_up = request.POST['pro_up']
        pro_gst = request.POST['pro_gst']
        pro_qty = request.POST['pro_qty']
        pro_unit = request.POST['pro_unit']

        pro_data = AllProduct()
        pro_data.pro_name = pro_name
        pro_data.pro_type = pro_type
        pro_data.pro_dealer = pro_dealer
        pro_data.pro_cat = pro_cat
        pro_data.pro_mrp = pro_mrp
        pro_data.pro_up = pro_up
        pro_data.pro_gst = pro_gst
        pro_data.pro_gst_price = (int(pro_gst/100)*int(pro_up))+int(pro_up)
        pro_data.pro_qty = pro_qty
        pro_data.pro_unit = pro_unit
        pro_data.save()

        pro_data = AllProduct.objects.all()
    all_dealer = Dealer_Details.objects.all()
    return render(request,"form/grocery_add.html",{'dealers':all_dealer} )
#Product_BILL
def product_bill(request):
    if request.method == 'POST':
        pro_dealer =  request.POST['pd_name']
        pro_invoice = request.POST['pro_invoice']
        pro_invoice_d = request.POST['pro_invoice_d'] 
        pro_amt = request.POST['pro_amt']
        pro_payment = request.POST['pro_payment'] 
        pro_amt1 = request.POST['pro_amt1']
        pro_bill_no = request.POST['pro_bill_no']
        pro_b1_d = request.POST['pro_b1_d']


        pro_bill_data = Product_Bill()
        pro_bill_data.pro_dealer = pro_dealer
        pro_bill_data.pro_invoice = pro_invoice
        pro_bill_data.pro_invoice_d = pro_invoice_d
        pro_bill_data.pro_amt = pro_amt
        pro_bill_data.pro_payment = pro_payment
        pro_bill_data.pro_amt1 = pro_amt1
        pro_bill_data.pro_bill_no = pro_bill_no
        pro_bill_data.pro_b1_d = pro_b1_d
        pro_bill_data.save()
        pro_bill = Product_Bill.objects.all()
    all_dealer = Dealer_Details.objects.all()
    return render(request,"form/grocery_bill.html",{'dealers':all_dealer})
#EC Bill
def ec_bill(request):
    if request.method == 'POST':
        sim_name =  request.POST['sim_name']
        ec_paid = request.POST['ec_paid']
        ec_b1_d = request.POST['ec_b1_d']

        ec_bill_data = EC_Bill()
        ec_bill_data.sim_name = sim_name
        ec_bill_data.ec_paid = ec_paid
        ec_bill_data.ec_b1_d = ec_b1_d
        ec_bill_data.save()

        ec_bill = EC_Bill.objects.all()
    all_dealer = Dealer_Details.objects.all()
    return render(request,"form/ec_bill.html",{'dealers':all_dealer})

# Product Price View
# Dealer Details
def dealer_view(request):
    all_dealer = Dealer_Details.objects.all()
    return render(request, "dynamic/dealers.html",{'dealers':all_dealer})
#Medicine_ Price
def med_price(request):
    medi_data = Medi.objects.all()
    return render(request, "dynamic/med_price.html",{'medicine':medi_data})
#Vegetable _ Price
def veg_price(request):
    vegi_data = Grains.objects.all()
    return render(request, "dynamic/veg_price.html",{'veg':vegi_data})
#Dhal_ Price
def dhal_price(request):
    vegi_data = Grains.objects.all()
    return render(request, "dynamic/dhal_price.html",{'veg':vegi_data})
#Grocery Price
def grocery_price(request):
    pro_data = AllProduct.objects.all()
    return render(request, "dynamic/grocery.html",{'pro':pro_data})
#Stationary Price
def stationary_price(request):
    pro_data = AllProduct.objects.all()
    return render(request, "dynamic/stationary.html",{'pro':pro_data})

#Bill View
# All Bill Page
def Bill_view(request):
    medi_bill_data = Medicine_Bill.objects.all()
    veg_bill = veg_dhal_bill.objects.all()
    pro_bill = Product_Bill.objects.all()
    ec_bill = EC_Bill.objects.all()
    return render(request, "bill/bill_page.html",{"med":medi_bill_data,
                'veg':veg_bill,'pro':pro_bill,'ec':ec_bill})
#Medicine Bill
def Med_Bill_view(request):
    medi_bill_data = Medicine_Bill.objects.all()
    return render(request, "bill/med_bill_view.html",{'med':medi_bill_data})
#Grain Bill
def Grain_bill_view(request):
    veg_bill_data = veg_dhal_bill.objects.all()
    all_dealer = Dealer_Details.objects.all()
    return render(request,"bill/grain_bill_view.html",{'veg':veg_bill_data,'bill':all_dealer})
#Product Bill
def product_bill_view(request):
   pro_bill_data = Product_Bill.objects.all()
   all_dealer = Dealer_Details.objects.all()
   return render(request,"bill/product_bill_view.html",{'pro':pro_bill_data,'bill':all_dealer}) 

#Delete Data
#Dealer
def delete_dealer(request,id):
    all_dealer = Dealer_Details.objects.get(id=id)
    all_dealer.delete()
    return redirect(dealer_view)
#Medicine
def delete_medicine(request,id):
    medi_data = Medi.objects.get(id=id)
    medi_data.delete()
    return redirect(med_price)
#Medicine Bill
def delete_med_bill(request,id):
    medi_bill_data = Medicine_Bill.objects.get(id=id)
    medi_bill_data.delete()
    return redirect(Med_Bill_view)
# Vegetable Product
def delete_veg(request,id):
    vegi_data = Grains.objects.get(id=id)
    vegi_data.delete()
    if(vegi_data.veg_category == "Vegetable"):
        return redirect(veg_price)
    else:
        return redirect(dhal_price)
#Vegetable & Dhall Bill
def delete_veg_bill(request,id):
    veg_bill = veg_dhal_bill.objects.get(id=id)
    veg_bill.delete()
    return redirect(Grain_bill_view)
#Product
def delete_pro(request,id):
    pro_data = AllProduct.objects.get(id=id)
    pro_data.delete()
    if(pro_data.pro_cat == "Stationary"):
        return redirect(stationary_price)
    else:
       return redirect(grocery_price) 
# Product Bill
def delete_pro_bill(request,id):
    pro_bill = Product_Bill.objects.get(id=id)
    pro_bill.delete()
    return redirect(pro_bill)
#EC Bill
def delete_ec(request,id):
    ec_bill = EC_Bill.objects.get(id=id)
    ec_bill.delete()
    return redirect(ec_bill)

#Update
#Medicine_Update
def med_update_form(request,id):
    med_data = Medi.objects.get(id=id)
    if request.method == 'POST':
        medicine_name = request.POST['medicine_name']
        med_combination = request.POST['combination'] 
        med_dealer =  request.POST['med_dealer']
        med_category = request.POST['med_category']
        med_mrp = request.POST['med_mrp'] 
        med_up = request.POST['med_up']
        med_gst = request.POST['med_gst']
        med_qty = request.POST['med_qty']
        med_unit = request.POST['med_unit']

        med_data.medicine_name = medicine_name
        med_data.med_combination = med_combination
        med_data.med_dealer = med_dealer
        med_data.med_category = med_category
        med_data.med_mrp = med_mrp
        med_data.med_up = med_up
        med_data.med_gst = med_gst
        med_data.med_u_gst = (int (med_up)*int(med_gst)/100)+int(med_up)
        med_data.med_qty = med_qty
        med_data.med_unit = med_unit
        med_data.save()
        return redirect(med_price)
    all_dealer = Dealer_Details.objects.all()

    return render(request,"update/med_update.html",{'id':med_data,'dealers':all_dealer})
#Medicine Bill Update
def med_bill_upd(request,id):
    med_bill_data = Medicine_Bill.objects.get(id=id)
    if request.method == 'POST':
        med_dealer =  request.POST['med_dealer']
        med_invoice = request.POST['med_invoice']
        med_invoice_d = request.POST['med_invoice_d']
        med_amt = request.POST['med_amt']
        med_payment = request.POST['med_payment'] 
        med_amt1 = request.POST['med_amt1']
        med_bill_no = request.POST['med_bill_no']
        med_b1_d = request.POST['med_b1_d']
        med_amt2 = request.POST['med_amt2']
        med_bill_no2 = request.POST['med_bill_no2']
        med_b2_d = request.POST['med_b2_d']

        med_bill_data.med_dealer = med_dealer
        med_bill_data.med_invoice = med_invoice
        med_bill_data.med_invoice_d = med_invoice_d
        med_bill_data.med_amt = med_amt
        med_bill_data.med_payment = med_payment
        med_bill_data.med_amt1 = med_amt1
        med_bill_data.med_bill_no = med_bill_no
        med_bill_data.med_b1_d = med_b1_d
        med_bill_data.med_amt2 = med_amt2
        med_bill_data.med_bill_no2 = med_bill_no2
        med_bill_data.med_b2_d = med_b2_d
        med_bill_data.save()
        return redirect(Med_Bill_view)
    all_dealer = Dealer_Details.objects.all()
    return render(request,"update/med_bill_update.html",{'id':med_bill_data,'dealers':all_dealer} )
# Veg Update
def veg_update(request,id):
    veg_data = Grains.objects.get(id=id)
    if request.method == 'POST':
        veg_name = request.POST['veg_name']
        veg_mar = request.POST['veg_margin'] 
        veg_dealer =  request.POST['vd_name']
        veg_category = request.POST['veg_cat']
        veg_mrp = request.POST['veg_mrp'] 
        veg_up = request.POST['veg_up']
        veg_gst = request.POST['veg_gst']
        veg_qty = request.POST['veg_qty']
        veg_unit = request.POST['veg_unit']

        veg_data.veg_name = veg_name
        veg_data.veg_mar = veg_mar
        veg_data.veg_dealer = veg_dealer
        veg_data.veg_category = veg_category
        veg_data.veg_mrp = veg_mrp
        veg_data.veg_up = veg_up
        veg_data.veg_mar_Price = (int(veg_mar/100)*int(veg_up))+int(veg_up)
        veg_data.veg_up = veg_up
        veg_data.veg_gst = veg_gst
        veg_data.with_gst = (int(veg_gst/100)*int(veg_up))+int(veg_up)
        veg_data.veg_qty = veg_qty
        veg_data.veg_unit = veg_unit
        veg_data.save()
        if(veg_category == "Grain"):
            return redirect(dhal_price)
        else:
            return redirect(veg_price)
    all_dealer = Dealer_Details.objects.all()
    return render(request,"update/veg_update.html",{'id':veg_data,'dealers':all_dealer} )
# Veg Bill
def veg_bill_upd(request,id):
    veg_bill_data = veg_dhal_bill.objects.get(id=id)
    if request.method == 'POST':
        veg_dealer =  request.POST['vd_name']
        veg_invoice = request.POST['veg_invoice']
        veg_invoice_d = request.POST['veg_invoice_d'] 
        veg_amt = request.POST['veg_amt']
        veg_payment = request.POST['veg_payment'] 
        veg_amt1 = request.POST['veg_amt1']
        veg_bill_no = request.POST['veg_bill_no']
        veg_b1_d = request.POST['veg_b1_d']

        veg_bill_data.veg_dealer = veg_dealer
        veg_bill_data.veg_invoice = veg_invoice
        veg_bill_data.veg_invoice_d = veg_invoice_d
        veg_bill_data.veg_amt = veg_amt
        veg_bill_data.veg_payment = veg_payment
        veg_bill_data.veg_amt1 = veg_amt1
        veg_bill_data.veg_bill_no = veg_bill_no
        veg_bill_data.veg_b1_d = veg_b1_d
        veg_bill_data.save()
        return redirect(Grain_bill_view)
    all_dealer = Dealer_Details.objects.all()
    return render(request,"update/dhal_bill_update.html",{'id':veg_bill_data,'dealers':all_dealer})
#Product Update
def product_update(request,id):
    pro_data = AllProduct.objects.get(id=id)
    if request.method == 'POST':
        pro_name = request.POST['pro_name']
        pro_type = request.POST['pro_type'] 
        pro_dealer =  request.POST['pd_name']
        pro_cat = request.POST['pro_cat']
        pro_mrp = request.POST['pro_mrp'] 
        pro_up = request.POST['pro_up']
        pro_gst = request.POST['pro_gst']
        pro_qty = request.POST['pro_qty']
        pro_unit = request.POST['pro_unit']

        pro_data.pro_name = pro_name
        pro_data.pro_type = pro_type
        pro_data.pro_dealer = pro_dealer
        pro_data.pro_cat = pro_cat
        pro_data.pro_mrp = pro_mrp
        pro_data.pro_up = pro_up
        pro_data.pro_gst = pro_gst
        pro_data.pro_gst_price = (int(pro_gst/100)*int(pro_up))+int(pro_up)
        pro_data.pro_qty = pro_qty
        pro_data.pro_unit = pro_unit
        pro_data.save()
        if(pro_cat == "Stationary"):
            return redirect(stationary_price)
        else:
            return redirect(grocery_price)

    all_dealer = Dealer_Details.objects.all()
    return render(request,"update/grocery_update.html",{'id':pro_data,'dealers':all_dealer} )
#Product Bill Update
def product_bill_upd(request,id):
    pro_bill_data = Product_Bill.objects.get(id=id)
    if request.method == 'POST':
        pro_dealer =  request.POST['pd_name']
        pro_invoice = request.POST['pro_invoice']
        pro_invoice_d = request.POST['pro_invoice_d'] 
        pro_amt = request.POST['pro_amt']
        pro_payment = request.POST['pro_payment'] 
        pro_amt1 = request.POST['pro_amt1']
        pro_bill_no = request.POST['pro_bill_no']
        pro_b1_d = request.POST['pro_b1_d']

        pro_bill_data.pro_dealer = pro_dealer
        pro_bill_data.pro_invoice = pro_invoice
        pro_bill_data.pro_invoice_d = pro_invoice_d
        pro_bill_data.pro_amt = pro_amt
        pro_bill_data.pro_payment = pro_payment
        pro_bill_data.pro_amt1 = pro_amt1
        pro_bill_data.pro_bill_no = pro_bill_no
        pro_bill_data.pro_b1_d = pro_b1_d
        pro_bill_data.save()
        return redirect(product_bill_view)
    all_dealer = Dealer_Details.objects.all()
    return render(request,"update/grocery_bill_update.html",{'id':pro_bill_data,'dealers':all_dealer})
#Order
def med_order(request):    
    medi_data = Medi.objects.all()
    if request.method == 'POST':
        name = request.POST['or_name']
        dealer =  request.POST['or_deal']
        cat = request.POST['or_cat']
        mrp = request.POST['or_mrp'] 
        up = request.POST['or_up']
        gst_price = request.POST['or_gst_price']
        qty = request.POST['or_qty']
        unit = request.POST['or_unit']

        med_data = Medicine_Order()
        med_data.name = name
        med_data.dealer = dealer
        med_data.cat = cat
        med_data.mrp = mrp
        med_data.up = up
        med_data.gst_price = gst_price
        med_data.qty = qty
        med_data.unit = unit
        med_data.save()
    med_order = Medicine_Order.objects.all()
    return render(request, "order/or_med.html",{'medicine':medi_data, 'order':med_order})
def del_med_order(request,id):
    med_data = Medicine_Order.objects.get(id=id)
    med_data.delete()
    return redirect(med_order)
#Grain Order
def grain_order(request):    
    grain_data = Grains.objects.all()
    if request.method == 'POST':
        name = request.POST['or_name']
        dealer =  request.POST['or_deal']
        cat = request.POST['or_cat']
        mrp = request.POST['or_mrp'] 
        up = request.POST['or_up']
        gst_price = request.POST['or_gst_price']
        qty = request.POST['or_qty']
        unit = request.POST['or_unit']

        data = Grain_Order()
        data.name = name
        data.dealer = dealer
        data.cat = cat
        data.mrp = mrp
        data.up = up
        data.gst_price = gst_price
        data.qty = qty
        data.unit = unit
        data.save()
    grain_order = Grain_Order.objects.all()
    return render(request, "order/or_dhal.html",{'grain':grain_data, 'order':grain_order})
#Grain Order Delete
def del_grain_order(request,id):
    grain_data = Grain_Order.objects.get(id=id)
    grain_data.delete()
    return redirect(grain_order)
#Grocery Order
def grocery_order(request):    
    pro_data = AllProduct.objects.all()
    if request.method == 'POST':
        name = request.POST['or_name']
        dealer =  request.POST['or_deal']
        cat = request.POST['or_cat']
        mrp = request.POST['or_mrp'] 
        up = request.POST['or_up']
        gst_price = request.POST['or_gst_price']
        qty = request.POST['or_qty']
        unit = request.POST['or_unit']

        idata = Grocery_Order()
        idata.name = name
        idata.dealer = dealer
        idata.cat = cat
        idata.mrp = mrp
        idata.up = up
        idata.gst_price = gst_price
        idata.qty = qty
        idata.unit = unit
        idata.save()
    grocery_order = Grocery_Order.objects.all()
    return render(request, "order/or_grocery.html" ,{'pro':pro_data, 'order':grocery_order})
#Grocery Order Delete
def del_gro_order(request,id):
    gro_data = Grocery_Order.objects.get(id=id)
    gro_data.delete()
    return redirect(grocery_order)
#Stationary Order
def sta_order(request):    
    pro_data = AllProduct.objects.all()
    if request.method == 'POST':
        name = request.POST['or_name']
        dealer =  request.POST['or_deal']
        cat = request.POST['or_cat']
        mrp = request.POST['or_mrp'] 
        up = request.POST['or_up']
        gst_price = request.POST['or_gst_price']
        qty = request.POST['or_qty']
        unit = request.POST['or_unit']

        idata = Stationary_Order()
        idata.name = name
        idata.dealer = dealer
        idata.cat = cat
        idata.mrp = mrp
        idata.up = up
        idata.gst_price = gst_price
        idata.qty = qty
        idata.unit = unit
        idata.save()
    grocery_order = Stationary_Order.objects.all()
    return render(request, "order/or_sationary.html" ,{'pro':pro_data, 'order':grocery_order})
#Grocery Order Delete
def del_sta_order(request,id):
    gro_data = Grocery_Order.objects.get(id=id)
    gro_data.delete()
    return redirect(grocery_order)