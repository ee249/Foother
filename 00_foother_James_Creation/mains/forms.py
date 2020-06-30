from django import forms
from .models import Food, Emotion

class EmotionForm(forms.ModelForm):
     class Meta:
         model = Emotion


class FoodForm(forms.ModelForm):
     class Meta:
         model = Food





        