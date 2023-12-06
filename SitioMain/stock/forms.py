from stock.models import Sable, Componente, Crystal
from django import forms

# creamos los formularios para traer los datos (SableFormulario/etc)
class SableFormulario(forms.Form):
    nombre= forms.CharField()
    stock= forms.IntegerField()
    precio=forms.FloatField()
    descripcion= forms.CharField()
    medida= forms.CharField()
    color_sable= forms.CharField()
    color_luz= forms.CharField() 
    
class CrystalFormulario(forms.Form):
    nombre= forms.CharField(initial="Kyber Crystal") 
    color= forms.CharField()
    origen= forms.CharField() 
    stock= forms.IntegerField()
    precio= forms.FloatField()
    descripcion= forms.CharField()
    
    
class ComponenteFormulario(forms.Form):
    tipo= forms.CharField() # mostrar listado de tipos?
    nombre= forms.CharField() 
    material= forms.CharField() # mostrar listado de materiales?
    stock= forms.IntegerField()
    precio= forms.FloatField()
    descripcion= forms.CharField()
    
    
    