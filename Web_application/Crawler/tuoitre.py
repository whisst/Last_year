import requests
import bs4

titles = []
imgCaps = []
imgLinks = []


for i in range(1,10):
    page = requests.get("https://tuoitre.vn/suc-khoe/phong-mach/trang-"+str(i)+".htm")
    soup = bs4.BeautifulSoup(page.content,"html.parser")

    atribute = soup.find_all("li",{"class":"news-item"})
    for j in atribute:
        title = j.find('a')
        img = j.find('img')
        titles.append(title.get('title'))
        imgLinks.append(img.get('src'))
        imgCaps.append(img.get('alt'))

print('\n'.join(titles))
print('\n')
print('\n'.join(imgCaps))
print('\n')
print('\n'.join(imgLinks))