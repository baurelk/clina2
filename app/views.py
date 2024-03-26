from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.decorator import unauthenticated_user

# Create your views here.

# @unauthenticate

@login_required(login_url='login')
def dashbordView(request):
    context = {
        "PageName":"Dashboard",
        "PageNameDesction":"Dashboard"
    }
    return render(request, "dashboad.html", context)


def AddCustomer(request):
    context = {
        "PageName":"AddCustomer",
        "PageNameDesction":" Add a new customer"
    }
    return render(request, "customer/add_customer.html", context)
    