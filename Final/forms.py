from django import forms
from .models import *

class CargaZapato(forms.ModelForm):
    class Meta:
        model = Zapatos
        fields = ['tipo','color','material', 'numero']
    
    
class CargaCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','apellido','condicion']
    
class CargaProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['razonsocial','condicion','mail']