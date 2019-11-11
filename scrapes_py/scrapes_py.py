import requests
from bs4 import BeautifulSoup


# Requests allows us to grap the data. It like a web browser without the GUI
# Beautiful allows up to grab the HTML data and clean it up. Converts string(s)
# into an object that can be used and manipulated.

response = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(response.text, 'html.parser') # parse the returned HTML
