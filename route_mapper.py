from scapy.all import *
from scapy.layers.inet import traceroute
import pandas as pd
import csv
from pyvis.network import Network
import requests
import ip_scraper


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location(ip):
    ip_address = ip
    #response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    response = requests.get(f'http://ip-api.com/json/{ip_address}').json()
    location_data = (response.get("country"),response.get("regionName"), response.get("org"))
    
    return location_data



target = input("Enter target hostname (ex: google.com): ")
ask_extras = input("Do you want to include IP's that the website is communicating as well ? (y/n): ")
if ask_extras == 'y':
    extras = True
else:
    extras = False
hostname = [target]

result, unans = traceroute(hostname, maxttl=30)


with open("traceroute.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IP", "COUNTRY", "CITY", "ORG"])
    for snd, rcv in result:
        print(rcv.src)
        country, city, org = get_location(rcv.src)
        print(f"Now Printing city for {country}")
        if country != None:
            print(country)
            writer.writerow([rcv.src, country, str(city).encode("utf-8").decode("windows-1252"), org])

got_data = pd.read_csv("traceroute.csv")

net = Network()
i = 1
nodeLength = 0
for i in range(len(got_data)):
    nodeLength = nodeLength + 1
    if type(got_data["COUNTRY"][i]) == float:
        net.add_node(got_data["IP"][i] + "\n" + "Country Not Found")
    else:
        net.add_node(got_data["IP"][i] + "\n" + got_data["COUNTRY"][i] + "\n" + got_data["CITY"][i] ,title=got_data["ORG"][i])
        #print(type(got_data["COUNTRY"][i]))
    if i != 0:
        if type(got_data["COUNTRY"][i]) != float:
            if type(got_data["COUNTRY"][i-1]) != float:
                net.add_edge(got_data["IP"][i] + "\n" + got_data["COUNTRY"][i] + "\n" + got_data["CITY"][i], got_data["IP"][i-1] + "\n" + got_data["COUNTRY"][i-1] + "\n" + got_data["CITY"][i-1])
            else:
                net.add_edge(got_data["IP"][i] + "\n" + got_data["COUNTRY"][i] + "\n" + got_data["CITY"][i], got_data["IP"][i-1] + "\n" + "Country Not Found")
        else:
            if type(got_data["COUNTRY"][i-1]) != float:
                net.add_edge(got_data["IP"][i] + "\n" + "Country Not Found", got_data["IP"][i-1] + "\n" + got_data["COUNTRY"][i-1] + "\n" + got_data["CITY"][i-1])
            else:
                net.add_edge(got_data["IP"][i] + "\n" + "Country Not Found", got_data["IP"][i-1] + "\n" + "Country Not Found")
            pass

if extras == True:
    ip_scraper.ip_gatherer(target)
    got_extras = pd.read_csv("extras.csv")
    for i in range(len(got_extras)):
        net.add_node(got_extras["IP"][i],title=got_extras["URI"][i] ,color="green")
        net.add_edge(got_data["IP"][nodeLength-1] + "\n" + got_data["COUNTRY"][nodeLength-1] + "\n" + got_data["CITY"][nodeLength-1], got_extras["IP"][i])
else:
    pass
net.show("route.html", notebook=False)
