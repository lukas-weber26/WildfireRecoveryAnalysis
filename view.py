from streetview import search_panoramas
from streetview import get_streetview

panos = search_panoramas(lat=38.47496561, lon=-122.7486986)

first = panos[0]

for a in panos:
    if a.date != None:
        print (a.date)
        print (a.pano_id)
        image = get_streetview(pano_id=a.pano_id,api_key="AIzaSyCKAa7TIgjJzVKdQlD_fK2v68WrHVx7R3I")
        name = "Cali" + a.date+ ".jpg" 
        image.save(name, "jpeg")

