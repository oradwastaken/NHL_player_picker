from bs4 import BeautifulSoup
from urllib.request import urlopen
from hockey_classes import Player, SkaterStats
from datetime import datetime

# Skaters
url_skaters = 'https://www.hockey-reference.com/leagues/NHL_2021_skaters.html'
url_goalies = 'https://www.hockey-reference.com/leagues/NHL_2021_goalies.html'



