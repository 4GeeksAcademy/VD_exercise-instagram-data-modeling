import os
import sys,enum
from sqlalchemy import Column, ForeignKey, Integer, String,Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class MediaType(enum.Enum):
    jpg="jpg"
    mp4="mp4"
    png="png"

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    # id = Column(Enum(MediaType), primary_key=True)
    id_follower = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id_user'))
    user_to_id = Column(Integer, ForeignKey('user.id_user'))

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_user = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    followers = relationship('Follower', backref='user', lazy= True)
    comment= relationship('Comment', backref='user', lazy= True)
    post= relationship('Post', backref='user', lazy= True)

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_comment = Column(Integer, primary_key=True)
    comment_text = Column(String(50), unique=True, nullable=False)
    author_id = Column(Integer, ForeignKey('user.id_user'))
    post_id = Column(Integer, ForeignKey('post.id_post'))

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_post = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id_user'))
    post= relationship('Media', backref='post', lazy= True)

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_media = Column(Integer, primary_key=True)
    type = Column(Enum(MediaType)) 
    url = Column(String(50), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id_post'))  
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
