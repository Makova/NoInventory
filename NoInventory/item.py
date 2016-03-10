from bson.objectid import ObjectId
from pymongo import MongoClient
import time



class Item(object):
    """Clase para almacenar informacion de los items"""

    def __init__(self, item_id=None,nombre_item=None,fecha_alta_item=None, descripcion_item=None,tag_item=None,tipo_item=None,estado_item=None,codigo_centro=None,centro=None):

        if item_id is None:
            self._id = ObjectId()
        else:
            self._id = item_id

        self.nombre_item=nombre_item
        self.fecha_alta_item = time.strftime("%c")
        self.descripcion_item = descripcion_item
        self.tag_item=tag_item
        self.tipo_item=tipo_item
        self.estado_item=estado_item
        self.codigo_centro=codigo_centro
        self.centro=centro

    def get_as_json(self):
        """ Metodo que devuelve el objeto en formato Json, para almacenar en MongoDB """
        return self.__dict__


    @staticmethod
    def build_from_json(json_data):
        """ Metodo usado para contruir objetos item apartir de Json"""
        if json_data is not None:
            try:
                #print"Jsonnnn"
                #print json_data
                return Item(json_data.get('_id', None),
                    json_data['nombre_item'],
                    json_data['fecha_alta_item'],
                    json_data['descripcion_item'],
                    json_data['tag_item'],
                    json_data['tipo_item'],
                    json_data['estado_item'],
                    json_data['codigo_centro'],
                    json_data['centro'])
            except KeyError as e:
                raise Exception("Clave no encontrada en json: {}".format(e.message))
        else:
            raise Exception("No hay datos para crear un Item!")


class ItemsDriver(object):
    """ ItemsDriver implemeta las funcionalidades CRUD para administrar items """

    def __init__(self):
        # inizializar MongoClient
        # aacceso a la base de datos
        self.client = MongoClient(host='localhost', port=27017)
        self.database = self.client['items']


    def create(self, item):
        if item is not None:
            self.database.items.insert(item.get_as_json())
        else:
            raise Exception("Imposible crear Item")


    def read(self, item_id=None):
        if item_id is None:
            return self.database.items.find()
        else:
            return self.database.items.find({"_id":ObjectId(item_id)})


    def update(self, item):
        if item is not None:
            # the save() method updates the document if this has an _id property
            # which appears in the collection, otherwise it saves the data
            # as a new document in the collection
            self.database.items.save(item.get_as_json())
        else:
            raise Exception("Imposible actualizar Item")


    def delete(self, item):
        if item is not None:
            self.database.items.remove(item.get_as_json())
        else:
            raise Exception("Imposible Borrar")

    def destroyDriver(self):
        self.database.items.remove()