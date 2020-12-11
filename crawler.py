import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4


URL = "https://casinogoodorbad.com/"


def get_html():
    html_code_url = requests.get(URL)  # Response
    return html_code_url.text  # возращает HTML код


def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    all_objects = soup.find_all('a')
    links = []

    for all_object in all_objects:
        a = all_object.get('href')  # строка
        links.append(a)
        links = sorted(links)

    return links


def main():
    all_links = get_all_links(get_html())
    sorted_all_links = []
    for i in all_links:
        if i[:1] == '/':
            sorted_all_links.append(i)
        if i[:5] == 'https':
            sorted_all_links.append(i)
        else:
            continue
    for i in sorted_all_links:
        print(i)

# TODO сохранить список не вошедших данных
# TODO дополнить адреса
# TODO пропинговать адреса на ответ
# TODO сохранить список адресов не casinogoodorbad.com
# TODO удалить дубли





if __name__ == '__main__':
    main()
