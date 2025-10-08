import requests
from bs4 import BeautifulSoup
url = "https://jalantikus.com/tags/tech-hack/"
req_get = requests.get (url)
soup = BeautifulSoup(
    req_get.content,
    "html.parser"
)

anchors = soup.find_all ('article')
for anchor in anchors:
    print (anchor.get ('id'))


















































































