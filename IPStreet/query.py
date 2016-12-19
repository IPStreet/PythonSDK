from datetime import datetime
from IPStreet import error

class Query:
    def __init__(self):
        self.q = {}
        self.query_is_big = 10000

    def add_keywords(self, input):
        if 'keywords' in self.q.keys():
            self.q['keywords'] = self.q['keywords'] + ', ' + (str(input))
        else:
            self.q['keywords'] = str(input)

    def add_owner(self, input):
        if 'owner' in self.q.keys():
            self.q['owner'] = self.q['owner'] + ', ' + (str(input))
        else:
            self.q['owner'] = str(input)

    def add_ultimate_parent(self, input):
        if 'ultimate_parent' in self.q.keys():
            self.q['ultimate_parent'] = self.q['ultimate_parent'] + ', ' + (str(input))
        else:
            self.q['ultimate_parent'] = str(input)

    def add_inventor(self, input):
        if 'inventor' in self.q.keys():
            self.q['inventor'] = self.q['inventor'] + ', ' + (str(input))
        else:
            self.q['inventor'] = str(input)

    def add_patent_class(self, input):
        if 'patent_class' in self.q.keys():
            self.q['patent_class'] = self.q['patent_class'] + ', ' + (str(input))
        else:
            self.q['patent_class'] = str(input)

    def add_patent_office(self, input):
        if 'patent_office' in self.q.keys():
            self.q['patent_office'] = self.q['patent_office'] + ', ' + (str(input))
        else:
            self.q['patent_office'] = str(input)

    def add_grant_number(self, input):
        if 'grant_number' in self.q.keys():
            current_list = self.q['grant_number']
            current_list.append(str(input))
            self.q['grant_number'] = current_list
        else:
            self.q['grant_number'] = [str(input)]

    def add_application_number(self, input):
        if 'application_number' in self.q.keys():
            current_list = self.q['application_number']
            current_list.append(str(input))
            self.q['application_number'] = current_list
        else:
            self.q['application_number'] = [str(input)]


    def add_publication_number(self, input):
        if 'publication_number' in self.q.keys():
            current_list = self.q['publication_number']
            current_list.append(str(input))
            self.q['publication_number'] = current_list
        else:
            self.q['publication_number'] = [str(input)]

    def add_prior_owner(self, input):
        if 'prior_owner' in self.q.keys():
            self.q['prior_owner'] = self.q['prior_owner'] + ', ' + (str(input))
        else:
            self.q['prior_owner'] = str(input)

    def add_law_firm(self, input):
        if 'law_firm' in self.q.keys():
            self.q['law_firm'] = self.q['law_firm'] + ', ' + (str(input))
        else:
            self.q['law_firm'] = str(input)

    def add_examiner(self, input):
        if 'examiner' in self.q.keys():
            self.q['examiner'] = self.q['examiner'] + ', ' + (str(input))
        else:
            self.q['examiner'] = str(input)

    def add_start_date(self, input, start_date_type):
        try:
            datetime.strptime(input, "%Y-%m-%d")
        except:
            error.ParamsInvalidError("end_date requires a date object in %Y-%m-%d format")

        if str(start_date_type) not in ['earliest_date_filed', 'application_date',
                                'publication_date', 'grant_date', 'expiration_date']:
            raise error.ParamsInvalidError("start_date_type must be 'earliest_date_filed','application_date', 'publication_date','grant_date', or 'expiration_date")
        else:
            self.q['start_date'] = input
            self.q['start_date_type'] = start_date_type

    def add_end_date(self, input, end_date_type):
        try:
            datetime.strptime(input, "%Y-%m-%d")
        except:
            error.ParamsInvalidError("end_date requires a date object in %Y-%m-%d format")

        if str(end_date_type) not in ['earliest_date_filed', 'application_date',
                                            'publication_date', 'grant_date', 'expiration_date']:
            raise error.ParamsInvalidError(
                "end_date_type must be 'earliest_date_filed','application_date', 'publication_date','grant_date', or 'expiration_date")
        else:
            self.q['end_date'] = input
            self.q['end_date_type'] = end_date_type

    def add_applied(self, input):
        if input not in ['True', 'False']:
            raise error.ParamsInvalidError("add_applied accepts only True or False")
        else:
            self.q['applied'] = input


    def add_granted(self, input):
        if input not in ['True', 'False']:
            raise error.ParamsInvalidError("add_granted accepts only True or False")
        else:
            self.q['granted'] = input

    def add_expired(self, input):
        if input not in ['True', 'False']:
            raise error.ParamsInvalidError("add_granted accepts only True or False")
        else:
            self.q['expired'] = input

    def add_max_expected_results(self, input):
        if type(input) is not int:
            raise error.ParamsInvalidError("max_expected_results should be an int")
        else:
            self.q['max_expected_results'] = input

        if input > self.query_is_big:
            print("Your response size will be very large, expect query to take a long time.")

    def add_page_size(self, input):
        if type(input) is not int:
            raise error.ParamsInvalidError("page_size should be an int")
        else:
            self.q['page_size'] = input


    def add_offset(self, input):
        if type(input) is not int:
            raise error.ParamsInvalidError("offset should be an int")
        else:
            self.q['offset'] = input

    def print_current_query(self):
        print(vars(self))

    def remove_current_query(self):
        self.q = {}

class PatentData(Query):
    pass


class ConceptSearchQuery(Query):
    def __init__(self):
        self.raw_text = None
        super(ConceptSearchQuery, self).__init__()

    def add_raw_text(self, raw_text):
        try:
            type(raw_text) is str
        except TypeError:
            print("raw_text should be a string")
        else:
            self.raw_text = raw_text


class FullTextSearch(ConceptSearchQuery):
    def __init__(self):
        super(FullTextSearch, self).__init__()


class ClaimOnlySearch(ConceptSearchQuery):
    def __init__(self):
        super(ClaimOnlySearch, self).__init__()


class ClaimParserQuery:
    def __init__(self):
        self.q = {}

    def add_grant_number(self, input):
        if 'grant_number' in self.q.keys():
            self.q['grant_number'] = self.q['grant_number'] + ', ' + (str(input))
        else:
            self.q['grant_number'] = str(input)

    def add_application_number(self, input):
        if 'application_number' in self.q.keys():
            self.q['application_number'] = self.q['application_number'] + ', ' + (str(input))
        else:
            self.q['application_number'] = str(input)

    def add_publication_number(self, input):
        if 'publication_number' in self.q.keys():
            self.q['publication_number'] = self.q['publication_number'] + ', ' + (str(input))
        else:
            self.q['publication_number'] = str(input)

    def add_patent_office(self, input):
        if 'patent_office' in self.q.keys():
            self.q['patent_office'] = self.q['patent_office'] + ', ' + (str(input))
        else:
            self.q['patent_office'] = str(input)

    def remove_current_query(self):
        self.q = {}



class NgramQuery(ClaimParserQuery):
    def __init__(self):
        super(NgramQuery, self).__init__()


class KeyPhraseQuery(ClaimParserQuery):
    def __init__(self):
        super(KeyPhraseQuery, self).__init__()


class ClaimElementsQuery(ClaimParserQuery):
    def __init__(self):
        super(ClaimElementsQuery, self).__init__()
