from app.keywords import count_word_on_page, get_keywords, get_page_source


def test_get_page():
    url = "https://www.python.org"
    assert "head" in get_page_source(url)
    assert "body" in get_page_source(url)


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


def test_count_word_on_page(html_content):
    assert count_word_on_page(html_content, "python") == 63
    assert count_word_on_page(html_content, "software") == 6
    assert count_word_on_page(html_content, "download") == 5
    assert count_word_on_page(html_content, "object") == 1
