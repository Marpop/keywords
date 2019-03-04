import os

from flask import Flask

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

import keywords.views  # noqa: E402 F401 isort:skip
