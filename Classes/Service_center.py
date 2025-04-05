"""
@author: António Brito / Carlos Bragança (2025)
#objective: class Customer_login
"""
# Class Customer_login
# Import the generic class
from Classes.gclass import Gclass
import pandas as pd
class service_center(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_name',"_location"]
    # Class header title
    header = 'Service_centers'
    # field description for use in, for example, input form
    des = ['Id','Name','Location']
    # Constructor: Called when an object is instantiated
    def __init__(self,id,name,location):
        super().__init__()
        # Object attributes
        id = service_center.get_id(id)
        self._id = int(id)
        self._name = name
        self._location= location
        # Add the new object to the Customer's list
        service_center.obj[id] = self
        service_center.lst.append(id)
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    # name property getter method
    @property
    def name(self):
        return self._name
    @property
    def service_location(self):
        return self._location