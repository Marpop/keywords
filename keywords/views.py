from flask import render_template

from keywords import app, counting
from keywords.forms import URLForm


@app.route("/", methods=["GET", "POST"])
def url():
    form = URLForm()
    if form.validate_on_submit():
        url = form.data.get("url")
        page_source = counting.get_page_source(url)
        keywords = counting.get_keywords(page_source)
        result = counting.count_keywords(page_source, keywords)
        return render_template("url_result.html", result=result)
    return render_template("url_form.html", title="URL Form", form=form)
