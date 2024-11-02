from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
   
    # ADD FORM
    path("add_dealer",views.dealer_add,name="add dealer"),
    path("add_medicine", views.med_add_form,name="add medicine"),
    path("add_medicine_bill", views.med_bill, name="add medicine bill"),
    path("add_vegetable", views.veg_dhal_add_form, name="add vegetable"),
    path("add_vegetable_bill",views.dhal_bill, name="add dhal bill"),
    path("add_product",views.product_add_form,name="add product"),
    path("add_product_bill", views.product_bill, name="add product bill"),
    path("add_ec_bill",views.ec_bill, name="add ec bill"),
    # Bill View 
    path("store_bill",views.Bill_view, name="All Bill"),
    path("Medical_bill",views.Med_Bill_view, name="Medical Bill"),
    path("grain_bill",views.Grain_bill_view, name="Grain & Veg Bill"),
    path("product_bill",views.product_bill_view, name="Product Bill"),
    # Details/ Price
    path("dealer_details",views.dealer_view,name='View Dealer Details'),
    path("medicine_Price",views.med_price,name='Medicine Pirce'),
    path("vegetable_Price",views.veg_price,name='Vegetable Pirce'),
    path("grain_Price",views.dhal_price,name='Grain Pirce'),
    path("grocery_Price",views.grocery_price,name='Grocery Pirce'),
    path("stationary_Price",views.stationary_price,name='Stationary Pirce'),
    # Order Add
    path("medicine_order",views.med_order,name='Medicine Order'),
    path("delete_med_order/<int:id>",views.del_med_order,name='Delete Medicine Order'),
    path("grain_order",views.grain_order,name='Grain Order'),
    path("delete_grain_order/<int:id>",views.del_grain_order,name='Grain Order'),
    path("grocery_order",views.grocery_order,name='Grocery Order'),
    path("deldete_grocery_order/<int:id>",views.del_gro_order,name='Delete Grocery Order'),
    path("stationary_order",views.sta_order,name='Stationary Order'),
    path("delete_stationary_order/<int:id>",views.del_sta_order,name='Stationary Order'),
    #Delete Datas
    path("delete_dealer/<int:id>", views.delete_dealer, name="Delete Medicine"),
    path("delete_medicine/<int:id>", views.delete_medicine, name="Delete Medicine"),
    path("delete_medicine_bill/<int:id>", views.delete_med_bill, name="Delete Medicine Bill"),
    path("delete_veg&dhal/<int:id>", views.delete_veg, name="Veg & Dhall"),
    path("delete_veg_bill/<int:id>", views.delete_veg_bill, name="Delete Dhall Bill"),
    path("delete_product/<int:id>", views.delete_pro, name="Delete Product"),
    path("delete_product_bill/<int:id>", views.delete_pro_bill, name="Delete Product Bill"),
    path("delete_ec_bill/<int:id>", views.delete_ec, name="Delete EC Bill"),
    # Update
    path('update_medicine/<int:id>', views.med_update_form ,name="update medicine"),
    path('update_veg/<int:id>', views.veg_update ,name="update Veg&Grain"),
    path('update_product/<int:id>', views.product_update ,name="update Product"),
    # Bills
    path('update_medicine_bill/<int:id>', views.med_bill_upd ,name="update Medical Bill"),
    path('update_Grain_bill/<int:id>', views.veg_bill_upd ,name="update Veg&Grain Bill"),
    path('update_product_bill/<int:id>', views.product_bill_upd ,name="update Product Bill"),


]