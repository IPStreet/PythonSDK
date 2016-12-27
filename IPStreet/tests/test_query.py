import unittest
from IPStreet import query, error


class QueryTestCase(unittest.TestCase):
    def setUp(self):
        self.basic_data_query = query.PatentData()
        self.claim_only_concept_search = query.ClaimOnlySearch()
        self.full_text_concept_search = query.FullTextSearch()
        self.ngram_query = query.NgramQuery()
        self.keyphrase_query = query.KeyPhraseQuery()
        self.claim_elements_query = query.ClaimElementsQuery()

    def test_add_keywords(self):
        self.basic_data_query.add_keywords("test text")
        self.assertTrue('keywords' in self.basic_data_query.q)
        self.basic_data_query.remove_current_query()

    def test_add_owner(self):
        self.basic_data_query.add_owner("test text")
        self.assertTrue('owner' in self.basic_data_query.q)
        self.basic_data_query.remove_current_query()

    def test_add_ultimate_parent(self):
        self.basic_data_query.add_ultimate_parent("test text")
        self.assertTrue('ultimate_parent' in self.basic_data_query.q)
        self.basic_data_query.remove_current_query()

    def test_add_inventor(self):
        self.basic_data_query.add_inventor("test text")
        self.assertTrue('inventor' in self.basic_data_query.q)
        self.basic_data_query.remove_current_query()

    def test_add_patent_class(self):
        self.basic_data_query.add_patent_class("test text")
        self.assertTrue('patent_class' in self.basic_data_query.q)
        self.basic_data_query.remove_current_query()

    def test_add_patent_office(self):
        self.basic_data_query.add_patent_office("test text")
        self.assertTrue('patent_office' in self.basic_data_query.q)
        self.basic_data_query.remove_current_query()

    def test_add_grant_number(self):
        self.basic_data_query.add_grant_number("test text")
        self.assertTrue('grant_number' in self.basic_data_query.q)

        self.basic_data_query.add_grant_number("second test text")
        self.assertTrue(len(self.basic_data_query.q['grant_number']) == 2,
                        "additional numbers are not being appended correctly")

        self.basic_data_query.add_grant_number("third test text")
        self.assertTrue(len(self.basic_data_query.q['grant_number']) == 3,
                        "additional numbers are not being appended correctly")
        self.basic_data_query.remove_current_query()

    def test_add_application_number(self):
        self.basic_data_query.add_application_number("test text")
        self.assertTrue('application_number' in self.basic_data_query.q)

        self.basic_data_query.add_application_number("second test text")
        self.assertTrue(len(self.basic_data_query.q['application_number']) == 2,
                        "additional numbers are not being appended correctly")

        self.basic_data_query.add_application_number("third test text")
        self.assertTrue(len(self.basic_data_query.q['application_number']) == 3,
                        "additional numbers are not being appended correctly")
        self.basic_data_query.remove_current_query()

    def test_add_publication_number(self):
        self.basic_data_query.add_publication_number("test text")
        self.assertTrue('publication_number' in self.basic_data_query.q)

        self.basic_data_query.add_publication_number("second test text")
        self.assertTrue(len(self.basic_data_query.q['publication_number']) == 2,
                        "additional numbers are not being appended correctly")

        self.basic_data_query.add_publication_number("third test text")
        self.assertTrue(len(self.basic_data_query.q['publication_number']) == 3,
                        "additional numbers are not being appended correctly")
        self.basic_data_query.remove_current_query()

    def test_add_prior_owner(self):
        self.basic_data_query.add_prior_owner("test text")
        self.assertTrue('prior_owner' in self.basic_data_query.q)
        self.basic_data_query.remove_current_query()

    def test_add_law_firm(self):
        self.basic_data_query.add_law_firm("test text")
        self.assertTrue('law_firm' in self.basic_data_query.q)
        self.basic_data_query.remove_current_query()

    def test_add_examiner(self):
        self.basic_data_query.add_examiner("test text")
        self.assertTrue('examiner' in self.basic_data_query.q)
        self.basic_data_query.remove_current_query()

    def test_add_start_date(self):
        self.assertRaises(error.ParamsInvalidError, self.basic_data_query.add_start_date,
                          {'input': '2015', 'start_date_type': 'application_date'},
                          "Improper date format should raise ParamsInvalidError, it does not.")
        self.assertRaises(error.ParamsInvalidError, self.basic_data_query.add_start_date,{'input':'2015-01-01','start_date_type':'test'},
                          "Improper date format should raise ParamsInvalidError, it does not.")

        self.basic_data_query.add_start_date('2016-01-01', 'application_date')
        self.assertTrue('start_date' in self.basic_data_query.q)
        self.assertTrue(self.basic_data_query.q['start_date'] == '2016-01-01')
        self.assertTrue('start_date_type' in self.basic_data_query.q)
        self.assertTrue(self.basic_data_query.q['start_date_type'] == 'application_date')
        self.basic_data_query.remove_current_query()

    def test_add_end_date(self):
        self.assertRaises(error.ParamsInvalidError, self.basic_data_query.add_end_date,
                          {'input': '2015', 'end_date_type': 'application_date'},
                          "Improper date format should raise ParamsInvalidError, it does not.")

        self.assertRaises(error.ParamsInvalidError, self.basic_data_query.add_end_date,
                          {'input': '2015-01-01', 'end_date_type': 'test'},
                          "Improper date format should raise ParamsInvalidError, it does not.")

        self.basic_data_query.add_end_date('2016-01-01', 'application_date')
        self.assertTrue('end_date' in self.basic_data_query.q)
        self.assertTrue(self.basic_data_query.q['end_date'] == '2016-01-01')
        self.assertTrue('end_date_type' in self.basic_data_query.q)
        self.assertTrue(self.basic_data_query.q['end_date_type'] == 'application_date')
        self.basic_data_query.remove_current_query()

    def test_add_applied(self):
        self.assertRaises(error.ParamsInvalidError,self.basic_data_query.add_applied,{'input':"test text"})

        self.basic_data_query.add_applied('True')
        self.assertTrue('applied' in self.basic_data_query.q)
        self.assertTrue(self.basic_data_query.q['applied'] == 'True')
        self.basic_data_query.remove_current_query()

    def test_add_granted(self):
        self.assertRaises(error.ParamsInvalidError, self.basic_data_query.add_granted, {'input': "test text"})

        self.basic_data_query.add_granted('True')
        self.assertTrue('granted' in self.basic_data_query.q)
        self.assertTrue(self.basic_data_query.q['granted'] == 'True')
        self.basic_data_query.remove_current_query()

    def test_add_expired(self):
        self.assertRaises(error.ParamsInvalidError, self.basic_data_query.add_expired, {'input': "test text"})

        self.basic_data_query.add_expired('True')
        self.assertTrue('expired' in self.basic_data_query.q)
        self.assertTrue(self.basic_data_query.q['expired'] == 'True')
        self.basic_data_query.remove_current_query()

    def test_add_max_expected_results(self):
        self.assertRaises(error.ParamsInvalidError, self.basic_data_query.add_max_expected_results, {'input': "test"})

        self.basic_data_query.add_max_expected_results(50)
        self.assertTrue('max_expected_results' in self.basic_data_query.q)
        self.assertTrue(self.basic_data_query.q['max_expected_results'] == 50)
        self.basic_data_query.remove_current_query()

    def test_add_page_size(self):
        self.assertRaises(error.ParamsInvalidError, self.basic_data_query.add_page_size, {'input': "test"})

        self.basic_data_query.add_page_size(50)
        self.assertTrue('page_size' in self.basic_data_query.q)
        self.assertTrue(self.basic_data_query.q['page_size'] == 50)
        self.basic_data_query.remove_current_query()

    def test_add_offset(self):
        self.assertRaises(error.ParamsInvalidError, self.basic_data_query.add_offset, {'input': "test"})

        self.basic_data_query.add_offset(50)
        self.assertTrue('offset' in self.basic_data_query.q)
        self.assertTrue(self.basic_data_query.q['offset'] == 50)
        self.basic_data_query.remove_current_query()

    def test_print_current_query(self):
        pass

    def test_basic_data_query_object(self):
        self.basic_data_query.add_ultimate_parent('Tesla Motors, Inc.')
        self.basic_data_query.add_end_date('2016-01-01', 'application_date')
        self.basic_data_query.add_keywords('battery')
        self.basic_data_query.add_max_expected_results(20000)

        self.assertIsInstance(self.basic_data_query.q, dict, "The query you have constructed is not a dict.")
        self.assertDictEqual(self.basic_data_query.q, {'ultimate_parent': 'Tesla Motors, Inc.',
                                                       'end_date': '2016-01-01',
                                                       'end_date_type': 'application_date',
                                                       'keywords': 'battery',
                                                       'max_expected_results': 20000},
                             "The constructed query does not match the intended query")

        self.basic_data_query.remove_current_query()

    def test_claim_only_query_object(self):
        self.claim_only_concept_search.add_raw_text("This is a text")
        self.assertIn('This is a text', self.claim_only_concept_search.raw_text,
                      "The constructed query does not match the intended query.")

        self.claim_only_concept_search.add_ultimate_parent('Tesla Motors, Inc.')
        self.claim_only_concept_search.add_end_date('2016-01-01', 'application_date')
        self.claim_only_concept_search.add_keywords('battery')
        self.claim_only_concept_search.add_max_expected_results(20000)
        self.assertDictEqual(self.claim_only_concept_search.q, {'ultimate_parent': 'Tesla Motors, Inc.',
                                                                'end_date': '2016-01-01',
                                                                'end_date_type': 'application_date',
                                                                'keywords': 'battery',
                                                                'max_expected_results': 20000},
                             "The constructed query does not match the intended query")

    def test_full_text_query_object(self):
        self.full_text_concept_search.add_raw_text("This is a text")
        self.assertIn('This is a text', self.full_text_concept_search.raw_text,
                      "The constructed query does not match the intended query.")

        self.full_text_concept_search.add_ultimate_parent('Tesla Motors, Inc.')
        self.full_text_concept_search.add_end_date('2016-01-01', 'application_date')
        self.full_text_concept_search.add_keywords('battery')
        self.full_text_concept_search.add_max_expected_results(20000)

        self.assertDictEqual(self.full_text_concept_search.q, {'ultimate_parent': 'Tesla Motors, Inc.',
                                                               'end_date': '2016-01-01',
                                                               'end_date_type': 'application_date',
                                                               'keywords': 'battery',
                                                               'max_expected_results': 20000},
                             "The constructed query does not match the intended query")

    def test_ngram_query_object(self):
        self.ngram_query.add_grant_number('6895123')

        self.assertIsInstance(self.ngram_query.q, dict, "The query you have constructed is not a dict.")
        self.assertDictEqual(self.ngram_query.q, {'grant_number': '6895123'})

    def test_keyphrase_valid_json(self):
        self.keyphrase_query.add_grant_number('6895123')

        self.assertIsInstance(self.keyphrase_query.q, dict, "The query you have constructed is not a dict.")
        self.assertDictEqual(self.keyphrase_query.q, {'grant_number': '6895123'})

    def test_claim_elements_valid_json(self):
        self.claim_elements_query.add_grant_number('6895123')

        self.assertIsInstance(self.claim_elements_query.q, dict, "The query you have constructed is not a dict.")
        self.assertDictEqual(self.claim_elements_query.q, {'grant_number': '6895123'})


if __name__ == '__main__':
    unittest.main()
