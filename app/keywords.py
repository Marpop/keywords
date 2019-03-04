import requests
from bs4 import BeautifulSoup


def get_page_source(url):
    page = requests.get(url)
    return page.text


def get_keywords(page_content):
    soup = BeautifulSoup(page_content, "html.parser")
    meta_keywords_tag = soup.find(name="meta", attrs={"name": "keywords"})
    keywords_string = meta_keywords_tag.attrs.get("content")
    keywords_list = keywords_string.split()
    return set(keywords_list)


def count_word_on_page(page_content, word):
    soup = BeautifulSoup(page_content.lower(), "html.parser")
    words = soup.find_all(text=lambda text: text and word in text)
    return len(words)
