from app import db

import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.orm import Mapped


from datetime import datetime, timezone
from .User import User


class Post(db.Model):
    id: Mapped[int] = so.mapped_column(primary_key=True)
    body: Mapped[str] = so.mapped_column(sa.String(255))
    timestamp: Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))

    user_id: Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)
    author: Mapped[User] = so.relationship(back_populates="posts")

    def from_dict(self, data):
        for field in filter(lambda x: x in ("body", "author", "timestamp"), data):
            setattr(self, field, data[field])

    def to_dict(self, data, include_email=False):
        data = {
            "id": self.id,
            "body": self.body,
            "timestamp": self.timestamp.isoformat() + "Z",
            "author": self.author.username
        }
        return data


from .User import User
