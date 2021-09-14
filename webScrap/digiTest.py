from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd 
#pd:
data = []
removal_words = ['sim','dual' , 'single' , 'mobile phone']
#
for i in range(3):
    with urlopen(f"https://www.digikala.com/search/category-mobile-phone/?has_selling_stock=1&pageno={i+1}") as response:
        html=response.read().decode("utf-8") #1- request to url
        soup=BeautifulSoup(html,"html.parser") #2 - parse html
        mobiles=soup.find_all("div",{"class":"c-product-box__content"})
        for mobile in mobiles:
            try:
                name=mobile.find("div",{"class":"c-product-box__title-en"}).text
            except AttributeError:
                name="not found"
         
            try:
                price=mobile.find("div",{"class":"c-price__value-wrapper"}).text.strip().split("\n")[0]
            except AttributeError:
                price="price not found!"
           # print(name,price)
            #CSV: Comma Seperated Values
            name=name.lower()
            sim = 2 if name.count('dual-sim') != 0 else 1
            for word in removal_words:
                name = name.replace(word,'')
            words = name.split()
            name=' '.join(words[1:])
            data.append([name,words[0],sim,int(price.replace(',',''))])

df = pd.DataFrame(data,columns=["name","brand","No.Sim","price"])
df.to_csv("mobiles.csv",index=False)