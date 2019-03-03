import os

import pytest


@pytest.fixture
def python_html():
    base_dir = os.path.dirname(__file__)
    python_org = os.path.join(base_dir, "data", "python.org.html")
    with open(python_org, "r") as html_file:
        return html_file.read()
