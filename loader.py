import numpy as np 
import pandas as pd 
from streetview import search_panoramas
from streetview import get_streetview
import os 

data = pd.read_csv('All_HousingRecovery.csv')
#print(data[["Latitude","Longitude"]])

for index in data.index:
    if (index > 1077):
        latitude = data['Latitude'][index]
        longitude = data['Longitude'][index]
        print(index, latitude, longitude)
        panos = search_panoramas(lat=latitude, lon=longitude)
        imageCount = 0 

        for p in panos:
            if ((p.date != None) and (imageCount < 10000)):
                name = "Index:" + str(index) + " Lat:" + str(latitude) + " Long:" + str(longitude) + " Date:" + str(p.date)
                image = get_streetview(pano_id=p.pano_id,api_key="")

                path_general = "general" 
                path_specific = "Lat:" + str(latitude) + " Long:" + str(longitude)
                
                if os.path.exists(path_general):
                    pass 
                else:
                    os.mkdir(path_general)

                if os.path.exists(path_specific):
                    pass 
                else: 
                    os.mkdir(path_specific)

                generalSave = 'general/' + name
                specificSave = "Lat:" + str(latitude) + " Long:" + str(longitude) + "/" + name
                image.save(generalSave , "jpeg")
                image.save(specificSave, "jpeg")
            
                imageCount = imageCount + 1
