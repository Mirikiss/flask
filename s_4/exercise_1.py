import requests
import  threading
import time

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]

def get_url(url, name):
    response = requests.get(url).text
    way = 'C:/Users/limit/Desktop/Flask/s_4/threadingss'
    with open(f'{way}/filesthreading{name}.html', 'w', encoding='UTF-8') as file:
        file.write(response)

if __name__ == '__main__':
    ts = time.time()
    threads = []
    for n, url in enumerate(urls):
        t = threading.Thread(target=get_url, args=(url, n))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()
    tf= time.time()
    print(f'Время работы {ts- tf}')
