from wtforms import Form, StringField
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm


class MyForm(DynamicForm):
    todo = StringField(('Todo Item'),
        description=('Add a Todo!'),
        validators = [DataRequired()], widget=BS3TextFieldWidget())