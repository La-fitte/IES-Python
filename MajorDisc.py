import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
from Scraper import DiscworldChar


class WikiDownload:
    
    def __init__(self):
        """
        Initialize variables
        """
        self.links = []
        self.books = []
        self.dfs = None
        
    def getAllLinks(self, soup):
        """
        get links with such characteristics
        """
        soup = getSoup(link)
        lis = soup.find('span',{'id':'Unseen_University_and_the_Wizards'}).parent.previous.previous.parent.parent.parent.find_all('li')
        links = ['http://wiki.lspace.org' + lis.find('a')['href'] for li in lis]
        return links
    
    def getBooks(self, link):
        """
        Downloads all books links in the specified webpage and saves it to self.links
        """
        r = requests.get(link)
        r.encoding = 'UTF-8'
        soup = BeautifulSoup(r.text, 'html.parser')

        self.links = self.getAllLinks(soup)

    def downloadBooks(self:
        """
        Download books and stored it
        """
        for book_info in self.links:
            book = WikiBook(book_info['link'], book_info['title'])
            self.books.append(book)

    def saveDfs(self):
        dfs = {
               'books': pd.DataFrame([x.characteristics for x in self.books])
        }
        self.dfs = dfs


if __name__ == '__main__':
    downloader = WikiDownload()
    downloader.get_books_links('http://wiki.lspace.org/mediawiki/List_of_Pratchett_characters')
    downloader.download_books()
    downloader.save_dfs()
    print(MajorDisc.dfs['books'].info())