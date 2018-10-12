from faker import Faker

from imdb.tests.base.base import UIAutomationBase


fake = Faker()


class SearchTest(UIAutomationBase):

    def test_validate_search_result(self):

        query_string = fake.word()
        print('='*20, query_string, '='*20)
        self.home_page.search_by_keyword(query_string)

        movie_names = self.search_result_page.get_result_list()

        for movie_name in movie_names:
            assert query_string.lower() in movie_name.lower(), movie_name

        # all(query_string.lower() in movie_name.lower() for movie_name in movie_names)




