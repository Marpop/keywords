from urllib.request import urlopen

from bs4 import BeautifulSoup


def get_page_content(url):
    page = urlopen(url)
    return str(page.read())


def get_keywords(page_content):
    soup = BeautifulSoup(page_content, "html.parser")
    meta_keywords_tag = soup.find(name="meta", attrs={"name": "keywords"})
    keywords_string = meta_keywords_tag.attrs.get("content")
    keywords_list = keywords_string.split()
    return set(keywords_list)
