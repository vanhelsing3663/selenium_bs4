from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup


class Avito:
    '''В рамках курса Python Linux создана первая программа на пайтоне'''
    OPTIONS = webdriver.ChromeOptions()
    OPTIONS.add_argument(
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36')

    def __init__(self, address: str):
        self.link = None
        self.url = address
        self.driver = webdriver.Chrome(executable_path=r'/home/kir24/chormedriver/chromedriver_linux64/chromedriver')

    def get_the_right_link(self, item_want_find: str):
        """
        :param item_want_find: запрос который подаем в поисковую строку
        :return:
        """
        self.driver.get(self.url)
        print(f'Сайт с которого мы парсим информацию{self.driver.current_url}')
        search = self.driver.find_element(By.XPATH, '//*[@id="downshift-input"]')
        search.click()
        search.send_keys(item_want_find)
        time.sleep(5)
        search.send_keys(Keys.ENTER)
        time.sleep(5)
        print(f'Страница сайта с которого мы извлечем ссылки автомобилей {self.driver.current_url}')
        self.link = self.driver.current_url
        time.sleep(20)

    def parse_links_site(self):
        request = requests.get(self.link)
        bs = BeautifulSoup(request.text, 'html.parser')
        all_links = bs.find_all('a', class_='iva-item-title-py3i_')
        count = 0
        for i in all_links:
            count+=1
            print(f'Ссылка № {count} https://www.avito.ru/{i["href"]}')


address_site = Avito('https://www.avito.ru/')
address_site.get_the_right_link('Легковые машины в Ярославле')
address_site.parse_links_site()
