import requests
from bs4 import BeautifulSoup

def scarping():
    url = r'https://theinternship.io/'
    data = requests.get(url)

    soup = BeautifulSoup(data.text,'html.parser')

    partner = soup.find_all('div',class_='partner')
    partners=[]
    for i in partner:
    
        p={}
        p['content']=i.span.text
        p['url_logo']= i.img['src']
        partners.append(p)

    sorted(partners, key = lambda i: i['content'],reverse=True)

    return partners
    
        
data = scarping()
for i in data:
    print(i['url_logo'])