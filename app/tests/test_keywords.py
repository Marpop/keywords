from app.keywords import get_page_content


def test_get_page():
    url = "https://www.python.org"
    assert "head" in get_page_content(url)
    assert "body" in get_page_content(url)
