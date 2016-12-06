import json

from IPStreet import client, query

if __name__ == '__main__':

    ########################################################################
    #    Basic configuration data                                          #
    ########################################################################
    apikey = '5AsaMTe6HUypUlAqv3Rw3E6Pvjo4dYL64Rr2z2va'
    api_version = 2

    ########################################################################
    #    Instantiate the client                                            #
    ########################################################################
    client = client.Client(apikey=apikey, api_version=api_version)


    ########################################################################
    #    Instantiate and run an ngram query                                #
    ########################################################################
    ngram_query = query.NgramQuery()
    ngram_query.add_grant_number('6895123')
    ngram_results = client.send(ngram_query)
    print(ngram_results)

    ########################################################################
    #    Instantiate and run an key phrase parse query                     #
    ########################################################################
    keyphrase_query = query.KeyPhraseQuery()
    keyphrase_query.add_grant_number('6895123')
    keyphrase_results = client.send(keyphrase_query)
    print(keyphrase_results)

    ########################################################################
    #    Instantiate and run an claim elements query                        #
    ########################################################################
    claim_elements_query = query.ClaimElementsQuery()
    claim_elements_query.add_grant_number('6895123')
    claim_elements_results = client.send(claim_elements_query)
    print(claim_elements_results)

    ########################################################################
    #    Instantiate and run an basic data query                           #
    ########################################################################
    basic_data_query = query.PatentData()
    basic_data_query.add_ultimate_parent('Tesla Motors, Inc.')
    basic_data_query.add_end_date('2016-01-01', 'application_date')
    basic_data_query.add_keywords('battery')
    basic_data_query.add_max_expected_results(200)
    basic_data_query.add_page_size(100)
    basic_data_results = client.send(basic_data_query)
    print(basic_data_results)


    ########################################################################
    #    Instantiate and run a claim_only concept search query             #
    ########################################################################
    claim_only_concept_search = query.ClaimOnlySearch()
    claim_only_concept_search.add_raw_text("a configurable battery pack charging system coupled to said charging "
                                           "system controller, said battery pack and a power source,"
                                           "wherein said configurable battery pack charging system charges said"
                                           "battery pack in accordance with said battery pack charging "
                                           "conditions set by said charging system controller.")
    claim_only_concept_search.add_max_expected_results(100)
    claim_only_concept_results = client.send(claim_only_concept_search)

    ########################################################################
    #    Instantiate and run an full_test data query                       #
    ########################################################################
    full_text_concept_search = query.FullTextSearch()
    full_text_concept_search.add_raw_text("a configurable battery pack charging system coupled to said charging "
                                           "system controller, said battery pack and a power source,"
                                           "wherein said configurable battery pack charging system charges said"
                                           "battery pack in accordance with said battery pack charging "
                                           "conditions set by said charging system controller.")
    full_text_concept_search.add_max_expected_results(100)
    full_text_concept_results = client.send(full_text_concept_search)

