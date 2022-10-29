from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CreateItemForm(FlaskForm):
    name = StringField(
        label="Item name:",
        name="item-name",
        validators=[
            DataRequired(),
            Length(min=5),
        ],
    )
