import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    clave = Column(String(250), nullable=False)

class Personaje(Base):
    __tablename__ = 'personaje'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    personaje_id = Column(Integer, primary_key=True)
    personaje_name = Column(String(250), nullable=False)

class Location(Base):
    __tablename__ = 'location'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    location_id = Column(Integer, primary_key=True)
    location_name = Column(String(250), nullable=False)

class Personaje_Favorito(Base):
    __tablename__ = 'personaje_favorito'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    personaje_id = Column(Integer, ForeignKey('personaje.id'))
    personaje = relationship(Personaje)

class Location_Favorito(Base):
    __tablename__ = 'location_favorito'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    location_id = Column(Integer, ForeignKey('location.id'))
    location = relationship(Location)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
