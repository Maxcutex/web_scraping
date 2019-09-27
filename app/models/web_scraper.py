import os
import string
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import urllib
import re
from urllib.parse import urlencode, urlparse, parse_qs


class WebScraper:
    def __init__(self, query):
        self.query = query
        self.ua = UserAgent()

    def search_online(self):
        keywords_list = self.query.split()
        invalid_chars = set(string.punctuation)
        valid_keywords = []
        for i, l in enumerate(keywords_list):
            if not any(char in invalid_chars for char in l):
                valid_keywords.append(l)
        query = urllib.parse.quote_plus(self.query)  # Format into URL encoding
        number_result = 5

        google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
        response = requests.get(google_url, {"User-Agent": self.ua.random})
        soup = BeautifulSoup(response.text, "html.parser")

        links = []
        browse_links = []
        titles = []
        descriptions = []

        result_div = soup.find_all('div', attrs={'class': 'ZINbbc'})

        for r in result_div:
            # Checks if each element is present, else, raise exception
            try:
                link = r.find('a', href=True)
                title = r.find('div', attrs={'class': 'vvjwJb'}).get_text()
                description = r.find('div', attrs={'class': 's3v9rd'}).get_text()

                # Check to make sure everything is present before appending
                if link != '' and title != '' and description != '':
                    links.append(link['href'])
                    titles.append(title)
                    descriptions.append(description)
            # Next loop if one element is not present
            except:
                continue

        to_remove = []
        clean_links = []
        for i, l in enumerate(links):
            clean = re.search('\/url\?q\=(.*)\&sa', l)

            # Anything that doesn't fit the above pattern will be removed
            if clean is None:
                to_remove.append(i)
                continue
            clean_links.append(clean.group(1))
        print("print_clean_links")
        print(clean_links)
        # Remove the corresponding titles & descriptions
        for x in to_remove:
            del links[x]
            del titles[x]
            del descriptions[x]
        for link in links:
            if link.startswith("/url?"):
                actual_url = parse_qs(urlparse(link).query)['q']
                browse_links.append(actual_url[0])

        return browse_links, valid_keywords


    def find_relevant_info(self, url, valid_keywords):

        response = requests.get(url, {"User-Agent": self.ua.random})
        soup = BeautifulSoup(response.text, "html.parser")
        result_div = soup.find_all(string=re.compile("keystone"))
        sub_list = []
        for valid in valid_keywords:
            set = soup.find_all(text=re.compile(valid))
            sub_list.append(set)
        return sub_list

    def clean_up_data(self, array_data):
        pass