# import json
# f=open("cookies.json","r")
# cookies= f.read()
# cookiedata = json.loads(cookies)
# all_cookies= dict()
# def get_cookies():
#     for i in cookiedata:
#         name=i["name"]
#         value=i["value"]
#         # print(value)
#         # print(name)
#         all_cookies[name]=value
#         print(all_cookies)


# # a=[{2},{4},{6}]
# # print(a[0])

# get_cookies()

# import json

# all_cookies=dict()
# def get_cookies():
#     global all_cookies
#     f = open ("cookies.json","r")
#     cookie= f.read()
#     f.close()

#     cookiedata= json.loads(cookie)

#     # for i in cookiedata:
#     #     name= i["name"]
#     #     value=i["value"]
#     #     all_cookies[name]=value
#     #     print(all_cookies)

#     for i in range(0,len(cookiedata)):
#         name = cookiedata[i]['name']
#         value = cookiedata[i]['value']
#         all_cookies[name] = value
#         print(all_cookies)

# get_cookies()

# from bs4 import BeautifulSoup
# import requests
# headers= dict()
# headers["User-Agent"]="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"


# def scrape_restaurants():
#     r=requests.get("https://www.zomato.com/pune/sinhgad-road-restaurants",headers=headers)
#     print(r.text.string)

# scrape_restaurants()

import requests
from bs4 import BeautifulSoup

# The URL of the Zomato page you want to scrape
url = "https://www.zomato.com/pune/sinhgad-road-restaurants"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the <a> tags with class "result-title" and extract the restaurant names
restaurant_names = [a.text.strip() for a in soup.find("h4", class_="sc-1hp8d8a-0")]

# Print the restaurant names
print(restaurant_names)

