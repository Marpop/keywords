from keywords.counting import (
    count_keywords,
    count_word_on_page,
    get_counting,
    get_keywords,
    get_page_source,
)


def test_get_page():
    url = "https://www.python.org"
    assert "head" in get_page_source(url)
    assert "body" in get_page_source(url)


def test_get_keywords(html_content):
    assert get_keywords(html_content) == [
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
    ]


def test_count_word_on_page(html_content, beautiful_soup):
    assert count_word_on_page(beautiful_soup, "python") == 63
    assert count_word_on_page(beautiful_soup, "software") == 6
    assert count_word_on_page(beautiful_soup, "download") == 5
    assert count_word_on_page(beautiful_soup, "object") == 1


def test_count_keywords(html_content):
    assert count_keywords(html_content, {"python", "download"}) == {
        "python": 63,
        "download": 5,
    }


def test_get_counting(mocker):
    mock_get_page_source = mocker.patch("keywords.counting.get_page_source")
    mock_get_keywords = mocker.patch("keywords.counting.get_keywords")
    mock_count_keywords = mocker.patch("keywords.counting.count_keywords")
    url = "https://www.python.org"
    get_counting(url)
    mock_get_page_source.assert_called_once_with(url)
    mock_get_keywords.assert_called_once()
    mock_count_keywords.assert_called_once()
