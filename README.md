# Бот для Tinder

Бот автоматически запускает браузер Chrome. Открывает сайт tinder.com. Свайпает вправо.  
Надо доделать еще, чтобы он автоматически писал сообщения.

Чтобы Tinder не распознал бот, он делает случайные задержки между действиями, 
а при инициализации запускается как обычный браузер (вместо автоматизированного ПО).

Для запуска необходимо предварительно запустить Chrome в режиме отладки:  
'/C/Program Files/Google/Chrome/Application/chrome.exe' --remote-debugging-port=9222 --user-data-dir="/D/IT/Python/Projects/AutoTinder/chr"  
Затем перейти на сайт tinder.com и войти в аккаунт по номеру телефона (сделать это нужно только первый раз).



Написан на Python. Использует ChromeDriver и библиоеку Selenium.

Статус проекта: Разрабатывается.




2022 Evgeny Goryachev  
Gor.Com 