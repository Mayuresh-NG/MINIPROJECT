import phonenumbers

import folium

from myNumber import number

from phonenumbers import geocoder

Key = '047ba78d55814bb38c55b934c586df6a'


sanNumber = phonenumbers.parse(number)

yourlocation = geocoder.description_for_number(sanNumber,"en")
print(yourlocation)


##get service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(yourlocation)

results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat,lng], zoom_start= 9)

folium.Marker([lat, lng],popup= yourlocation).add_to((myMap))

## save map in html file

myMap.save("myLocation.html")