from flask import render_template

from keywords import app
from keywords.forms import URLForm


@app.route("/", methods=["GET", "POST"])
def url():
    form = URLForm()
    return render_template("url_form.html", title="URL Form", form=form)
