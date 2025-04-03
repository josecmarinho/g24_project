"""
@author: António Brito / Carlos Bragança (2025)
#objective: class OrderProduct
"""""
# Class OrderProduct
from Classes.dealer import Dealer
from Classes.Vehicle import Vehicle
# Import the generic class
from Classes.gclass import Gclass
import datetime
import pandas as pd

class Sales(Gclass):
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
        # Check the order and product referential integrity
        Dealer_id = float(dealer_id)
        Vehicle_id = float(vehicle_id)
        if Dealer_id in Dealer.lst:
            if Vehicle_id in Vehicle.lst:
                id = Sales.get_id(id)
                self._id = id
                self._dealer_id = dealer_id
                self._vehicle_id = vehicle_id
                self._price = float(price)
                l=date.split("-")
                self._date=datetime.date(int(l[0]),int(l[1]),int(l[2]))
                # Add the new object to the OrderProduct list
                Sales.obj[id] = self
                Sales.lst.append(id)
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
    
def load_sales_from_csv(file_path):
    df = pd.read_csv(file_path, encoding="utf-8", low_memory=False)
    sales_created = {} 
    for _, row in df.iterrows():
        vehicle_id = str(row["vehicle_id"])
        dealer_id= str(row["dealer_id"])
        price = row["sale_price"]
        date=row["sale_date"]
        