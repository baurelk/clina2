from django.shortcuts import render

from app_params.forms import ClothingCatForm
from app_params.models import ClothingCat

def clothingCatPage(request):
    context ={}
    
    if request.method == 'POST':
        context["ClothingCats"] = ClothingCat.objects.all()
        # add the dictionary during initialization
    
    if request.method == 'POST':
        form = ClothingCatForm(request.POST or None)
        if form.is_valid():
            form.save()
            context['form'] = form
            context["ClothingCats"] = ClothingCat.objects.all()
            

    return render(request, "app_params/clothing_cat_page.html", context)
