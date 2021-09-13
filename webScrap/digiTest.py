from urllib.request import urlopen
from bs4 import BeautifulSoup
for i in range(30):
    with urlopen(f"https://www.digikala.com/search/category-mobile-phone/?has_selling_stock=1&pageno={i+1}") as response:
        html=response.read().decode("utf-8") #1- request
        soup=BeautifulSoup(html,"html.parser") #2 - parse
        mobiles=soup.find_all("div",{"class":"c-product-box__content"})
        for mobile in mobiles:
            try:
                name=mobile.find("div",{"class":"c-product-box__title-en"}).text
            except AttributeError:
                name="not found"
            print(f"{i+1} - {name}",end=" - ")
            try:
                price=mobile.find("div",{"class":"c-price__value-wrapper"}).text.strip().split("\n")[0]
            except AttributeError:
                price="price not found!"
            print(price)

