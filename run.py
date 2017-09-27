from scraper import ArtistsScraper


if __name__ == '__main__':
    current_scraper = ArtistsScraper()
    a = current_scraper.get_artists_list()
    b = current_scraper.get_ages(a)
    c = current_scraper.get_average(b)
    print(c)
