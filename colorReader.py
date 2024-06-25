import functools
import numpy as np
from PIL import Image 
import os
from functools import partial
import matplotlib.pyplot as plt


def getPercentGreen(name):
    image = Image.open(name)
    #print(image.format)
    #print(image.size)
    #print(image.mode)

    imgArray= np.asarray(image)

    r = sum(sum(imgArray[:,:,0]))
    g = sum(sum(imgArray[:,:,1]))
    b = sum(sum(imgArray[:,:,2]))
    percentGreen = 100*g/(r+g+b)
    #print("Percent green: ", percentGreen)
    return percentGreen 

def nameContainsIndex(index,name):
    if ('Index:' + str(index)) in name:
        return True 
    else: 
        return False

#def getFilesFromIndex(index,fileList):

#getPercentGreen('Lat:38.49531984 Long:-122.6971486/Index:1422 Lat:38.49531984 Long:-122.6971486 Date:2011-06')
files = os.listdir('./general/')

d = {"2008":0,"2009":0,"2010":0,"2011":0,"2012":0,"2013":0,"2014":0,"2015":0,"2016":0,"2017":0,"2017":0,"2018":0,"2019":0,"2020":0,"2021":0,"2022":0,"2023":0,"2024":0}
c = {"2008":0,"2009":0,"2010":0,"2011":0,"2012":0,"2013":0,"2014":0,"2015":0,"2016":0,"2017":0,"2017":0,"2018":0,"2019":0,"2020":0,"2021":0,"2022":0,"2023":0,"2024":0}

for i in range(0,1000):
    #print("Looking for: ", i)
    g = partial(nameContainsIndex, i)
    validFiles = filter(g, files)
    
    for s in validFiles:
        date = s[-7:-3]
        d[date] += getPercentGreen('./general/'+s)
        c[date] += 1
        #print(s)


means = {"2008":0.0,"2009":0.0,"2010":0.0,"2011":0.0,"2012":0.0,"2013":0.0,"2014":0.0,"2015":0.0,"2016":0.0,"2017":0.0,"2017":0.0,"2018":0.0,"2019":0.0,"2020":0.0,"2021":0.0,"2022":0.0,"2023":0.0,"2024":0.0}

for k in means.keys():
    if (c[k] != 0):
        means[k] = (float(d[k])/float(c[k]))

values = means.values()
keys = means.keys()
print(means)


plt.plot(keys,values)
plt.title('Green Channel Relative Strength')
plt.savefig('out.png')

#t isfor file in files:
#    print(getPercentGreen('./general/'+file))

#print(files)

