from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        basket_link.click()

    def text_after_add_to_basket(self):
        name_link = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name = name_link.text
        print(name)
        name_link_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        name_in_basket = name_link_in_basket.text
        print(name_in_basket)
        price_link = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price = price_link.text
        print(price)
        price_link_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        price_in_basket = price_link_in_basket.text
        print(price_in_basket)
        assert (name == name_in_basket) and (price == price_in_basket), "Name and price not found"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Element not disappeared"
