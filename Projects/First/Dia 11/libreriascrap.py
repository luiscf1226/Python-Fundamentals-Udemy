import bs4
import requests

url_base='http://books.toscrape.com/catalogue'

resultado=requests.get(url_base.format('1'))
sopa=bs4.BeautifulSoup(resultado.text,'lmxl')

print(sopa.select('.product-pod'))