import time
import allure
from pages.main_page import MainPage
import pytest
import logging
from pytest_zebrunner import attach_test_artifact
from utils.attachments import attach_screenshot, attach_logs, attach_recorded_video
from locators.elements_page_locators import MainPageLocators

@allure.suite('MainPage')
class TestsRozetkaMainPageSearch:

    @pytest.mark.label("Search", "correct")
    @allure.title('Check correct search')
    def test_correct_search(self, driver):
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        main_page.open()
        attach_screenshot()
        search_text = "Agm A9"
        main_page.set_search_input(search_text)
        main_page.click_search_button()
        attach_screenshot()
        attach_logs(logging.INFO, 'Test was successful')
        assert main_page.verify_is_search_brand_present_in_goods_title(search_text), "Search text not" \
                                                                                     " contains in all " \
                                                                                     "goods title texts"

    @pytest.mark.label("Search", "Incorrect")
    @allure.title('Check incorrect search')
    def test_incorrect_search(self, driver):
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        main_page.open()
        attach_screenshot()
        search_text = "hgvhvg"
        main_page.set_search_input(search_text)
        main_page.click_search_button()
        attach_screenshot()
        attach_logs(logging.INFO, 'Test was successful')
        assert main_page.verify_wrong_search_request(), "Wrong request text isn`t presented"
        assert "Google"=="Google"

    @pytest.mark.parametrize("first_name,last_name,phone,email,password,xpath_param",
                             [("jgjhjghj", "Білий", "0993050111", "vitalii@gmail.com", "Hh3vhvjj",
                               MainPageLocators.REGISTER_ERROR_MESSAGE),
                              ("Віталій", "jhvjjj", "0993050111", "vitalii@gmail.com ", "Hh3vhvjj",
                               MainPageLocators.REGISTER_ERROR_MESSAGE),
                              ("Віталій", "Білий", "hvghvg", "vitalii@gmail.com", "Hh3vhvjj",
                               MainPageLocators.REGISTER_ERROR_MESSAGE),
                              ("Віталій", "Білий", "мрпмрпр", "vitalii@gmail.com", "Hh3vhvjj",
                               MainPageLocators.REGISTER_ERROR_MESSAGE),
                              ("Віталій", "Білий", " 0", "vitalii@gmail.com", "Hh3vhvjj",
                               MainPageLocators.REGISTER_ERROR_MESSAGE),
                              ("Віталій", "Білий", "0993050111", "@gmail.com", "Hh3vhvjj",
                               MainPageLocators.REGISTER_ERROR_MESSAGE),
                              ("Віталій", "Білий", "0993050111", "vitalii@.com", "Hh3vhvjj",
                               MainPageLocators.REGISTER_ERROR_MESSAGE),
                              ("Віталій", "Білий", "0993050111", "vitalii@gmail", "Hh3vhvjj",
                               MainPageLocators.REGISTER_ERROR_MESSAGE),
                              ("Віталій", "Білий", "0993050111", "vitalii@gmail.com", "hjgjgj",
                               MainPageLocators.REGISTER_ERROR_LIST_MESSAGE),
                              ("Віталій", "Білий", "0993050111", "vitalii@gmail.com", "Hhjgjgj",
                               MainPageLocators.REGISTER_ERROR_LIST_MESSAGE),
                              ("Віталій", "Білий", "0993050111", "vitalii@gmail.com", "hj3gjgj",
                               MainPageLocators.REGISTER_ERROR_LIST_MESSAGE),
                              ("Віталій", "Білий", "0993050111", "vitalii@gmail.com", "Ррпмрпр",
                               MainPageLocators.REGISTER_ERROR_LIST_MESSAGE)])
    def test_incorrect_register(self, driver, first_name, last_name, phone, email, password, xpath_param):
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        main_page.open()
        attach_screenshot()
        main_page.click_sign_in_button()
        attach_screenshot()
        main_page.click_register_link()
        attach_screenshot()
        main_page.type_text_input_field(driver, MainPageLocators.FIRSTNAME_INPUT_FIELD, first_name)
        main_page.type_text_input_field(driver, MainPageLocators.LASTNAME_INPUT_FIELD, last_name)
        main_page.type_text_input_field(driver, MainPageLocators.USER_PHONE_NUMBER_INPUT_FIELD, phone)
        main_page.type_text_input_field(driver, MainPageLocators.USER_EMAIL_INPUT_FIELD, email)
        main_page.type_text_input_field(driver, MainPageLocators.USER_PASSWORD_INPUT_FIELD, password)
        main_page.click_register_button()
        attach_screenshot()
        assert main_page.check_is_element_present(driver, xpath_param), "Register error message isn't presented"

    @pytest.mark.parametrize("city_name", [("Львів"), ("Житомир"), ("Тернопіль"), ("Луцьк")])
    def test_change_destination_city(self, driver, city_name):
        main_page = MainPage(driver, 'https://rozetka.com.ua/ua/')
        main_page.open()
        attach_screenshot()
        main_page.click_burger_menu_button()
        attach_screenshot()
        main_page.click_city_toggle()
        attach_screenshot()
        main_page.set_city_input(city_name)
        attach_screenshot()
        main_page.choose_city_click()
        attach_screenshot()
        main_page.click_apply_button()
        main_page.click_burger_menu_button()
        attach_screenshot()
        assert main_page.verify_chosen_city(city_name), "Toggle isn't contains chosen city"

