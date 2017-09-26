import requests
from bs4 import BeautifulSoup
import re


class ArtistsScraper():
    def __init__(self):
        self.link = 'https://artmuseum.pl/pl/kolekcja/artysci'

    def get_artists_list(link):
        artists_list = requests.get(link, verify=False)
        text = artists_list.text
        soup = BeautifulSoup(text, 'html.parser')
        artists_ul = soup.find_all("ul", class_="artist-list")[0]
        hrefs_list = artists_ul.find_all("a")

        links_list = [link['href'] for link in hrefs_list]
        urls_list = ["http://artmuseum.pl" + element for element in links_list]
        return urls_list

    def get_ages(urls_list):
        ages = []

        for url in urls_list[:10]:
            artist = requests.get(url, verify=False)
            print("jestem na stronie" + url)
            text = artist.text
            soup = BeautifulSoup(text, 'html.parser')
            name = str(soup('h2')[0].string)
            birth_date = re.findall(r'\d{4}', name)
            if len(birth_date) == 1:
                age = 2017 - int(birth_date[0])
                ages.append(age)
        return ages

    def get_average(ages):
        average = 0
        for age in ages:
            average += age
        result = average / len(ages)
        return result



# content = requests.get('https://artmuseum.pl/pl/kolekcja/artysci/miron-bialoszewski', verify=False)
# text = content.text
# soup = BeautifulSoup(text, 'html.parser')
# name = str(soup('h2')[0].string)
# birth_date = re.findall(r'\d{4}', name)
# # print(birth_date)
