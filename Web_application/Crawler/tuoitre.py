
import requests
import bs4

titles = []
imgCaps = []
imgLinks = []

page = requests.get("https://tuoitre.vn/suc-khoe/phong-mach/trang-"+str(i)+".htm")
soup = bs4.BeautifulSoup(page.content,"html.parser")

atribute = soup.find_all("li",{"class":"news-item"})
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

