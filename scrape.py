import requests
from bs4 import BeautifulSoup
import json
import sys
import time
import ast
import threading

all_cookies=dict()
# global all_cookies
headers= dict()
headers["User-Agent"]="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"

def get_cookies():
    # global all_cookies
    f = open ("cookies.json","r")
    cookie= f.read()
    f.close()

    cookiedata= json.loads(cookie)

    # for i in cookiedata:
    #     name= i["name"]
    #     value=i["value"]
    #     all_cookies[name]=value
    #     print(all_cookies)

    for i in range(0,len(cookiedata)):
        name = cookiedata[i]['name']
        value = cookiedata[i]['value']
        all_cookies[name] = value
        # print(all_cookies)


def connect_zomato():
    r=requests.get('https://zomato.com/',cookies=all_cookies,headers = headers)
    if("Log out" in r.text):
        print("Logged in")
    else:
        print("Invalid Cookies")
    # print(r.text)

 
def scrape_restaurants():
    r=requests.get("https://www.zomato.com/pune/",headers=headers)
    soup=BeautifulSoup(r.text,"html.parser")
    

    divs = soup.find_all('div',{'class':'sc-bYzVrU'})
    print(divs)
    
    # for div in divs:
    #     res_name= div.findChildren("h4",{"class":"sc-1hp8d8a-0"},recursive=False)
    #     print(res_name)

    
    # res=soup.find("div").get_text()
    # print(res)


    
    # divs.find_all("div",class_="sc-eylKsO fwzZbj")
    # print(divs)
    # for div in divs:
    #     res_name=div.find('div',class_='sc-bQmweE')
    #     print(res_name)

# # get_cookies()





connect_zomato()
scrape_restaurants()





# import json
# import requests
# import threading
# import sys
# import time
# import ast
# from bs4 import BeautifulSoup



# res_per_page = 30
# all_cookies = dict()
# headers = dict()
# headers['User-Agent']= 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:71.0) Gecko/20100101 Firefox/71.0'
# zomato_url = "https://zomato.com"
# zomato = list()
# sorted_zomato = list()
# subzone_url = ""
# stop_scraping = False
# categories = list()

# proxies = {"http" : "127.0.0.1:8080","https" : "127.0.0.1:8080"}


# def get_cookies_zomato(cfile):
#     global all_cookies
#     f = open(cfile,"r")
#     cookies = f.read()
#     f.close()
#     cookies = json.loads(cookies)

#     #get name and value of cookie
#     for i in range(0,len(cookies)):
#         name = cookies[i]['name']
#         value = cookies[i]['value']
#         all_cookies[name] = value
        

# def connect_zomato(city):
#     global subzone_url
#     global all_cookies

#     r = requests.get(zomato_url+"/%s/order"%city,headers=headers,cookies=all_cookies)
#     print(r.status_code)

#     f = open("output.html","wb")
#     f.write(r.text.encode('utf-8'))
#     f.close()

#     #Check if cookies are valid
#     if "Log out" in r.text:
#         print("Logged in!")
#     else:
#         print("Login Fail - Please change cookies!")
#         sys.exit(0)    

#     #get URL for other pages
#     soup = BeautifulSoup(r.text,"html.parser")
#     subzone_url = soup.find_all("a",{'class':'paginator_item'})[0].get("href")
    
#     return subzone_url



# def calculate_score(rating,offer_value):
#     rating_score = (rating/0.1) * 1
#     offer_score = offer_value * 2
    
#     return (rating_score + offer_score)



# def scrape_zomato(pg_no):
#     global stop_scraping
#     global categories
    
#     #Check scraping status
#     if(stop_scraping):
#         return
    
#     r = requests.get(zomato_url+subzone_url[0:len(subzone_url)-1]+str(pg_no),headers=headers,cookies=all_cookies)
#     soup = BeautifulSoup(r.text,"html.parser")
    
#     #First get number of restaurants on the page
#     restaurants = soup.find_all("div",{'class':'search-o2-card'})
    
    
#     print("No. of Restaurants on page %d - %d"%(pg_no,len(restaurants)))
    

#     #If no restaurants on a page, it means we've reached end.
#     if(len(restaurants)<res_per_page):
#         stop_scraping = True
    
#     for restaurant in restaurants:
#         #First check if restaurant is offline
#         if(restaurant.findChildren("div",{'class':'order_search_button'})):
#             continue
        
#         #Get the name of the restaurant
#         res_name = restaurant.findChildren("a",{'class':'result-order-flow-title'})[0].text.strip()
#         #print(res_name)
        
        
#         #Get restaurant ID
#         res_id = restaurant.get("data-res_id")

#         #Get category
#         res_category=restaurant.findChildren("div",{'class':'grey-text'})[0].text.strip()
        
#         #Get the rating of the restaurant
#         res_rating = restaurant.findChildren("div",{'class':'rating-popup','data-res-id':res_id})[0].text.strip()

#         try:
#             res_rating = float(res_rating)
#         except ValueError:
#             res_rating = 0.0
        
        
#         #Get the offer of restaurant
#         res_offer = "No offer"
#         res_offer_value = 0
#         if(restaurant.findChildren("span",{'class':'offer-text'})):
#             res_offer = restaurant.findChildren("span",{'class':'offer-text'})[0].text.strip()
#             #print(res_offer)

#             if u"\u0024" in res_offer: #rupee symbol
#                 res_offer_value = res_offer[res_offer.index(u"\u0024")+1:res_offer.index(" ")]
#             elif "%" in res_offer:
#                 res_offer_value = int((res_offer[0:res_offer.index('%')]).strip())
        
        
#         res_info = dict()
        
#         res_score = calculate_score(rating=res_rating,offer_value = res_offer_value)
        
#         res_info['res_id'] = res_id
#         res_info['res_rating'] = res_rating
#         res_info['res_category'] = res_category
#         res_info['res_name'] = res_name
#         res_info['res_offer'] = res_offer
#         res_info['res_score'] = res_score
        

#         #If specific categories are submitted as input
#         if((len(categories)>0)):
#             cats = res_category.strip().split(',')
#             for cat in cats:
#                 if(cat.lower() in categories):
#                     zomato.append(res_info)
#                     break

#         else:
#             zomato.append(res_info)


# def go_scraping(city,cfile,cats):
#     global categories
#     categories = list(cats)
#     get_cookies_zomato(cfile)
#     subzone_url = connect_zomato(city) #Get subzone_id so that we can frame other pages links
    
#     #Now start scraping. Each page, one thread
#     k=1
#     threads = list()
#     for i in range(0,2):
#         t = threading.Thread(target=scrape_zomato,args=(k,))
#         t.daemon= True
#         k = k + 1
#         threads.append(t)
#         if(stop_scraping):
#             print("Stopping Scraping")
#             break
#         t.start()
        
    
#     for i in threads:
#         i.join()

        
#     #contains only active/online restaurants  
#     sorted_zomato = sorted(zomato,key = lambda i: i['res_score'],reverse=True)



#     return sorted_zomato