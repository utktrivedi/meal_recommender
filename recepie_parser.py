from lib.repo import repo
from bs4 import BeautifulSoup
import requests
from pathlib import Path
import json



r =requests.get(url)
soup=BeautifulSoup(r.text,"lxml")
json_data = soup.find("script",type="application/ld+json")

print(json.loads(json_data.string)[1]["recipeIngredient"])