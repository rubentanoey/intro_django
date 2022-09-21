from django.test import TestCase, Client
from django.urls import reverse

class MyWatchListExistenceTest(TestCase):

    def setUpClient(self):
        self.client = Client()

    def test_mywatchlist_html_exists(self):
        url = self.client.get('/mywatchlist/')
        self.assertEqual(url.status_code, 200)
    
    def test_mywatchlist_xml_exists(self):
        url = self.client.get('/mywatchlist/xml/')
        self.assertEqual(url.status_code, 200)

    def test_mywatchlist_json_exists(self):
        url = self.client.get('/mywatchlist/json/')
        self.assertEqual(url.status_code, 200)

    def test_mywatchlist_html_responsiveness(self):
        url = self.client.get(reverse('mywatchlist:show_watchlist'))
        self.assertEqual(url.status_code, 200)

    def test_mywatchlist_xml_responsiveness(self):
        url = self.client.get(reverse('mywatchlist:show_xml'))
        self.assertEqual(url.status_code, 200)

    def test_mywatchlist_json_responsiveness(self):
        url = self.client.get(reverse('mywatchlist:show_json'))
        self.assertEqual(url.status_code, 200)