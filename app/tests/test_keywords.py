from app.keywords import get_keywords, get_page_content


def test_get_page():
    url = "https://www.python.org"
    assert "head" in get_page_content(url)
    assert "body" in get_page_content(url)


def test_get_keywords(html_content):
    assert get_keywords(html_content) == {
        "Python",
        "programming",
        "language",
        "object",
        "oriented",
        "web",
        "free",
        "open",
        "source",
        "software",
        "license",
        "documentation",
        "download",
        "community",
    }
