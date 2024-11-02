from django.contrib import admin
from .models import Dealer_Details,Medi,Grains,AllProduct,Medicine_Bill,veg_dhal_bill,Product_Bill,EC_Bill,Medicine_Order,Grain_Order,Grocery_Order,Stationary_Order
# Register your models here.
admin.site.register(Dealer_Details)
admin.site.register(Medi)
admin.site.register(Grains)
admin.site.register(AllProduct)
#Bill
admin.site.register(Medicine_Bill)
admin.site.register(veg_dhal_bill)
admin.site.register(Product_Bill)
admin.site.register(EC_Bill)
# Order
admin.site.register(Medicine_Order)
admin.site.register(Grain_Order)
admin.site.register(Grocery_Order)
admin.site.register(Stationary_Order)
