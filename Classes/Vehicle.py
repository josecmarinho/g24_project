# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 15:17:46 2025

@author: migue
"""

from Classes.gclass import Gclass
import pandas as pd

class vehicle(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_id','_model','_make','_price']
    header = 'Vehicle'
    des = ['Vehicle ID','Model','Make','Price']
    def __init__(self, id, model, make, price):
        super().__init__()
        vehicle_id = vehicle.get_id(id)
        self._id = int(vehicle_id)
        self._model = model
        self._make = make
        self._price = float(price)
        vehicle.obj[vehicle_id] = self
        vehicle.lst.append(int(id))
    
    @property
    def id(self):
        return self._id
    @property
    def model(self):
        return self._model
    @property
    def make(self):
        return self._make
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        self._price = float(price)
