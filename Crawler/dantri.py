import requests
from bs4 import BeautifulSoup

titles = []
contents = []
imglinks = []
imgcaps = []

for i in range(1,40):
    page = requests.get("https://dantri.com.vn/suc-khoe/ung-thu/trang-"+str(i)+".htm")

    soup = BeautifulSoup(page.content,"html.parser")
    
    title_temp = soup.find_all("h3",{"class":"news-item__title"})
    content_temp = soup.find_all("a",{"class":"news-item__sapo"})
    img_temp = soup.find_all("img",{"class":"no-img"})

    for j in title_temp:
        titles.append(j.getText().replace("\n","").strip())
    for j in content_temp:
        contents.append(j.getText().replace("\n","").strip())
    for j in img_temp:
        imglinks.append(j.get('src')) 
        imgcaps.append(j.get('alt'))
        
print("\n".join(titles))

        

