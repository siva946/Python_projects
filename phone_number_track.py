#pip install phonenumbers

import phonenumbers
from phonenumbers import geocoder,parse

import os

#pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()

#geocoding API key from opencage website after login
key="enter API key"

number=os.getenv("number")
phone_number=parse(number)
number_location=geocoder.description_for_number(phone_number,"en")
print(number_location)

from phonenumbers import carrier
service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

#pip install opencage

from opencage.geocoder import OpenCageGeocode

latlong=OpenCageGeocode(key)
results=latlong.geocode(str(number_location))

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

#pip install folium

import folium

Map=folium.Map(number_location=[lat,lng],zoom_start=8)
folium.Marker([lat,lng],popup=number_location).add_to(Map)
Map.save('location.html')
#save python file and run....after that run location.html file