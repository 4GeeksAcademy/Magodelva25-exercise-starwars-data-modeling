import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users_list (Base):
    __tablename__='users-list'
    user_id = Column(Integer, ForeignKey(''))
    user_name = Column(String, ForeignKey(''))
    user_active = Column(String, nulleable=False)

class User (Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nulleable=False)
    first_name = Column(String(32))
    last_name = Column(String(32))
    email = Column(String(32), nulleable=False)
    password = Column(String, nulleable=False)
    creation = Column(Integer)
    fav_list = Column(String)
    active = Column(String, nulleable=False)

class Fav_list (Base):
    __tablename__='fav-list'
    user_id = Column(Integer)
    item_id = Column(Integer)
    item_name = Column(String)
    item_type = Column(String)
    item_description = Column(String)

class Planets(Base):
    __tablename__='planets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    description = Column(String)

class Characters(Base):
    __tablename__='planets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    description = Column(String)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
