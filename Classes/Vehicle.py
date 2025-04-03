# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 15:17:46 2025

@author: migue
"""

from Classes.gclass import Gclass
import pandas as pd

class Vehicle(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_id','_model','_make','_price']
    header = 'Vehicle'
    des = ['Vehicle ID','Model','Make','Price']
    def __init__(self, id, model, make, price):
        super().__init__()
        vehicle_id = Vehicle.get_id(id)
        self._id = float(vehicle_id)
        self._model = model
        self._make = make
        self._price = float(price)
        Vehicle.obj[vehicle_id] = self
        Vehicle.lst.append(vehicle_id)
    
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
def load_vehicles_from_csv(file_path):
    df = pd.read_csv(file_path, encoding="utf-8", low_memory=False)
    vehicles_created = {} 
    for _, row in df.iterrows():
        vehicle_id = str(row["vehicle_id"])
        model = row["model"]
        make = row["make"]
        price = row["price"]
        
        if vehicle_id not in vehicles_created:
            vehicles_created[vehicle_id] = Vehicle(vehicle_id, model, make, price)
    
    print(f"{len(vehicles_created)} veículos carregados com sucesso!")
    return vehicles_created
load_vehicles_from_csv('G24_Automotive – Dealers  Vehicles with Service Centers_merged.csv')
