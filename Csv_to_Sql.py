# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 15:28:20 2025

@author: josec
"""

import pandas as pd
df = pd.read_csv('G24_Automotive – Dealers  Vehicles with Service Centers_merged.csv', sep = ';')
Vehicles=df.loc[:,['vehicle_id','model','make','price',]]
Vehicles=Vehicles.sort_values(by="vehicle_id")
Vehicles.drop_duplicates(inplace=True)
import sqlite3
conexao = sqlite3.connect('Dados.db')
Vehicles.to_sql('Vehicles', conexao, if_exists='replace', index=False)



Service_center=df.loc[:,['servicecenter_id','service_location','center_name',]]
Service_center=Service_center.sort_values(by="servicecenter_id")
Service_center.drop_duplicates(inplace=True)
Service_center.to_sql('Service_centers', conexao, if_exists='replace', index=False)

Dealer=df.loc[:,['dealer_id','name','location',"rating",]]
Dealer=Dealer.sort_values(by="servicecenter_id")
Dealer.drop_duplicates(inplace=True)
Dealer.to_sql('Dealer', conexao, if_exists='replace', index=False)
conexao.close()