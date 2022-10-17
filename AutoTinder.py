# Бот для автоматизации Tinder
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import random
from time import sleep, time

from selenium.common.exceptions import ElementClickInterceptedException

# xPath для кнопок "Лайк" и "Дизлайк"       
LIKE_BUTTON_XPATH = '//button//span[text()="Лайк"]'
DISLIKE_BUTTON_XPATH = '//button//span[text()="Нет"]'


# Класс со всеми методами
class TinderBot:
    # Инициализация webdriver Chrome
    def __init__(self):
        chrome_options = Options()

        # Заменяем пользовательский агент так, что tinder.com не узнает, что это автоматизированный скрипт
        chrome_options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.'
            '4044.113 Safari/537.36'
        )
        
        #'/C/Program Files/Google/Chrome/Application/chrome.exe' --remote-debugging-port=9222 --user-data-dir="/D/IT/Python/Projects/AutoTinder/chr"
        chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")

        self.driver = webdriver.Chrome(
            executable_path="C:\\chromedriver.exe",  # Путь к webdriver
            chrome_options=chrome_options
        )
        
        print("Webdriver is initialized")
    
    
    # Запуск бота
    def start(self):
        self.driver.get('https://tinder.com')
        print("Tinder is runned")
        sleep(5)


    # Свайпает вправо (НРАВИТСЯ)
    def swipe_right(self):
        btn_like = self.driver.find_element(by='xpath', value=LIKE_BUTTON_XPATH)
        self.driver.execute_script("arguments[0].click();", btn_like)


    # Свайпает влево (НЕ НРАВИТСЯ)
    def swipe_left(self):
        btn_dislike = self.driver.find_element_by_xpath(DISLIKE_BUTTON_XPATH)
        btn_dislike.click()

    
    # Рандомно засыпает на 1-3 секунды, чтобы tinder не определил, что это бот
    def rand_sleep(self):
        sleep_sec = random.uniform(1, 3)
        print('Sleeping for {} seconds'.format(str(sleep_sec)))
        sleep(sleep_sec)


    # Авто-свайпинг
    def auto_swipe(self):
        likes, dislikes = 0, 0  # Счетчик свайпов
        filename = time()       # Имя файла статистики получается из времени
        while True:
            self.rand_sleep()
            try:
                rand = random.random()
                #if rand < .80:  # Вероятности свайпов вправо (80) и влево (20)
                self.swipe_right()
                likes += 1
                print('Swiped Right, Count {}'.format(likes))
                #else:
                #    self.swipe_left()
                #    dislikes += 1
                #    print('Swiped Left, Count {}'.format(dislikes))
                # Записываем статистику в файл
                with open(str(filename).split('.')[0] + '.txt', 'w+') as stats:
                    stats.writelines('Swiped Right. Count {} \n'.format(likes))
                    stats.writelines('Swiped Left Count {}'.format(dislikes))
            except ElementClickInterceptedException as e:
                # Обработка, если на экране появляется какое-то неожиданное окно
                # Обновляем страницу и перезапускаем бот
                self.driver.refresh()
                sleep(5)
                self.auto_swipe()
            except Exception as e:
                print(str(e))
                return -1


tinder_bot = TinderBot()
tinder_bot.start()
tinder_bot.auto_swipe()