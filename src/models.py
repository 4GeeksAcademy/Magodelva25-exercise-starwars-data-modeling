import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users (Base):
    __tablename__='users'
    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    name = Column(String, ForeignKey('user.name'))
    active = Column(String, ForeignKey('user.active'))

class User (Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    first_name = Column(String(32))
    last_name = Column(String(32))
    email = Column(String(32))
    password = Column(String(16))
    creation = Column(Integer)
    fav_list = Column(String)
    is_active = Column(String)
    user = relationship(Users)

class Fav_Planets (Base):
    __tablename__='fav-planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    user = relationship(User)

class Planets(Base):
    __tablename__='planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    population = Column(Integer)
    gravity = Column(Integer)
    activity = Column(String(320))
    planet = relationship(Fav_Planets)

class Fav_Characters (Base):
    __tablename__='fav-characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    user = relationship(User)

class Characters(Base):
    __tablename__='characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    type = Column(String)
    age = Column(Integer)
    heigth = Column(Integer)
    affiliation = Column(String)
    character = relationship(Fav_Characters)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
