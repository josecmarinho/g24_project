"""
@author: António Brito / Carlos Bragança (2025)
#objective: class Order
"""""
# Class CustomerOrder
import datetime
from Classes.Service_center import service_center
# Import the generic class
from Classes.gclass import Gclass

class CustomerOrder(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_date','_service_center_id']
    # Class header title
    header = 'Customer Order'
    # field description for use in, for example, input form
    des = ['Id','Date','Service_center_id']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, date, service_center_id):
        super().__init__()
        # Object attributes
        # Check the customer referential integrity
        service_center_id =int(service_center_id)
        if service_center_id in service_center.lst:
            id = CustomerOrder.get_id(id)
            self._id = int(id)
            self._date = datetime.date.fromisoformat(date)
            self._service_center_id = service_center_id
            # Add the new object to the Order list
            CustomerOrder.obj[id] = self
            CustomerOrder.lst.append(id)
        else:
            print('Service_center ', service_center_id, ' not found')
    # Object properties
    # code property getter method
    @property
    def id(self):
        return self._id
    # date property getter method
    @property
    def date(self):
        return self._date
    # date property setter method
    @date.setter
    def date(self, date):
        self._date = date
    # customer property getter method
    @property
    def service_center_id(self):
        return self._service_center_id
    # customer property setter method
    @service_center_id.setter
    def customer_id(self, service_center_id):
        if service_center_id in service_center.lst:
            self._service_center_id = service_center_id
        else:
            print('Service_center ', service_center_id, ' not found')    
            