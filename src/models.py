import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_year = Column(Integer)
    gender = Column(String(250))
    height = Column(Integer)
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    favorites = relationship ('favorites', backref='characters', lazy = True)

    def to_dict(self):
        return {}
    

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    population = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer)
    favorites = relationship ('favorites', backref='planets', lazy = True)

    def to_dict(self):
        return {}


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    cargo_capacity = Column(Integer)
    consumables = Column(String(250))
    passengers = Column(Integer)
    crew = Column(Integer)
    favorites = relationship ('favorites', backref='vehicles', lazy = True)

    def to_dict(self):
        return {}


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    favorites = Column(String(250))
    users_id = Column(Integer, ForeignKey ('users.id'), nullable=False)
    characters_id = Column(Integer, ForeignKey ('characters.id'), nullable=True)
    planets_id = Column(Integer, ForeignKey ('planets.id'), nullable=True)
    vehicles_id = Column(Integer, ForeignKey ('vehicles.id'), nullable=True)

    def to_dict(self):
        return {}
        

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250))
    favorites = relationship ('favorites', backref='users', lazy = True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
