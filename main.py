import requests
from bs4 import BeautifulSoup


url = "https://pokeapi.co/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
for link in soup.findAll('a'):
    x =  link.get('href')
    if 'http' in x:
        try:
            response = requests.get(x)
            if response.status_code == 200:
                print(response.json())
        except:
            print("XXXXXXXX")

