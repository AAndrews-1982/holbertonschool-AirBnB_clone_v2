#!/usr/bin/python3
""" Module FileStorage """

import json
import os.path
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ class File Storage serialize and deserialize JSON objects """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ Return the dictionary __objects """
        if not cls:
            return FileStorage.__objects
        out_dict = {}
        for key, val in FileStorage.__objects.copy().items():
            # This doesnt work because the type is
            # set to a weird sqalchemy thing
            if type(val) == type(cls):
                out_dict[key] = val
                # TODO: fix this not giving any output
        return out_dict

    def new(self, obj):
        """ Set in __object the obj with the key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serialize __objects to JSON file """
        dictionary = {}
        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        if not getenv("HBNB_TYPE_STORAGE") == "db":
            for key, value in dictionary.items():
                # _sa_instance_state is not json serializable so if it's
                # there remove it
                if '_sa_instance_state' in value.keys():
                    value.pop('_sa_instance_state')
        with open(FileStorage.__file_path, 'w') as fd:
            json.dump(dictionary, fd)

    def reload(self):
        """ Deserialize __objects from JSON file """

        dct = {'BaseModel': BaseModel,
               'User': User,
               'Place': Place,
               'State': State,
               'City': City,
               'Amenity': Amenity,
               'Review': Review
               }

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as fd:
                obj_dict = json.load(fd)
                for key, value in obj_dict.items():
                    self.new(dct[value['__class__']](**value))
            return

    def delete(self, obj=None):
        """ Deletes obj from __objects """
        if not obj:
            return
        for key, val in FileStorage.__objects.copy().items():
            if val == obj:
                del FileStorage.__objects[key]

    def close(self):
        """ Calls self.reload() """
        self.reload()
