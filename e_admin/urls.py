from django.urls import path
from . import views
app_name= 'e_admin'

urlpatterns = [
    path('index',views.e_admin_index,name = 'e_admin_index'),
]