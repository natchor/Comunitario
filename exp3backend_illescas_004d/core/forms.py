from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.forms import widgets
from django.forms.forms import Form
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import User,Vehiculo

class VehiculoForms(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields =['patente','marca','modelo','user']
        labels ={ 
            'patente':'Patente del Vehiculo',
            'marca':'Modelo del Vehiculo',
            'modelo':'Modelo del Vehiculo',
            'User': 'Propietario del Vehiculo'
        }
        widgets={

            'patente':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Patente',
                    'id':'patente'
                }
            ),

            'marca':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Marca',
                    'id':'marca'
                }
            ),

            'modelo':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Modelo',
                    'id':'modelo'
                }
            ),
            'user':forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'user'
                }
            )


        }

class USerForms(forms.ModelForm):
    class Meta:
        model = User
        fields =['idUser','nombreUser','correo','password','nac']
        labels ={ 
            'idUser':'nickname',
            'nombreUser':'Nombre usuario',
            'correo':'Correo',
            'password': 'Pass usuario '
        }
        widgets={

            'idUser':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese nickname',
                    'id':'IdUser'
                }
            ),

            'nombreUser':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese nombre usuario',
                    'id':'Nombre'
                }
            ),

            'correo':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese correo',
                    'id':'Correo'
                }
            ),

            'password':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese password',
                    'id':'Password'
                }
            ),

            'nac':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese fecha nacimiento',
                    'id':'Fecha'
                
                }
            ),

            

        }        