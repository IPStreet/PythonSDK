import unittest
from IPStreet import client, query

class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.api_key = "IPSTREET_API_KEY"
        self.api_version = 2
        self.client = client.Client(apikey=self.api_key , api_version=2)

        self.basic_data_query = query.PatentData()
        self.claim_only_concept_search = query.ClaimOnlySearch()
        self.full_text_concept_search = query.FullTextSearch()
        self.ngram_query = query.NgramQuery()
        self.keyphrase_query = query.KeyPhraseQuery()
        self.claim_elements_query = query.ClaimElementsQuery()


    def test_send_PatentData(self):
        self.basic_data_query.add_grant_number("7477713")
        self.client.send(self.basic_data_query)
        self.assertTrue(self.client.endpoint == self.client.endpoint_patent_data, "Client is sending payload to wrong endpoint")
        self.basic_data_query.remove_current_query()

    def test_send_NgramQuery(self):
        self.ngram_query.add_grant_number("7477713")
        self.client.send(self.ngram_query)
        self.assertTrue(self.client.endpoint == self.client.endpoint_ngram, "Client is sending payload to wrong endpoint")
        self.ngram_query.remove_current_query()

    def test_send_KeyPhraseQuery(self):
        self.keyphrase_query.add_grant_number("7477713")
        self.client.send(self.keyphrase_query)
        self.assertTrue(self.client.endpoint == self.client.endpoint_keyphrase, "Client is sending payload to wrong endpoint")
        self.keyphrase_query.remove_current_query()

    def test_send_ClaimElementsQuery(self):
        self.claim_elements_query.add_grant_number("7477713")
        self.client.send(self.claim_elements_query)
        self.assertTrue(self.client.endpoint == self.client.endpoint_claim_element, "Client is sending payload to wrong endpoint")
        self.claim_elements_query.remove_current_query()

    def test_send_ClaimOnlySearch(self):
        self.claim_only_concept_search.add_raw_text("test")
        self.claim_only_concept_search.add_grant_number("7477713")
        self.client.send(self.claim_only_concept_search)
        self.assertTrue(self.client.endpoint == self.client.endpoint_claim_only, "Client is sending payload to wrong endpoint")
        self.claim_only_concept_search.remove_current_query()

    def test_send_FullTextSearch(self):
        self.full_text_concept_search.add_raw_text("test")
        self.full_text_concept_search.add_grant_number("7477713")
        self.client.send(self.full_text_concept_search)
        self.assertTrue(self.client.endpoint == self.client.endpoint_full_text, "Client is sending payload to wrong endpoint")
        self.full_text_concept_search.remove_current_query()

    def test_check_service_status(self):
        pass

    def test_get_default_page(self):
        pass

    def test_get_all_pages(self):
        pass

    def test_pages_to_assets(self):
        pass

    def test_parse_response_codes(self):
        pass




if __name__ == '__main__':
    unittest.main()