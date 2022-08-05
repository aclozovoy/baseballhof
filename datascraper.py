import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.baseball-reference.com/awards/hof_2022.shtml'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

print(soup)