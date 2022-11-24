#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 15:21:06 2022

@author: u0145079
"""
###########################################
######Downloading COG annotation###########
###########################################

import requests
import json
import pandas as pd
import itertools 

#Provide URL for the API:ie. https://www.ncbi.nlm.nih.gov/research/cog/api/cog/?organism=Nitrosopumilus_maritimus_SCM1

url = "https://www.ncbi.nlm.nih.gov/research/cog/api/cog/?organism=Bacteroides_thetaiotaomicron_VPI-5482"

# Grab the search results
response = requests.get(url)
resp_dict = response.json()

#start with the empty list
df=pd.DataFrame()

# Store the first page of results

counter = 0
for i in range(len(resp_dict["results"])): 
    df.loc[counter,"cogs"] = resp_dict["results"][i]["cog"]["cogid"] 
    df.loc[counter, "ids"] = resp_dict["results"][i]["gene_tag"]
    df.loc[counter, "description"] = resp_dict["results"][i]["cog"]["funcats"][0].get('description')
    counter+=1

# While data['next'] isn't empty,vdownload the next page:
while resp_dict['next'] is not None:
    print("Next page found, downloading", resp_dict['next'])
    response = requests.get(resp_dict['next'])
    resp_dict = response.json()
    # Store the current page of results
    for i in range(len(resp_dict["results"])):
        df.loc[counter,"cogs"] = resp_dict["results"][i]["cog"]["cogid"] 
        df.loc[counter, "ids"] = resp_dict["results"][i]["gene_tag"]
        df.loc[counter, "description"] = resp_dict["results"][i]["cog"]["funcats"][0].get('description')
        counter+=1
       
df.to_csv(path)










