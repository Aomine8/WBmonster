from django import forms
from ..prod.models import Product, Question

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'