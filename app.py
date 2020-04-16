from flask import Flask, redirect, url_for, request,render_template
from flask_security import SQLAlchemyUserDatastore, Security,login_required
from flask_sqlalchemy import SQLAlchemy
from config import Configuration
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user
from flask_admin import AdminIndexView

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import *

class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class AdminView(AdminMixin, ModelView):
    column_default_sort = ('pub_date', True)
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass





admin = Admin(app, 'MSPedit', url='/', index_view=HomeAdminView())
#admin=Admin(app)
admin.add_view(AdminView(News, db.session))
admin.add_view(AdminView(Events, db.session))
#admin.add_view(AdminView(User, db.session))
#admin.add_view(AdminView(Role, db.session))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.route('/')
def index():
    return redirect(url_for('admin.index'))



