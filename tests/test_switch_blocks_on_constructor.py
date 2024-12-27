from locators import TestLocators
from conftest import driver
from urls import DataUrls

class TestSwitchBlocksOnConstructor:

    # Проверка перехода в раздел "Начинки"
    def test_transfer_to_topping_block_from_sauces(self, driver):
        driver.get(DataUrls.URL)

        driver.find_element(*TestLocators.sause_block).click()
        driver.find_element(*TestLocators.topping_block).click()
        assert driver.find_element(*TestLocators.selected_button).text == "Начинки"

    # Проверка перехода в раздел "Соусы"
    def test_transfer_to_sauces_block_from_fillings(self, driver):
        driver.get(DataUrls.URL)

        driver.find_element(*TestLocators.sause_block).click()
        assert driver.find_element(*TestLocators.selected_button).text == "Соусы"

    # Проверка перехода в раздел "Булки"
    def test_transfer_to_bread_block_from_fillings(self, driver):
        driver.get(DataUrls.URL)

        driver.find_element(*TestLocators.sause_block).click()
        driver.find_element(*TestLocators.bread_block).click()
        assert driver.find_element(*TestLocators.selected_button).text == "Булки"