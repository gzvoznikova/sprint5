import pytest
from selenium import webdriver


# Фикстура веб-драйвера
@pytest.fixture(scope="function")
def driver():
    # driver = webdriver.Chrome(options=webdriver.ChromeOptions())
    driver = webdriver.Firefox(options=webdriver.FirefoxOptions())
    yield driver
    driver.quit()


