from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):


    def is_the_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET) \
               and not self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_LINK)

