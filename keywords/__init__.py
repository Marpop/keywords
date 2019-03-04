from flask import Flask

app = Flask(__name__)

import keywords.views  # noqa: E402 F401 isort:skip
