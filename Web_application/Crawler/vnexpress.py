import requests
from bs4 import BeautifulSoup
import pandas

imglinks = []
imgcaps = []

def crawl(x):
    img = soup.find("a",{"data-medium":"Item-"+str(x)}).find('img')
    imglinks.append(img.get('src'))
    imgcaps.append(img.get('alt'))

for i in range(1,26):
    page = requests.get("https://vnexpress.net/suc-khoe/ung-thu-p"+str(i))
    soup = BeautifulSoup(page.content,"html.parser")
    
    if (i==1):
        for j in range(1,25):
            crawl(j)
    else:
        for j in range(1,21):
            crawl(20*(i-1)+j+4)

data = {
    "Image Caption": imgcaps,
    "Image URL": imglinks
}
df = pandas.DataFrame(data)
df.to_csv(r'..\UI_demo_II\Vnexpress.csv', index = False)
