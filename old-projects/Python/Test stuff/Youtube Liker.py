import requests
from bs4 import BeautifulSoup


url = requests.get("http://aavtrain.com/index.asp")

soup = BeautifulSoup(url.text, 'html.parser')

for title in soup.findAll("form", {"name": "form1"}):
    #print(title)

payload = {"user_name": "hej", "password": "hej"}
r = requests.post(url, data=payload)
print(r.text)