import requests
from bs4 import BeautifulSoup


# Requests allows us to grap the data. It like a web browser without the GUI
# Beautiful allows up to grab the HTML data and clean it up. Converts string(s)
# into an object that can be used and manipulated.

url = 'https://news.ycombinator.com/news' # hn or Hacker News site
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser') # parse the returned HTML
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText() # Gets text inside of HTML/XML tags
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', '')) # convert to int; replace string with empty str
            print(points)
            hn.append({'title': title, 'link': href, 'votes': points})
    return hn

print(create_custom_hn(links, subtext))