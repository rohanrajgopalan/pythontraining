import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.google.com/")
#print(req.text)
tree = BeautifulSoup(req.text, features="lxml")
print(tree.title)