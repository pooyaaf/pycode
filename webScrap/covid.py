from bs4.element import SoupStrainer
import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = "https://www.worldometers.info/coronavirus/country/iran/"

response = requests.get(url)

Source = response.content

soup = BeautifulSoup(Source,"html.parser")
#cases:
cases = soup.find_all("div",class_="maincounter-number")

#list
data=[]
#find spans:
for i in cases:
     span=i.find("span")
     data.append(span.string)

pf=pd.DataFrame(

                    {
                         "Corona Data":data
                    }

)

pf.index=["Cases","Death","ReCovered"]
pf.to_csv("Covid-data.csv")