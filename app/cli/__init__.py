from faker import Faker
from datetime import timezone

from flask import Blueprint

blueprint = Blueprint("cli", __name__, cli_group=None)

from app import db
from app.models import User, Post


@blueprint.cli.command("seed")
def seed_db():
    faker = Faker("en_IE")
    num_users = 10
    num_posts = 100

    for _ in range(num_users):
        data = {
            "username": faker.user_name(),
            "email": faker.email(),
            "password": "secret",
            "about_me": faker.text(),
        }

        user = User()
        user.from_dict(data, new_user=True)
        db.session.add(user)

    for _ in range(num_posts):
        data = {
            "body": faker.text(),
            "timestamp": faker.date_time_this_year(tzinfo=timezone.utc),
            "author": User.query.get(faker.random_int(min=1, max=num_users))
        }

        post = Post()
        post.from_dict(data)
        db.session.add(user)

    db.session.commit()
