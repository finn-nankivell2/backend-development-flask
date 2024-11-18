from typing import Optional

import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.orm import Mapped, WriteOnlyMapped

import werkzeug.security

from app import db
from .traits import HasResource


class User(db.Model):
    id: Mapped[int] = so.mapped_column(primary_key=True)
    username: Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    posts: WriteOnlyMapped["Post"] = so.relationship(back_populates="author")

    def set_password(self, password):
        self.password_hash = werkzeug.security.generate_password_hash(password)

    def check_password(self, password):
        return werkzeug.security.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User {}>".format(self.username)

    def from_dict(self, data, new_user=False):
        for field in filter(lambda x: x in ("username", "email"), data):
            setattr(self, field, data[field])

        if new_user and data.get("password"):
            self.set_password(data["password"])

    def to_dict(self, data, include_email=False):
        data = {
            "id": self.id,
            "username": self.username,
            "post_count": self.posts_count(),
        }
        if include_email:
            data["email"] = self.email

        return data


from .Post import Post
