import requests
from bs4 import BeautifulSoup
url = "https://tanks-encyclopedia.com/"
req_get = requests.get (url)
soup = BeautifulSoup(
    req_get.content,
    "html.parser"
)

anchors = soup.find_all ('div')
for anchor in anchors:
    print (anchor.get ('class'))

# with open ("file.html", "w") as f:
#     f.write (req_get.text)




































































