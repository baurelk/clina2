

from django import forms
from .models import ClothingCat
 
 
# creating a form
class ClothingCatForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = ClothingCat
 
        # specify fields to be used
        fields = [
            "name",
            "description",
            "defaultPrice",
        ]