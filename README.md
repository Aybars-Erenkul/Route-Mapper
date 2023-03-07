# Route-Mapper
![Made With Python](http://ForTheBadge.com/images/badges/made-with-python.svg) ![Made with love](http://ForTheBadge.com/images/badges/built-with-love.svg)

Route Mapper visualizes the traceroute process to a target domain.
Here is the basic idea divided by steps:
```
1) Performs a traceroute on the target domain using scapy
2) Each IP's Country, Region and Organization data is pulled using IP-API
3) Stores the data in a .csv file
4) Reads the .csv file using pandas module
5) Creates a network node for each line in file
6) Saves the created network parameters in a .html file using PyVis
```

### Optionally, Route Mapper can also scrape the website for any additional IP addresses that the website is communicating with for various purposes (such as fonts, js, SEO).

This is accomplished by taking these steps:

```
1) Uses the requests module to get the website's source code.
2) The source-code of the page is scraped via bs4 to check any external connections the website is making.
3) Passes the found URIs to a DNS Query function to get the corresponding IP addresses.
4) Stores the URI and the IP datas to a seperate .csv file
4) Reads from the .csv file, then create a node for each IP address.
5) Adds and connects new nodes for visualization.
```


<img src="https://user-images.githubusercontent.com/90629653/223468455-ae0f23ff-e86c-46fe-8201-f968436cbb0c.png" width=733 height=456>

## Usage

``` bash

python route_mapper.py

Enter target hostname (ex: google.com): 

```

## Requirements

``` bash

beautifulsoup4==4.11.2
pandas==1.5.3
pyvis==0.3.2
requests==2.28.2
scapy==2.5.0

```

## Note

For easier readability, this program does not include private addresses. If you'd like to include them, just remove the condition ``` if country != None: ``` 
