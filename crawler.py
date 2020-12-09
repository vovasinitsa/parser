import requests
import lxml
# pip install requests
# pip install lxml
from bs4 import BeautifulSoup
# pip install beautifulsoup4


def get_html(url):
    html_code_url = requests.get(url)  # Response
    return html_code_url.text  # возращает HTML код


def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    all_objects = soup.find_all('a')
    links = []

    for all_object in all_objects:
        a = all_object.get('href')  # строка
        links.append(a)
    return links


def main():
    url = "https://casinogoodorbad.com/"
    all_links = get_all_links(get_html(url))
    for i in all_links:
        print(i)


if __name__ == '__main__':
    main()
