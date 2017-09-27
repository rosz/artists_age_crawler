from scraper import ArtistsScraper


if __name__ == '__main__':
    current_scraper = ArtistsScraper()
    print(current_scraper.get_average())
