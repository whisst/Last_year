import requests
from bs4 import BeautifulSoup
import pandas

imgCaps = []
imgLinks = []

def crawl(image):
    imgCaps.append(image.get('alt'))
    imgLinks.append(image.get('src'))

for i in range(1,41):
    page = requests.get("https://tuoitre.vn/suc-khoe/phong-mach/trang-"+str(i)+".htm")
    soup = BeautifulSoup(page.content,"html.parser")

    if (i == 1):
        img = soup.find('img',{'class':'img324x202'})
        crawl(img)
        img = soup.find_all('img',{'class':'img124x77'})
        for j in img:
            crawl(j)
    img = soup.find_all('img',{'class':'img212x132'})
    for j in img:
        crawl(j)

data = {
    "Image Caption": imgCaps,
    "Image URL": imgLinks
}
df = pandas.DataFrame(data)
df.to_csv(r'..\UI_demo_II\Tuoitre.csv', index = False)