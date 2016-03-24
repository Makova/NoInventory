from django import forms
from django.contrib.auth.models import User
from NoInventory.models import *

from clasificacion import *

from bson import Binary, Code
from bson.json_util import dumps
from bson.json_util import loads
import json
import os

from pymongo import MongoClient

ON_COMPOSE = os.environ.get('COMPOSE')
if ON_COMPOSE:
    client = MongoClient('mongodb://172.17.0.2:27017/')
else:
    client = MongoClient('mongodb://localhost:27017/')
db = client['noinventory-database']

manejadorClasificacion=ClasificacionDriver()


class ItemForm(forms.Form):
    lista_tag1=manejadorClasificacion.database.tag1.find()
    lista_tag2=manejadorClasificacion.database.tag2.find()
    lista_tag3=manejadorClasificacion.readTag3()


    nombre_item = forms.CharField(required=True,max_length=150, help_text="Introduce el nombre del objeto")
    descripcion_item  = forms.CharField(required=True,max_length=300, help_text="Breve descripcion sobre el objeto")
    tag_item = forms.CharField(required=True, max_length=150, help_text="Tag para ayudar a clasificar el objeto")
    tag1 = forms.ChoiceField(label="TAG 1", choices=[(x["VALOR1"], x["VALOR1"]) for x in lista_tag1])
    tag2 = forms.ChoiceField(label="TAG 2", choices=[(x["VALOR2"], x["VALOR2"]) for x in lista_tag2])
    tag3 = forms.ChoiceField(label="TAG 3", choices=[(x["VALOR3"], x["VALOR3"]) for x in lista_tag3])



class InventarioForm(forms.ModelForm):
    nombre_inventario = forms.CharField(max_length=150, help_text="Introduce el nombre del inventario")
    descripcion_inventario  = forms.CharField(widget = forms.Textarea, help_text="Breve descripcion sobre el inventario")
    tag_inventario = forms.CharField(max_length=150, help_text="Tag para ayudar a clasificar el inventario")
    caracteristicas_inventario = forms.CharField(widget = forms.Textarea, help_text="Caracteristicas del inventario para clasificar los objetos")


    class Meta:
        model = Inventario
        fields = ('nombre_inventario','descripcion_inventario','tag_inventario','caracteristicas_inventario')

class SelectItem(forms.Form):
    def __init__(self,*args,**kwargs):
        super(SelectItem, self).__init__(*args,**kwargs)
        lista_items=db.items.find()
        self.fields['items'] = forms.ChoiceField(label="items", choices=[(x["nombre_item"], x["nombre_item"]) for x in lista_items])

class DocumentForm(forms.Form):
    archivo = forms.FileField(label='Selecciona fichero csv',help_text='max. 42 megabytes')
