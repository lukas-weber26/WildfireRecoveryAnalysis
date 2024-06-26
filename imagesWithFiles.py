import pandas as pd
import numpy as np
import os 
import glob
import re 

data = pd.read_csv("All_HousingRecovery.csv")

#for i in data.index:
#    data.loc[i, "ImageName"] = "Index:" + str(i) + " Lat:" + str(data.loc[i,"Latitude"]) + " Long:" +  str(data.loc[i,"Longitude"])  + " Date:"

for d in range(2008,2025):
    data["Image"+str(d)] = "NA"

files = os.listdir("./general/")

indexR = re.compile("(?<=Index:).*(?=\sLat)")
indexD = re.compile("(?<=Date:).*(?=-)")

i = 0

for file in files:
    index = int(re.search(indexR,file)[0])
    year = str(re.search(indexD,file)[0])
    data.loc[index, ("Image"+year)]  = file 
    print(i)
    i += 1
    #at this point can add the filename to the dataframe 

#print(data.columns)
data.to_csv("withImgNames.csv")



