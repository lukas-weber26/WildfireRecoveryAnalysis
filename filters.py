import numpy as np
from PIL import Image 

def HSVToGreen(img):
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
def RGBToGreen(img):
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


image = Image.open("general/Index:998 Lat:38.47802812 Long:-122.7463271 Date:2022-09")
print(HSVToGreen(image))
