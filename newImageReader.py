import pandas as pd
import numpy as np
import os 
from PIL import Image 

data = pd.read_csv("withImgNames.csv")

def HSVToGreen(name):
    img = Image.open("general/" + name)
    im = np.asarray(img.convert('HSV'))
    greenCount = 0
    current = 0

    for i in range(640):
        for j in range(640):
            current = (im[i,j,0])
            if (current > 57 and current < 98):
                greenCount += 1

    return 100* greenCount / (640*640) 


#UNFORTUNATELY THIS COEFFICIENT REQUIES A THRESHOLD WHICH IS NOT REPORTED. 
#I AM JUST USING 2 FOR NOW
def RGBToGreen(name):
    img = Image.open("general/" + name)
    im = np.asarray(img.convert('RGB'))
    greenCount = 0;

    for i in range(640):
        for j in range(640):
            r = im[i,j,0];
            g = im[i,j,1];
            b = im[i,j,2];
            gmr = g - r
            gmb = g - b
            diff = gmr*gmb

            if (gmr > 0 and diff > 2): 
                greenCount += diff 

    return 100* greenCount / (640*640) 

def addNewRow(rowName, rowFunction):
    print("C1")
    for item in range(2008,2025):
        #make the new column
        data[rowName+str(item)] = ""
        print("C2")
       
        for i in range(0,len(data)):
            imgName = data.loc[i,"Image"+str(item)]
            if (not pd.isna(imgName)):
                val = rowFunction(imgName) 
                data.loc[i, rowName+str(item)] = val
                print(item," ",i)


addNewRow("HSVGreen",HSVToGreen)
#addNewRow("RGBGreen",RGBToGreen)

data.to_csv("DataWithHSVGreenVals")


