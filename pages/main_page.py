from selenium.webdriver.common.by import By
import time

from locators.elements_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def click_universal_category_link(self, driver, category):
        driver.find_element(By.XPATH, f"//a[@class='menu-categories__link' and contains(.,'{category}')]").click()
        time.sleep(3)

    def set_search_input(self, param):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(param)

    def click_search_button(self):
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()

    def click_city_toggle(self):
        self.element_is_visible(self.locators.CITY_TOGGLE).click()

    def click_burger_menu_button(self):
        self.element_is_visible(self.locators.BURGER_MENU).click()

    def click_sign_in_button(self):
        self.element_is_visible(self.locators.SIGN_IN_BUTTON).click()

    def click_register_link(self):
        self.element_is_visible(self.locators.REGISTER_LINK).click()

    def click_register_button(self):
        self.element_is_visible(self.locators.REGISTER_BUTTON).click()

    def type_text_input_field(self, driver, xpath_param, text_param):
        driver.find_element(By.XPATH, xpath_param).clear()
        driver.find_element(By.XPATH, xpath_param).send_keys(text_param)

    def check_is_element_present(self, driver, xpath_param):
        return driver.find_element(By.XPATH, xpath_param).is_displayed()

    def set_city_input(self, param):
        self.element_is_visible(self.locators.CITY_INPUT_FIELD).clear()
        self.element_is_visible(self.locators.CITY_INPUT_FIELD).send_keys(param)

    def choose_city_click(self):
        self.element_is_visible(self.locators.CHOSEN_CITY).click()

    def click_apply_button(self):
        self.element_is_visible(self.locators.APPLY_CHOSEN_CITY_BUTTON).click()

    def verify_chosen_city(self, param):
        return str(self.element_is_present(self.locators.CITY_TOGGLE_TEXT).text).__contains__(param)

    def get_goods_title_text(self):
        buffer = self.elements_are_present(self.locators.GOODS_TITLE_TEXTS)
        goods_title_texts = []
        for elem in buffer:
            goods_title_texts.append(elem.text)
        return goods_title_texts

    def verify_is_search_brand_present_in_goods_title(self, brand):
        goods_title_texts = [x.lower() for x in MainPage.get_goods_title_text(self)]
        res = all([ele for ele in str(brand).lower() if (ele in goods_title_texts)])
        return res

    def verify_wrong_search_request(self):
        time.sleep(2)
        return self.element_is_present(self.locators.NOT_FOUND_TEXT).is_displayed()
