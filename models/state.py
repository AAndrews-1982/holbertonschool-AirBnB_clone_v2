#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage
from models.city import City
import os
import models

if os.getenv("HBNB_TYPE_STORAGE") == 'db':


class State(BaseModel, Base):
    """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")

    else:

        class State(BaseModel):
            """ File Storage """
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        
        def cities(self):
            """Returns a list of City instances with state_id = id"""
            cities = []
            for thing in models.storage.all("City").values():
                if thing.state_id == self.id:
                    cities.append(thing)
            return cities
