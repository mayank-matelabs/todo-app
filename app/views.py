from flask import render_template, flash
from flask_appbuilder import expose, BaseView, has_access
from flask_appbuilder import SimpleFormView, ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_babel import lazy_gettext as _
from .forms import MyForm
from app import appbuilder, db
from .models import Todo

class Home(BaseView):

    default_view = 'home'

    @expose('/')
    @has_access
    def home(self):
        return self.render_template('home.html')

    @expose('/about/')
    @has_access
    def about(self):
        return self.render_template('about.html')

class AddTodoModelView(ModelView):
    datamodel = SQLAInterface(Todo)

    list_columns = ['id','name','description','due date']

    show_fieldsets = [
                        (
                            'Todos',
                            {'fields':['id','name','description','timestamp'],'expanded':True}
                        ),
                     ]

# class AddTodo(SimpleFormView, ModelView):
#     form = MyForm
#     form_title = 'Add Todo'
#     message = 'Todo Added !'

#     def form_get(self, form):
#         form.todo.data = ''

#     def form_post(self, form):
#         # post process form

#         flash(self.message, 'info')


# appbuilder.add_view(AddTodo, "AddTodo", icon="fa-group", label=_('Add Todo'),
#                      category="Add Todo", category_icon="fa-cogs")

db.create_all()
appbuilder.add_view(AddTodoModelView,
                    "Todos",
                    category = "Todos")            
appbuilder.add_view(Home(), "Home", category='Home')
# Use add link instead there is no need to create MyView twice.
appbuilder.add_link("About", href='/home/about', category='About')

"""
    Application wide 404 error handler
"""

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404


db.create_all()
