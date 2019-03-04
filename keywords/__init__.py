import os

from flask import Flask

from dotenv import load_dotenv
from flask_bootstrap import Bootstrap

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
bootstrap = Bootstrap(app)

import keywords.views  # noqa: E402 F401 isort:skip
