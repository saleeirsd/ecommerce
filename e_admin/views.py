from django.shortcuts import render

# Create your views here.
def e_admin_index(request):
    return render(request,'e_admin_templtaes/admin.html')