import pytest
from selenium import webdriver


# Фикстура веб-драйвера
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(options=webdriver.ChromeOptions())
    yield driver
    driver.quit()


