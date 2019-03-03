import os
from urllib.request import urlretrieve

import pytest


@pytest.fixture
def html_content():
    base_dir = os.path.dirname(__file__)
    html_file = os.path.join(base_dir, "data", "python.org.html")
    if not os.path.exists(html_file):
        urlretrieve("https://www.python.org", html_file)
    with open(html_file, "r") as file:
        return file.read()
