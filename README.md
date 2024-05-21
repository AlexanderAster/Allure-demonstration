# Allure-demonstration
Мой уровень владения Allure report.
Данный проект подразумевает простую демонстрацию внедрения allure report в небольшие тесты. Я старался использовать как можно больше allure меток,которые мне известны. 
1. Объект тестирования - авторизационная форма веб-ресурса Ростелеком [https://b2c.passport.rt.ru]
2. Фреймворк тестирования - Pytest на базе библиотеки веб-тестирования Selenium WebDriver (драйвер Firefox geckodriver V 0.34.0-win64)
3. Интерпретатор - VS code.
4. Файл test_allure.py содержит UI тесты,проверяющие функциональность ссылок.
5. Папка Page_atributs содержит файл locators.py со списком элементов страницы.
6. Папка allure-report сгенерированный посредством allure generate для передачи отчёт. (Скачать и запустить для просмотра отчёта)
7. geckodriver.exe сам драйвер браузера,используемый в прогоне. Укажите к нему путь при запуске тест-сьюта
  
Запуск:
1. Команда для консоли ~ {python -m pytest test_allure.py --alluredir allure-results} Если путь к драйверу задан заранее в переменных среды PATH
2. Команда для консоли ~ {python -m pytest --driver Firefox --driver-path C:{driver path}\geckodriver.exe test_allure.py --alluredir allure-results} Полная строка с вручную заданным путём

Отобразить отчёт:
1. Команда для консоли ~ {allure serve} Обратится к сгенерированному в папке отчёту и поднимет локальный сервер с данными (Только после первого запуска)
2. Команда для консоли ~ {allure open allure-report} Открыть скачанный allure-report
3. Или вручную открыть файл index.html из папки allure-report
