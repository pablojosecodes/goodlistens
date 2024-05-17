from typing import Optional 
from app import db, login
import sqlalchemy as sa

from hashlib import md5

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime



from sqlalchemy.orm import mapped_column, Mapped, WriteOnlyMapped, relationship
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

followers = sa.Table(
    'followers',
    db.metadata,
    sa.Column('follower_id', sa.Integer, sa.ForeignKey('user.id'),
              primary_key=True),
    sa.Column('followed_id', sa.Integer, sa.ForeignKey('user.id'),
              primary_key=True)
)



class User(UserMixin, db.Model):
    id: Mapped[int]  = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: Mapped[str] = mapped_column(sa.String(120), index=True,
                                             unique=True)
    password_hash: Mapped[Optional[str]] = mapped_column(sa.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)
     
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    following: WriteOnlyMapped['User'] = relationship(
        secondary=followers, primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        back_populates='followers')
    followers: WriteOnlyMapped['User'] = relationship(
        secondary=followers, primaryjoin=(followers.c.followed_id == id),
        secondaryjoin=(followers.c.follower_id == id),
        back_populates='following')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'

    def follow(self, user):
        if not self.is_following(user):
            self.following.add(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.following.remove(user)

    def is_following(self, user):
        query = self.following.select().where(User.id == user.id)
        return db.session.scalar(query) is not None

    def followers_count(self):
        query = sa.select(sa.func.count()).select_from(
            self.followers.select().subquery())
        return db.session.scalar(query)

    def following_count(self):
        query = sa.select(sa.func.count()).select_from(
            self.following.select().subquery())
        return db.session.scalar(query)
    


class Podcast(db.Model):
    id: Mapped[str] = mapped_column(sa.String(100), primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(sa.String(100))
    image: Mapped[str] = mapped_column(sa.String(1000))
    rss: Mapped[str] = mapped_column(sa.String(100))
    description: Mapped[str] = mapped_column(sa.String(1000))
    website: Mapped[str] = mapped_column(sa.String(1000))
    
    def __repr__(self):
        return '<Podcast {}>'.format(self.name)

# class Episode(db.Model):
#     # podcast: 
#     id: Mapped[str] = mapped_column(sa.String(20), primary_key=True, unique=True)
#     date: Mapped[DateTime]
#     title: Mapped[str] = mapped_column(sa.String(100))
#     image: Mapped[str] = mapped_column(sa.String(1000), nullable=True)
#     duration: Mapped[int] = mapped_column(sa.Integer)
#     description: Mapped[str] = mapped_column(sa.String(1000), nullable=True)
#     date = mapped_column(sa.DateTime)
#     podcast_id = db.Column(sa.String(100), sa.ForeignKey('podcast.id'))


class Episode(db.Model):
    __tablename__ = 'episode'

    id = Column(String, primary_key=True)
    date = Column(DateTime)
    title = Column(String)
    image = Column(String)
    duration = Column(Integer)
    description = Column(String)
    podcast_id = Column(String, ForeignKey('podcast.id'))

    def __init__(self, id, date, title, image, duration, description, podcast_id):
        self.id = id
        self.date = date
        self.title = title
        self.image = image
        self.duration = duration
        self.description = description
        self.podcast_id = podcast_id

    def __repr__(self):
        return f"<Episode(id='{self.id}', title='{self.title}')>"



@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))


