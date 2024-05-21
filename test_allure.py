import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_atributs.locators import AuthorizationLocators

AuthPage_url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=054109ff-a399-4999-a5fa-5953cf11d093&theme&auth_type'
Category = 'UI'
Story = 'Набор тестов, для проверки ссылок, в иконках социальных сетей.'

@pytest.fixture(autouse=True,scope='session') # scope session запустит код фикстуры один раз за весь прогон
def driver():
   driver = webdriver.Firefox()
   driver.implicitly_wait(10)
   yield driver
   driver.quit()
@pytest.fixture(autouse=True,scope='function') # Отработает в начале каждого теста
def get_url(driver):
   with allure.step('Драйвер получает адрес страницы авторизации'):
      driver.get(AuthPage_url)

@allure.epic(Category)
@allure.story(Story)
@allure.title("Иконка Вконтакте")
@allure.severity(allure.severity_level.MINOR)
def test_vk_icon(driver):
   '''Тест-кейс TRT-028. Проверка функциональности ссылки объекта: иконка ВКонтакте'''
   with allure.step('Переход по ссылке'):
      driver.find_element(*AuthorizationLocators.VK_ICON).click()
      assert driver.find_element(By.XPATH, '//div[contains(@class, "vkc__ServiceAvatar__serviceAvatar")]')
@allure.epic(Category)
@allure.story(Story)
@allure.title("Иконка Одноклассники")
@allure.severity(allure.severity_level.MINOR)
def test_ok_icon(driver):
   '''Тест-кейс TRT-029. Проверка функциональности ссылки объекта: иконка Одноклассники'''
   with allure.step('Переход по ссылке'):
      driver.find_element(*AuthorizationLocators.OK_ICON).click()
      assert driver.find_element(By.XPATH, '//*[@id="widget-el"]/div[2]/div/div/div[4]')
@allure.epic(Category)
@allure.story(Story)
@allure.title("Иконка Почта Mail.ru")
@allure.severity(allure.severity_level.NORMAL)
def test_mail_icon(driver):
   '''Тест-кейс TRT-030. Проверка функциональности ссылки объекта: иконка почты Mail.ru'''
   with allure.step('Переход по ссылке'):
      driver.find_element(*AuthorizationLocators.MAIL_ICON).click()
      assert driver.find_element(By.XPATH, '//*[@id="wrp"]/div[1]/span')
@allure.epic(Category)
@allure.story(Story)
@allure.title("Иконка Яндекс ID")
@allure.severity(allure.severity_level.NORMAL)
def test_yandx_icon(driver):
   '''Тест-кейс TRT-031. Проверка функциональности ссылки объекта: иконка яндекс ID'''
   with allure.step('Переход по ссылке'):
      driver.find_element(*AuthorizationLocators.YA_ICON).click()
      assert driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/a')

# python -m pytest --driver Firefox --driver-path C:{driver path}\geckodriver.exe tests\test_allure.py --alluredir allure-results
# allure serve {file name} отобразить отчёт после завершения тестов