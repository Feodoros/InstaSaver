from bs4 import BeautifulSoup
import httplib2
import urllib.request
import urllib.parse


# Get html
def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


# Save image from link
def saver(links):
    i = 0
    for link in links:
        i += 1
        h = httplib2.Http('.cache')
        response, content = h.request(link)
        out = open('img' + str(i) + '.jpg', 'wb')
        out.write(content)
        out.close()


# Get links of Instagramm photo
def page_parser(list_inks):
    insta_links = []
    for url in list_inks:
        soup = BeautifulSoup(get_html(url))
        for tag in soup.find_all('img'):
            insta_link = tag.get('src')
            if (insta_link is not None) and ("https" in insta_link):
                insta_links.append(insta_link)
    return insta_links


def main():

    tags = {"лес", "подъезд", "дом", "дача", "природа", "фото", "еда", "расскраска", "район",
            "двор", "парковка", "конспект", "школа", "окраина", "я", "друзья", "дерево", "лестница",
            "окно", "площадка"}

    list_links = []
    for tag in tags:
        list_links.append("https://stapico.ru/tag/" + urllib.parse.quote(tag))

    saver(page_parser(list_links))
    print("IS_DONE")


if __name__ == "__main__":
    main()