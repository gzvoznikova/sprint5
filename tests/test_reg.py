from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import driver


class TestRegistration:
    # Регистрация аккаунта пользователя с валидными значениями
    def test_reg_new_account_success(self, driver):
        username = 'lina111111'
        email = 'lina111111@ya.ru'
        password = 'pass101111111'
        driver.find_element(*TestLocators.button_login_in_main).click()
        driver.find_element(*TestLocators.button_register).click()
        driver.find_element(*TestLocators.input_name).send_keys(username)
        driver.find_element(*TestLocators.input_email).send_keys(email)
        driver.find_element(*TestLocators.input_password).send_keys(password)
        driver.find_element(*TestLocators.button_submit).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_login))
        assert driver.find_element(*TestLocators.button_register).is_displayed()

    # Регистрация аккаунта при пустом поле "Имя"
    def test_reg_name_is_empty_failed(self, driver):
        email = 'lina@ya.ru'
        password = 'pass101'
        driver.find_element(*TestLocators.button_login_in_main).click()
        driver.find_element(*TestLocators.button_register).click()
        driver.find_element(*TestLocators.input_name).send_keys('')
        driver.find_element(*TestLocators.input_email).send_keys(email)
        driver.find_element(*TestLocators.input_password).send_keys(password)
        driver.find_element(*TestLocators.button_submit).click()
        assert driver.find_element(*TestLocators.button_submit).is_displayed()

    # Регистрация аккаунта при вводе невалидного значения в поле Email — отсутствует @
    def test_reg_invalid_email_format_without(self, driver):
        username = 'aikern'
        email_name = 'aikern'
        password = 'pass101'
        driver.find_element(*TestLocators.button_login_in_main).click()
        driver.find_element(*TestLocators.button_register).click()
        driver.find_element(*TestLocators.input_name).send_keys(username)
        driver.find_element(*TestLocators.input_email).send_keys(f'{email_name}ya.ru')
        driver.find_element(*TestLocators.input_password).send_keys(password)
        driver.find_element(*TestLocators.button_submit).click()
        assert driver.find_element(*TestLocators.button_submit).is_displayed()

    # Регистрация аккаунта при вводе невалидного значения в поле Email
    def test_reg_invalid_mail_format_failed(self, driver):
        username = 'aikern'
        email_name = 'aikern'
        password = 'pass101'
        driver.find_element(*TestLocators.button_login_in_main).click()
        driver.find_element(*TestLocators.button_register).click()
        driver.find_element(*TestLocators.input_name).send_keys(username)
        driver.find_element(*TestLocators.input_email).send_keys(f'{email_name}@ya.')
        driver.find_element(*TestLocators.input_password).send_keys(password)
        driver.find_element(*TestLocators.button_submit).click()
        assert driver.find_element(*TestLocators.button_submit).is_displayed()

    # Проверка появления подсказки при вводе невалидного по длине значения в поле "Пароль"
    def test_reg_invalid_length_password_notification(self, driver):
        username = 'aikern'
        email = 'lina@ya.ru'
        password = '12345'
        driver.find_element(*TestLocators.button_login_in_main).click()
        driver.find_element(*TestLocators.button_register).click()
        driver.find_element(*TestLocators.input_name).send_keys(username)
        driver.find_element(*TestLocators.input_email).send_keys(email)
        driver.find_element(*TestLocators.input_password).send_keys(password)
        driver.find_element(*TestLocators.button_submit).click()
        assert driver.find_element(*TestLocators.notification_incorrect_password).text == 'Некорректный пароль'