import pytest
from selenium import webdriver


# Фикстура веб-драйвера
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(options=webdriver.ChromeOptions())
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


