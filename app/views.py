from django.shortcuts import render

from app.decorator import unauthenticate

# Create your views here.

# @unauthenticate

@unauthenticate
def dashbordView(request):
    context = {
        
    }
    return render(request, "dashboad.html", context)
