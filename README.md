# Route-Mapper
![Made With Python](http://ForTheBadge.com/images/badges/made-with-python.svg) ![Made with love](http://ForTheBadge.com/images/badges/built-with-love.svg)

A program to visualize the traceroute process to a target domain.

<img src="https://user-images.githubusercontent.com/90629653/222931201-0988a135-0f88-4719-808d-c325cb42f39e.png" width=459 height=311>

## Usage

``` bash

python route_mapper.py

Enter target hostname (ex: google.com): 

```

## Requirements

``` bash

pandas==1.5.3
pyvis==0.3.2
requests==2.28.2
scapy==2.5.0

```

## Note

For easier readability, this program does not include private addresses. If you'd like to include them, just remove the condition ``` if country != None: ``` 
