
from flask import Flask , jsonify
app = Flask(__name__)
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
logo =[]
x = scarping()
for i in x:
    logo.append(i['url_logo'])
print(logo)
@app.route('/companies', methods=['GET'])
def home(): 
    arr = logo
    return jsonify(arr)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)