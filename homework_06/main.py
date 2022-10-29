from flask import Flask, request, render_template, url_for, redirect
from flask_migrate import Migrate
from os import getenv
import config

from models import dbase, DemoItem

from forms import CreateItemForm

app = Flask(__name__)


CONFIG_OBJECT = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")

dbase.app = app
dbase.init_app(app)
migrate = Migrate(app, dbase, compare_type=True)


@app.route("/", endpoint="index_page")
def index_page():
    return render_template("index.html")


@app.route("/about/", endpoint="about_page")
def about_page():
    return render_template("about.html")

@app.route("/add/", methods=["GET", "POST"], endpoint="add_page")
def add_item():
    form = CreateItemForm()

    if request.method == "GET":
        return render_template("add.html", form=form)

    if not form.validate_on_submit():
        return render_template("add.html", form=form), 400

    item_name = form.name.data

    demo_item = DemoItem(name=item_name)
    dbase.session.add(demo_item)
    dbase.session.commit()

    url = url_for("list_page")
    return redirect(url)


@app.route("/list/", endpoint="list_page")
def list_page():
    demo_items = DemoItem.query.order_by(DemoItem.id).all()
    return render_template("list.html", demoitems=demo_items)


@app.route(
    "/<int:demoitem_id>/",
    methods=["GET", "DELETE"],
    endpoint="delete_page",
)
def get_item_by_id(demoitem_id: int):

    demo_item: DemoItem = DemoItem.query.get_or_404(
        demoitem_id,
        f"Item with ID #{demoitem_id} not found!",
    )

    dbase.session.delete(demo_item)
    dbase.session.commit()

    url = url_for("list_page")
    return redirect(url)


if __name__ == "__main__":
    app.run(debug=True)
