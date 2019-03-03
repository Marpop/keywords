from urllib.request import urlopen


def get_page_content(url):
    page = urlopen(url)
    return str(page.read())
