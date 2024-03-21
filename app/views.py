from django.shortcuts import render

from app.decorator import unauthenticate

# Create your views here.

# @unauthenticate
def dashbordView(request):
    context = {
        "author": "Gaurav Singhal",
        "website": {
            "domain": "https://pluralsight.com",
            "views": 200
        },
        "odds": [1, 3, 5]
    }
    return render(request, "dashboad.html", context)
