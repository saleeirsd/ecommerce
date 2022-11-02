from django.urls import path
from . import views
app_name= 'common'

urlpatterns = [
    path('',views.common_index,name = 'home'),
    path('admin',views.common_admin,name = 'admin'),
    path('customer',views.common_customer,name = 'customer'),
    path('seller',views.common_seller,name = 'seller'),
    path('cart',views.common_cart,name = 'cart')
]   