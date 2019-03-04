from flask import render_template

from keywords import app
from keywords.counting import get_counting
from keywords.forms import URLForm


@app.route("/", methods=["GET", "POST"])
def url():
    form = URLForm()
    if form.validate_on_submit():
        url = form.data.get("url")
        result = get_counting(url)
        return render_template("url_result.html", result=result)
    return render_template("url_form.html", title="URL Form", form=form)
