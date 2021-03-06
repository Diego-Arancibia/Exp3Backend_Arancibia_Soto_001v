from django import forms
from django.forms import fields
from .models import Contacto, Producto



class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

        widgets ={
        "fecha_despacho": forms.SelectDateWidget()
    }
