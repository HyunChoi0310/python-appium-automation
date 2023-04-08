from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultPage(Page):
    SEARCH_RESULT = (By.ID, 'org.wikipedia:id/page_list_item_title')

    def verify_search_result(self):
        expected_result = 'Python (programming language)'
        self.verify_text(expected_result, *self.SEARCH_RESULT)