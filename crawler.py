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
            new_link = 'https://casinogoodorbad.com' + i
            sorted_all_links.append(new_link)
        if i[:27] == 'https://casinogoodorbad.com':
            sorted_all_links.append(i)
    for i in sorted_all_links:  # удаляет дубли
        while sorted_all_links.count(i) > 1:
            sorted_all_links.remove(i)

    for i in sorted_all_links:
        answer_url = requests.get(i)  # получает ответ с каждого url в списке
        print(i, answer_url)

# TODO сохранить список не вошедших данных
# TODO сохранить список адресов не casinogoodorbad.com


if __name__ == '__main__':
    main()
