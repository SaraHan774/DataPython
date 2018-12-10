import urllib.request
import bs4
import time

for i in range(0,10):
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
#    print(type(page)) #<class 'http.client.HTTPResponse'>
    
    soup = bs4.BeautifulSoup(page, "html.parser")
    tags = soup.find_all("strong")
#    print(tags)
    strtags = str(tags)
    getPrice = strtags.replace("[<strong>", "")
    getPrice = getPrice.replace("</strong>]", "")
    print("Current Price of the Coffee is : " + getPrice)
    time.sleep(1) 
    
    
#output example - international price of the coffe updated every sec. 
#Current Price of the Coffee is : $5.21
#Current Price of the Coffee is : $5.38
#Current Price of the Coffee is : $6.23
#Current Price of the Coffee is : $6.08
#Current Price of the Coffee is : $5.02
#Current Price of the Coffee is : $5.48
#Current Price of the Coffee is : $5.33
#Current Price of the Coffee is : $6.97
#Current Price of the Coffee is : $6.21
#Current Price of the Coffee is : $5.67
