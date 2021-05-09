import requests
import bs4
from googlesearch import search


class DocumentCollection:
    def __init__(self, query):
        self.query = query

    def webpage(self):
        url = []
        count = 0
        for i in search(query=self.query, tld='co.id', lang='id', num=10, stop=10, pause=2.0):
            count += 1
            url.append(i)
        text = []
        for i in url:
            page = requests.get(i)
            soup = bs4.BeautifulSoup(page.content, 'html.parser')
            html_tag = soup.find_all("p")
            for string in html_tag:
                text.append(string.text)
        str1 = ""
        for ele in text:
            str1 += ele
        return str1

    def searchpage(self):
        url = 'https://google.com/search?q=' + self.query
        request_result = requests.get(url)
        soup = bs4.BeautifulSoup(request_result.text, "html.parser")
        temp = soup.find("div", class_='BNeawe s3v9rd AP7Wnd').text     # BNeawe s3v9rd AP7Wnd
        return temp

