import requests
import json
import logging
import time

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
    try:
        r = requests.get(url)
        data = json.loads(r.content)
        logging.info("Server is working...")
    except Exception:
        print("Something went wrong. The server is unavailable!")
        logging.warning("The server is down!")
    else:
        logging.info("Сервер доступний. Час на сервері: %s", data['date'])
        logging.info("Запитувана сторінка: : %s", data['current_page'])
        logging.info("Відповідь сервера місти наступні поля:")
        for key in data.keys():
            logging.info("Ключ: %s, Значення: %s", key, data[key])


if __name__ == '__main__':
    tries=1
    while tries <= 4:
        main("http://localhost:8000/health")
        time.sleep(60)
        tries=tries+1
