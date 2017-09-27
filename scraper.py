import requests
from bs4 import BeautifulSoup
import re


class ArtistsScraper():
    main_link = 'http://artmuseum.pl'
    link = 'https://artmuseum.pl/pl/kolekcja/artysci'

    # get list of links to artists's individual pages
    def get_artists_list(self, link):
        artists_list = requests.get(self.link, verify=False)
        print(artists_list)
        text = artists_list.text
        soup = BeautifulSoup(text, 'html.parser')
        artists_ul = soup.find_all('ul', class_='artist-list')[0]
        hrefs_list = artists_ul.find_all('a')

        links_list = [link['href'] for link in hrefs_list]
        urls_list = [ArtistsScraper.main_link + element for element in links_list]
        print(urls_list)
        return urls_list

    # get list of artists' ages
    def get_ages(self, urls_list):
        urls_list = self.get_artists_list()
        ages = []

        for url in urls_list:
            artist = requests.get(url, verify=False)
            text = artist.text
            soup = BeautifulSoup(text, 'html.parser')
            name = str(soup('h2')[0].string)
            birth_date = re.findall(r'\d{4}', name)
            if len(birth_date) == 1:
                age = 2017 - int(birth_date[0])
                ages.append(age)
        return ages

    # get average of ages
    def get_average(self, ages):
        ages = self.get_ages()
        average = 0
        for age in ages:
            average += age
        result = average / len(ages)
        return result

if __name__ == '__main__':
    current_scraper = ArtistsScraper()
    print(current_scraper)


# print(ArtistsScraper.get_average(ArtistsScraper.get_ages(ArtistsScraper.get_artists_list("https://artmuseum.pl/pl/kolekcja/artysci"))))
