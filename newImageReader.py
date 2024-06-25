import pandas as pd
import numpy as np
import os 
from PIL import Image 
import glob

data = pd.read_csv("All_HousingRecovery.csv")
data["ImageName"] = "";


def addNewRow(rowName, rowFunction):
    for item in range(2010,2024):
        #add a new column
        data[str(rowName) + str(item)] = item

        for i in data.index:
            #step 1: Find if the image exists and what it's name is 
            fName = "./general/" + data.loc[i,"ImageName"] + str(item) + "*"
            print(fName) 

            for f in glob.glob(fName):
                print(f)
                image = Image.open(f)
                print("Got one!")
                #step 2: Run the classification function on the image 
                break

for i in data.index:
    data.loc[i, "ImageName"] = "Index:" + str(i) + " Lat:" + str(data.loc[i,"Latitude"]) + " Long:" +  str(data.loc[i,"Longitude"])  + " Date:"

#Index:945 Lat:38.48036703 Long:-122.7426521 Date:2011

addNewRow("HSV","")
#print(data.columns)

#print(glob.glob("./general/*"))
