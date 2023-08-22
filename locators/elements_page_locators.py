from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[class*='button_color_green']")
    GOODS_TITLE_TEXTS = (By.XPATH, "//span[@class='goods-tile__title']")
    NOT_FOUND_TEXT = (By.XPATH, "//span[@class='ng-star-inserted']")
    BURGER_MENU = (By.XPATH, "//rz-mobile-user-menu[contains(@class,'menu')]/button[contains(@class,'header__button')]")
    CITY_TOGGLE = (By.XPATH, "//button[contains(@class,'city-toggle')]")
    CITY_INPUT_FIELD = (By.XPATH, "//input[contains(@class,'input-text')]")
    CHOSEN_CITY = (By.XPATH, "(//div[@class='autocomplete__item'])[1]")
    APPLY_CHOSEN_CITY_BUTTON = (By.XPATH, "//div[@class='header-location__footer']/button[contains(@class,'button')]")
    CITY_TOGGLE_TEXT = (By.XPATH, "//span[@class='city-toggle__text']")
    SIGN_IN_BUTTON = (By.XPATH,"//li[contains(@class,'user')]")
    REGISTER_LINK = (By.XPATH,"//button[contains(@class,'register-link')]")
    FIRSTNAME_INPUT_FIELD = "//input[@id='registerUserName']"
    LASTNAME_INPUT_FIELD = "//input[@id='registerUserSurname']"
    USER_PHONE_NUMBER_INPUT_FIELD = "//input[@id='registerUserPhone']"
    USER_EMAIL_INPUT_FIELD = "//input[@id='registerUserEmail']"
    USER_PASSWORD_INPUT_FIELD = "//input[@id='registerUserPassword']"
    REGISTER_BUTTON = (By.XPATH,"//button[contains(@class,'auth-modal__submit')]")
    REGISTER_ERROR_MESSAGE = "//p[contains(@class,'validation-message')]"
    REGISTER_ERROR_LIST_MESSAGE = "//ul[contains(@class,'errors-list')]"


class DevicePageLocators:
    SHORT_CHARACTERISTICS_TITLE = "//h1[@class='product__title']"
    PRODUCT_PRICE = "//p[contains(@class,'product-price__big')]"
    SHORT_CHARACTERISTIC = "//p[@class='product-about__brief ng-star-inserted']"
    ALL_CHARACTERISTIC = "//h3[@class='product-tabs__heading']//span[contains(@class,'heading_color_gray')]"


class DeviceCategoryLocators:
    FILTER_LINKS="//li[contains(@class,'selection')]//a[contains(@class,'link')]"
    OK_BUTTON = "//button[contains(@class,'slider-filter__button')]"
    DEVICE_PRICES = "//span[@class='goods-tile__price-value']"
    GOODS_TITLE_TEXT = "//span[@class='goods-tile__title']"
    CART_GOODS_COUNTER_TEXT = "//span[contains(@class,'badge--green')]"
    SHOPPING_BASKET_BUTTON = "//li[contains(@class,'cart')]/*/button[contains(@class,'header__button')]"


class ShoppingBasketLocators:
    UNIVERSAL_PRICE_INPUT_VALUE = "//input[@data-testid='cart-counter-input']"
    SUM_PRICE_TEXT = "//div[@class='cart-receipt__sum-price']//span"
    EMPTY_STATUS_TEXT = "//h4[@class='cart-dummy__heading']"
    GOODS_IN_CART_TITLE_PRICE = "//p[@data-testid='cost']"
