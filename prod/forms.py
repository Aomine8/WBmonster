from django import forms
from .models import Product, Questions

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'