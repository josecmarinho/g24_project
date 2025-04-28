"""
@author: António Brito / Carlos Bragança (2025)
#objective: class OrderProduct
"""""
# Class OrderProduct
from Classes.dealer import dealer
from Classes.Vehicle import vehicle
vehicle.read("data/vehicle.db")
dealer.read("data/dealer.db")
dealer_l=dealer.lst
vehicle_l=vehicle.lst

# Import the generic class
from Classes.gclass import Gclass
import datetime
import pandas as pd

class sales(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier id, attribute must be the first on the list
    att = ['_id', '_dealer_id','_vehicle_id','_price',"_date"]
    # Class header title
    header = 'Persons'
    # field description for use in, for example, input form
    des = ['Id','Order_id','Customer_id','Price',"Date"]
    # Constructor: Called when an object is instantiated
    def __init__(self, id, dealer_id, vehicle_id, price,date):
        super().__init__()
        # Object attributes
        vehicle_id=int(vehicle_id)
        # Check the order and product referential integrity
        if dealer_id in dealer_l:
            if vehicle_id in vehicle_l:
                self._id = (id)
                self._dealer_id = (dealer_id)
                self._vehicle_id = (vehicle_id)
                self._price = float(price)
                l=date.split("-")
                self._date=datetime.date(int(l[0]),int(l[1]),int(l[2]))
                # Add the new object to the OrderProduct list
                sales.obj[id] = self
                sales.lst.append(id)
            else:
                print('Vehicle ', vehicle_id, ' not found')
        else:
            print('Dealer ', dealer_id, ' not found')
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    # order property getter method
    @property
    def dealer_id(self):
        return self._dealer_id
    # product property getter method
    @property
    def vehicle_id(self):
        return self._vehicle_id
    # quantity property getter method

    @property
    def price(self):
        return self._price
    # price property setter method
    @price.setter
    def price(self, price):
        self._price = float(price)
        
    @property
    def date(self):
         return self._date

        