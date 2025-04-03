import datetime
from Classes.Service_center import Service_center
from Classes.gclass import Gclass
import pandas as pd
class Dealer(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_dealer_id', '_name', '_location', '_rating']
    header = 'Dealer'
    des = ['Dealer ID', 'Name', 'Location', 'Rating']

    # Construtor
    def __init__(self, id, name, location, rating):
        super().__init__()
        dealer_id = Dealer.get_id(id)
        self._id = dealer_id  
        self._name = name
        self._location = location
        self._rating = float(rating)  

        Dealer.obj[dealer_id] = self
        Dealer.lst.append(dealer_id)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        self._rating = float(rating)  
    
def load_dealers_from_csv(file_path):
    df = pd.read_csv(file_path, encoding="utf-8", low_memory=False)
    dealers_created = {} 
    for _, row in df.iterrows():
        dealer_id = str(row["dealer_id"])
        name = row["name"]
        location=row["location"]
        rating=row["rating"]
        
        if dealer_id not in dealers_created:
            dealers_created[dealer_id] = Dealer(dealer_id, name, location, rating)
    
    print(f"{len(dealers_created)} dealers carregados com sucesso!")
    return dealers_created
load_dealers_from_csv('G24_Automotive – Dealers  Vehicles with Service Centers_merged.csv')

