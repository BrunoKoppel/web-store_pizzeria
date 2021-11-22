from django import forms
from .models import Pizza, Topping
# dob = forms.DateField(auto_now=False)
# dob = Pizza.DateField(auto_now=False)

class PizzaForm(forms.ModelForm):
  name = forms.CharField(max_length=50, required=True)
  # nested class
  class Meta:
    model = Pizza
    fields = ['name']
    labels = {'name': ''}

class ToppingForm(forms.ModelForm):
  name = forms.CharField(max_length=50, required=True)
  # nested class
  class Meta:
    model = Topping
    fields = ['name']
    labels = {'name': ''}
    widgets = {'name': forms.Textarea(attrs={'cols':80})}