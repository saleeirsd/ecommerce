from django.shortcuts import render

# Create your views here.
def common_index(request):
    return render(request,'common_templates/index.html')

def common_admin(request):
    return render(request,'common_templates/adminlogin.html')

def common_customer(request):
    return render(request,'common_templates/customerlogin.html')

def common_seller(request):
    return render(request,'common_templates/sellerlogin.html')

def common_cart(request):
    return render(request,'common_templates/cart.html')                