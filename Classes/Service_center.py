"""
@author: António Brito / Carlos Bragança (2025)
#objective: class Customer_login
"""
# Class Customer_login
# Import the generic class
from Classes.gclass import Gclass
import pandas as pd
class Service_center(Gclass):
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
        id = Service_center.get_id(id)
        self._id = id
        self._name = name
        self._location= location
        # Add the new object to the Customer's list
        Service_center.obj[id] = self
        Service_center.lst.append(id)
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
def load_centers_from_csv(file_path):
    df = pd.read_csv(file_path, encoding="utf-8", low_memory=False)
    centers_created = {} 
    for _, row in df.iterrows():
        service_id = str(row["servicecenter_id"])
        name = row["center_name"]
        location = row["service_location"]
        
        
        if service_id not in centers_created:
            centers_created[service_id] = Service_center(service_id, name, location)
    
    print(f"{len(centers_created)} centers carregados com sucesso!")
    return centers_created
load_centers_from_csv('G24_Automotive – Dealers  Vehicles with Service Centers_merged.csv')