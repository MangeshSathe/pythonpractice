"""API for python"""

import requests
from lxml import etree

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&'

parameters = {
    "starttime" : "2022-01-01",
    "endtime" : "2022-01-31",
    "minlatitude" : "8.0",
    "maxlatitude" : "37.0",
    "minlongitude" : "68.0",
    "maxlongitude" : "97.0"
}
list_of_earthquakes = []
data_request = requests.get(url,parameters)
raw_data = data_request.json()

for key,value in raw_data.items():

    if key == "metadata":       
        api_exec_time = value['generated']
    
    if key == "features":
       for ldata in value:
           magnitude = ldata['properties']['mag']
           place = ldata['properties']['place']
           time = ldata['properties']['time']
           detail = ldata['properties']['detail']
           title = ldata['properties']['title']

           coordinates_lat = ldata['geometry']['coordinates'][0]
           coordinates_lon = ldata['geometry']['coordinates'][1]
           coordinates_rad = ldata['geometry']['coordinates'][2]
      
           id = ldata['id']

           list_of_earthquakes.append([api_exec_time, magnitude, place, time, detail, title, coordinates_lat, coordinates_lon, coordinates_rad, id])


root = etree.Element("earthquake")

for  _,magnitude, place, time, detail, title, coordinates_lat, coordinates_lon, coordinates_rad, id in list_of_earthquakes:
    fulldata = etree.SubElement(root, "earthquake_logs", identifier=id)
    etree.SubElement(fulldata,"magnitude").text = str(magnitude)
    etree.SubElement(fulldata,"place").text = str(place)
    etree.SubElement(fulldata,"time").text = str(time)
    etree.SubElement(fulldata,"title").text = str(title)
    etree.SubElement(fulldata, "url").text =str(detail)
    etree.SubElement(fulldata,"coordinates_lat").text = str(coordinates_lat)
    etree.SubElement(fulldata,"coordinates_lon").text = str(coordinates_lon)
    etree.SubElement(fulldata,"coordinates_rad").text = str(coordinates_rad)

xml_tree = etree.ElementTree(root)
xml_tree.write("eqt.xml",pretty_print = True, xml_declaration = True, encoding = "UTF-8")

