import datetime

from Classes.gclass import Gclass
import pandas as pd
class dealer(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_id', '_name', '_location', '_rating']
    header = 'Dealer'
    des = ['Dealer ID', 'Name', 'Location', 'Rating']

    # Construtor
    def __init__(self, id, name, location, rating):
        super().__init__()
        dealer_id = dealer.get_id(id)
        self._id = int(dealer_id)  
        self._name = name
        self._location = location
        self._rating = float(rating)  

        dealer.obj[id] = self
        dealer.lst.append(id)

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



