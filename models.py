from app import db
from datetime import datetime
from flask_security import UserMixin, RoleMixin


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    for_pub = db.Column(db.Boolean, default=False)
    pub_date = db.Column(db.DateTime, default=datetime.now())
    news_header = db.Column(db.String(256))
    news_href = db.Column(db.String(256), unique=True)

    def __init__(self, *args, **kwargs):
        super(News, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<News id: {}, header: {}>'.format(self.id, self.news_header)


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    for_pub = db.Column(db.Boolean, default=False)
    pub_date = db.Column(db.DateTime, default=datetime.now())
    event_header = db.Column(db.String(256))
    event_text = db.Column(db.String(256))
    event_href = db.Column(db.String(256), unique=True)

    def __init__(self, *args, **kwargs):
        super(Events, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Events id: {}, header: {}>'.format(self.id, self.event_header)


"""
Flask Security
"""
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
                       )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(255))
