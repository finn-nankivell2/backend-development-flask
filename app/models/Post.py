from app import db

import sqlalchemy as sa
import sqlalchemy.orm as so

from datetime import datetime, timezone


class Post(db.Model):
    id: so.Mapped[str] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(255))
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))

    user_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey(User.id), index=True)


from app.models.User import User
