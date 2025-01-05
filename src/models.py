import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users_list (Base):
    __tablename__='users-list'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_name = Column(String, ForeignKey('user.name'))
    user_active = Column(String, ForeignKey('user.active'))

class User (Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    first_name = Column(String(32))
    last_name = Column(String(32))
    email = Column(String(32))
    password = Column(String)
    creation = Column(Integer)
    fav_list = Column(String)
    active = Column(String)
    user = relationship(Users_list)

class Fav_list (Base):
    __tablename__='fav-list'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    item_id = Column(Integer, ForeignKey('items.id'))
    user = relationship(User)

class Items(Base):
    __tablename__='items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    description = Column(String)
    user = relationship(Fav_list)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
