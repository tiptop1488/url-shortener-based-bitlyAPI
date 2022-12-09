# url shortener based bitlyAPI

Скрипт для создания коротких ссылок и подсчета переходов по ним.

## установка

Для запуска потребуется Python 3 и библиотеки перечисленные
в файле `requirements.txt.` Создайте файл `.env` и присвойте свой токен в `BITLY_TOKEN`. 

## запуск

Запустите скрипт с ссылкой в качестве аргумента. Если это обычная ссылка,
в ответ придет короткая ссылка которая ведет на тот же адрес. 
Если отправленна короткая ссылка придет кол-во кликов по ней.

  ```
PS C:\url _shortener_bitlyAPI> python .\main.py https://www.google.com/
usage: https://bit.ly/3iMQXoe
PS C:\url _shortener_bitlyAPI> python .\main.py https://bit.ly/3iMQXoe
usage: 1
  ```

## как работает скрипт

`shorten_link` принимает два обязательных аргумента токен и ссылку
которую требуется сократить. Возвращает короткую ссылку.

`count_clicks` принимает два обязательных аргумента, токен и укороченную ссылку.
Возвращает колличество кликов по ссылке.

`is_bitlink` принимает два обязательных аргумента токен и ссылку.
Возвращает `True` если ссылка укорочена, и `False` если ссылка обычная.