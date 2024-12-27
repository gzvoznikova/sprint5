from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import driver
from urls import DataUrls


class TestNavigateToConstructor:
    # Проверка перехода по клику на Конструктор
    def test_transfer_from_lk_to_constructor_by_header(self, driver):
        driver.get(DataUrls.URL)

        driver.find_element(*TestLocators.button_lk).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.input_email_auth))
        driver.find_element(*TestLocators.header_of_page_constructor).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_login_in_main))
        assert driver.find_element(*TestLocators.button_login_in_main).is_displayed()

    # Проверка перехода по клику на логотип
    def test_transfer_from_lk_to_constructor_by_logo(self, driver):
        driver.get(DataUrls.URL)

        driver.find_element(*TestLocators.button_lk).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.input_email_auth))
        driver.find_element(*TestLocators.logo).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_login_in_main))
        assert driver.find_element(*TestLocators.button_login_in_main).is_displayed()