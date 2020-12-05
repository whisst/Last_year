import requests
from bs4 import BeautifulSoup
import pandas

imglinks = []
imgcaps = []

for i in range(1,21):
    page = requests.get("https://dantri.com.vn/suc-khoe/ung-thu/trang-"+str(i)+".htm")
    soup = BeautifulSoup(page.content,"html.parser")

    if (i==1):
        img = soup.find('div',{'class':'col--highlight-news'}).find_all('img')
        parents = soup.find('div',{'class':'col--primary'}).find_all('ul',{'class':'dt-list--lg'})
        for j in parents:
            child = j.find_all('img')
            for k in child:
                img.append(k)
        for j in img:
            imgcaps.append(j.get('alt'))
            imglinks.append(j.get('src'))
    else:
        img = soup.find('ul',{'class':'dt-list--lg'}).find_all('img')
        for j in img:
            imgcaps.append(j.get('alt'))
            imglinks.append(j.get('src'))

data = {
    "Image Caption": imgcaps,
    "Image URL": imglinks
}
df = pandas.DataFrame(data)
df.to_csv(r'..\UI_demo_II\Dantri.csv', index = False)
