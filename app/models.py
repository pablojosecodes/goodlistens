from typing import Optional 
from app import db, login
import sqlalchemy as sa
from sqlalchemy.orm import mapped_column, Mapped
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


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


class Podcast(db.Model):
    id: Mapped[str] = mapped_column(sa.String(20), primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(sa.String(100))
    image: Mapped[str] = mapped_column(sa.String(200))
    def __repr__(self):
        return '<Podcast {}>'.format(self.name)

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
