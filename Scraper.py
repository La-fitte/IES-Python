import requests
from bs4 import BeautifulSoup
import pandas as pd


class DiscworldChar:
    """
    Class containing methods for parsing Major Discworld characters that are related to Ankh-Morpork 
    and The Watch from self.soup attribute.
    """

    def __init__(self, link, title):
        self.link = link
        self.title = title
        r = requests.get(link)
        r.encoding = 'UTF-8'
        self.soup = BeautifulSoup(r.text, 'html.parser')

        self.characteristics = self.parseCharacteristics()

    def parseCharacteristics(self):
        """
        Parses dictionary of values from the table into a pandas Series.
        :return: pandas series with Major Discworld characters
        """
        table = self.getLisRows()
        return pd.Series(table)

    def getARows(self):
        """
        Finds table on the page of the selected book and parses its rows.
        :return: dict of 'row_name': 'row_value'
        """
        table = self.soup.find('tbody')
        rows = table.find_all('a', title='Book:')
        rows_with_values = {**{'Book': self.title},
                            **{row.text.strip(): row.next_sibling.text.strip() for row in rows}}
        return rows_with_values

