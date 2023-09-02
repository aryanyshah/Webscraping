import requests
from bs4 import BeautifulSoup
import pandas as pd

data = {'title': [3, 2, 1, 0], 'price': ['a', 'b', 'c', 'd']}
pd.DataFrame.from_dict(data)

url = "http://books.toscrape.com/catalogue/category/books/history_32/index.html"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r=requests.get(url,headers=headers)

soup=BeautifulSoup(r.text,'html.parser')
""" print(soup.prettify()) """
titles = []
for book in soup.find_all("h3"):
    titles.append(book.a.attrs["title"])

# Print the titles
for title in titles:
    print(title)
   
prices=[]
for price in soup.find_all("p",class_="price_color"):
    prices.append(price.text.strip())

# Print the titles
for price in prices:
    print(price)
    

data = {'title': titles, 'price': prices}
df = pd.DataFrame.from_dict(data)

#print(df) 
df.to_excel("book_data.xlsx", index=False, engine='xlsxwriter')

 

