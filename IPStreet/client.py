import json

import requests
from IPStreet.error import APIConnectionError, SendError

from IPStreet import query


class Client:
    """Basic IP Street API Client Object"""

    def __init__(self, apikey, api_version):

        self.debug = True

        # credentials
        self.apikey = apikey
        self.headers = {'x-api-key': self.apikey}

        # create most up-to-date endpoints
        self.host = 'https://api.ipstreet.com'
        self.api_version = "/v" + str(api_version)

        # endpoints
        self.endpoint_full_text = self.host + self.api_version + '/full_text'
        self.endpoint_claim_only = self.host + self.api_version + '/claim_only'

        self.endpoint_data_feed = self.host + self.api_version + '/data'
        self.endpoint_patent_data = self.endpoint_data_feed + '/patent'

        self.endpoint_claim_parser = self.host + self.api_version + '/claim_parser'
        self.endpoint_ngram = self.endpoint_claim_parser + '/ngram'
        self.endpoint_keyphrase = self.endpoint_claim_parser + '/keyphrase'
        self.endpoint_claim_element = self.endpoint_claim_parser + '/claim_element'

    def check_service_status(self):
        """"Checks the status of all IP Street Endpoints"""
        pass

    def send(self, query_object):

        # if (isinstance(query_object, query.Query) or query_object is None):
        #     raise SendError("The object you are attempting to send is not a valid query object")

        if isinstance(query_object, query.FullTextSearch):
            self.endpoint = self.endpoint_full_text
            self.payload = {"raw_text": query_object.raw_text, "q": query_object.q}
            pages = self.get_all_pages()
            assets = self.pages_to_assets(pages)
            return assets

        if isinstance(query_object, query.ClaimOnlySearch):
            self.endpoint = self.endpoint_claim_only
            self.payload = {"raw_text": query_object.raw_text, "q": query_object.q}
            pages = self.get_all_pages()
            assets = self.pages_to_assets(pages)
            return assets

        if isinstance(query_object, query.PatentData):
            self.endpoint = self.endpoint_patent_data
            self.payload = {'q': query_object.q}
            pages = self.get_all_pages()
            assets = self.pages_to_assets(pages)
            return assets

        if isinstance(query_object, query.NgramQuery):
            self.endpoint = self.endpoint_ngram
            self.payload = {'q': query_object.q}
            results = self.get_default_page()
            return results

        if isinstance(query_object, query.KeyPhraseQuery):
            self.endpoint = self.endpoint_keyphrase
            self.payload = {'q': query_object.q}
            results = self.get_default_page()
            return results

        if isinstance(query_object, query.ClaimElementsQuery):
            self.endpoint = self.endpoint_claim_element
            self.payload = {'q': query_object.q}
            results = self.get_default_page()
            return results

        else:
            raise SendError("The object you are attempting to send is not a valid query object")

    def get_default_page(self):
        r = requests.post(url=self.endpoint, headers=self.headers, data=json.dumps(self.payload))
        self.parse_response_codes(r, self.debug)
        results = r.json()

        if 'totalPage' in results:
            total_page_count = int(results['totalPage'])
            print('Downloading page 1 of {}'.format(str(total_page_count)))
        return results

    def get_all_pages(self):
        pages = []

        first_page = self.get_default_page()
        pages.append(first_page)
        total_page_count = int(first_page['totalPage'])
        if total_page_count > 1:
            current_page_count = 2
            while current_page_count <= total_page_count:
                self.payload['q']['offset'] = current_page_count
                page = self.get_default_page()
                print('Downloading page {} of {}'.format(str(current_page_count),str(total_page_count)))
                pages.append(page)
                current_page_count += 1
        return pages

    def pages_to_assets(self,pages):
        assets = []
        # print(pages)
        for page in pages:
            assets.append(page['Assets'])

        assets = [j for i in assets for j in i]
        return assets

    def parse_response_codes(self, response, debug):
        if response.status_code == 200:
            if debug:
                print("Request successful")
                return

        if response.status_code == 400:
            raise APIConnectionError("Invalid format or invalid data is specified in the request")

        if response.status_code == 401:
            raise APIConnectionError("Authentication credentials were missing or incorrect")

        if response.status_code == 403:
            raise APIConnectionError("The request was understood, but it has been refused")

        if response.status_code == 404:
            raise APIConnectionError("The URI requested is invalid or the requested resource does not exist")

        if response.status_code == 429:
            raise APIConnectionError("You are making requests too quickly, slow down and try again.")

        if response.status_code == 500:
            raise APIConnectionError("Something unexpected occurred.")

        if response.status_code == 502:
            raise APIConnectionError("IP Street service is down")

        if response.status_code == 503:
            raise APIConnectionError("IP Street service is up but overloaded with requests")
