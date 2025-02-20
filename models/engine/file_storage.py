#!/usr/bin/python3
"""defines a class to manage file storage for hbnb clone"""
import json
from models import city, place, review, state, amenity, user, base_model


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    CDIC = {
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'Amenity': amenity.Amenity,
        'User': user.User
    }

    def all(self, cls=None):
        """returns dict of models in storage
        if cls specified returns that class"""
        if cls is not None:
            if cls in self.CDIC.keys():
                cls = self.CDIC.get(cls)
            spec_rich = {}
            for ky, vl in self.__objects.items():
                if cls == type(vl):
                    spec_rich[ky] = vl
            return spec_rich
        return self.__objects

    def new(self, obj):
        """adds new object to storage dict"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """saves storage dict to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """loads storage dict from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """if obj deletes obj from __objects"""
        try:
            key = obj.__class__.__name__ + "." + obj.id
            del self.__objects[key]
        except (AttributeError, KeyError):
            pass

    def close(self):
        self.reload()
