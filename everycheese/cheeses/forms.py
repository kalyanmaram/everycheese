from django import forms
from .models import Cheese
from .models import Rating

class CheeseUpdateForm(forms.ModelForm):
    class Meta:
        model = Cheese
        fields = ['name', 'description', 'firmness', 'country_of_origin']
    
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating'] 
