from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_url_correct(self, correct_substring):
        get_url = self.browser.current_url
        sub_string_url = get_url.split('/')[-1]
        return sub_string_url == correct_substring, print(sub_string_url)

