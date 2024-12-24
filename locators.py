from selenium.webdriver.common.by import By


class TestLocators:
    # Регистрация аккаунта
    # Поле "Имя"
    input_name = By.XPATH, '//label[text()="Имя"]/following-sibling::input'

    # Поле Email
    input_email = By.XPATH, './/label[text()="Email"]/following-sibling::input'

    # Поле "Пароль"
    input_password = By.XPATH, './/input[@name="Пароль"]'

    # Кнопка "Зарегистрироваться"
    button_submit = By.XPATH, '//button[text() = "Зарегистрироваться"]'

    # Сообщение об ошибке: пароль не прошел валидацию
    notification_incorrect_password = By.XPATH, '//p[text() = "Некорректный пароль"]'

    # Кнопка "Войти" на форме регистрации
    button_login_in_registration_form = By.XPATH, '//a[text() = "Войти"]'

    # Аутентификация
    # Поле Email
    input_email_auth = By.XPATH, '//label[text()="Email"]/following-sibling::input'

    # Поле "Пароль"
    input_password_auth = By.XPATH, '//input[@name = "Пароль"]'

    # Кнопка "Войти"
    button_login = By.XPATH, '//button[text()="Войти"]'

    # Кнопка "Зарегистрироваться"
    button_register = By.XPATH, '//a[text() = "Зарегистрироваться"]'

    # Восстановление пароля
    # Кнопка "Восстановить пароль"
    button_forgot_password = By.XPATH, '//a[text() = "Восстановить пароль"]'

    # Кнопка "Войти" в форме регистрации
    button_login_passwd_recovery_form = By.XPATH, '//a[text() = "Войти"]'

    # Личный кабинет
    # Раздел "Профиль"
    profile = By.XPATH, '//a[@href = "/account/profile"]'

    # Раздел "История заказов"
    order_history = By.XPATH, '//a[@href = "/account/order-history"]'

    # Кнопка "Выйти", логаут
    button_logout = By.XPATH, '//button[@type = "button"]'

    # Главная
    # Кнопка "Войти в аккаунт" на главной
    button_login_in_main = By.XPATH, '//button[text() = "Войти в аккаунт"]'

    # Кнопка "Личный кабинет"
    button_lk = By.XPATH, '//p[text() = "Личный Кабинет"]'

    # Кнопка "Оформить заказ"
    button_make_the_order = By.XPATH, '//button[text()="Оформить заказ"]'

    # Кнопка "Конструктор" в шапке сайта
    header_of_page_constructor = By.XPATH, '//p[text() = "Конструктор"]'

    # Селектор, помечающий выбранный раздел конструктора как активный
    selected_button = By.XPATH, ('//div[@class = "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')

    # Заголовок раздела "Булки" в меню конструктора
    bread_block = By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[1]/span[text() = "Булки"]'

    # Заголовок раздела "Соусы" в меню конструктора
    sause_block = By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[2]/span[text() = "Соусы"]'

    # Заголовок раздела "Начинки" в меню конструктора
    topping_block = By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[3]/span[text() = "Начинки"]'

    # Кликабельный логотип в шапке сайта
    logo = By.XPATH, '/html/body/div/div/header/nav/div[@class="AppHeader_header__logo__2D0X2"]'