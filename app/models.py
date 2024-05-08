from typing import Optional 
from app import db
import sqlalchemy as sa
from sqlalchemy.orm import mapped_column, Mapped

class User(db.Model):
    id: Mapped[int]  = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: Mapped[str] = mapped_column(sa.String(120), index=True,
                                             unique=True)
    password_hash: Mapped[Optional[str]] = mapped_column(sa.String(256))



class Podcast(db.Model):
    id: Mapped[str] = mapped_column(sa.String(20), primary_key=True)