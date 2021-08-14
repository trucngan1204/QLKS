from flask_admin import BaseView, expose
from flask import redirect
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from flask_login import UserMixin, current_user,logout_user
from enum import Enum as UserEnum
from app1 import db

class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True,autoincrement=True )
    name = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    # receipts = relationship('Receipt', backref='customer', lazy=True)


class Customer(db.Model):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    cmnd = Column(String(50))
    address = Column(String(255))
    # room = relationship('Room', backref='room', lazy=True)
    # service = relationship('Service',backref='Service', lazy=True )

    def __str__(self):
        return self.name

class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    image = Column(String(255), nullable=True)
    price = Column(Float, default=0)
    room = relationship('Room',backref='category', lazy=True)


class Room(db.Model):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    image = Column(String(255), nullable=True)
    description = Column(String(255))
    price = Column(Float, default=0)

    # room = relationship('Room', backref='Category', lazy = True)
    category_id = Column(Integer, ForeignKey(Category.id),
                         nullable=False)

    def __str__(self):
        return self.name


class Receptionist(db.Model):
    __tablename__ = 'receptionist'

    id = Column(Integer,primary_key=True, autoincrement=True)


class Accountant(db.Model):
    __tablename__ = 'accountant'

    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


class Service(db.Model):
    __tablename__ = 'service'

    id = Column(Integer,primary_key=True, autoincrement=True)
    image = Column(String(255), nullable=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    # customer_id = Column(Integer, ForeignKey(Customer.id),
    #                      nullable=True)


class Statistical(db.Model):
    __tablename__ = 'statistical'

    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


class Invoice(db.Model):
    __tablename__ = 'invoice'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)


class LogoutView(BaseView):
    @expose("/")
    def index(self):
        logout_user()

        return redirect("/admin")

    def is_accessible(self):
        return current_user.is_authenticated

if __name__ == '__main__':
    db.create_all()
