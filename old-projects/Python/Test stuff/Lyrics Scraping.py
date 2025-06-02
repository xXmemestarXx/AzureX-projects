import requests
from bs4 import BeautifulSoup

# Self entered url
#url = input("type in a url for the lyrics")
# r = requests.get(url):

# Specific url
r = requests.get("https://genius.com/Xxxtentacion-palm-trees-lyrics")

soup = BeautifulSoup(r, "html.parser")

for p in soup.find_all('p'):
    print(p);



