from app.controllers.base_controller import BaseController
from app.models.web_scraper import WebScraper


class HomeController(BaseController):
    def __init__(self, request):
        BaseController.__init__(self, request)
        self.search_string = None

    def home_page(self):
        return self.handle_response('OK', payload={'App': 'Welcome Message'})

    def search_words(self):

        self.search_string = self.request_params('search_string')
        web_scraper = WebScraper(self.search_string)
        browse_links, valid_keywords = web_scraper.search_online()

        container={}

        for result_link in browse_links:
            result_set = web_scraper.find_relevant_info(result_link,valid_keywords)

            # pending cleanup of data as data returned will be bulky and not relevant yet
            container[result_link] = result_set

        return self.handle_response('OK', payload={'searchResponse': container.serialize()})
