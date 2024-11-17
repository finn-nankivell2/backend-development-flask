from faker import Faker
from datetime import timezone
import os
import shutil

from flask import Blueprint

from app import db
from app.models import User, Post

blueprint = Blueprint("cli", __name__, cli_group="custom")


@blueprint.cli.command("seed")
def seed_db():
    """Seed the database with placeholder data"""

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
            "author": User.query.get(faker.random_int(min=1, max=num_users)),
        }

        post = Post()
        post.from_dict(data)
        db.session.add(user)

    db.session.commit()


@blueprint.cli.command("migrate_fresh")
def migrate_fresh():
    """Delete migrations folder / database and run migrations from scratch"""

    from flask import current_app as app

    app.logger.info("Running migrations from scratch")
    if os.path.exists("migrations/"):
        app.logger.info("- Removing migrations directory")
        shutil.rmtree("migrations")

    if os.path.exists("storage/app.db"):
        app.logger.info("- Removing migrations directory")
        os.remove("storage/app.db")

    app.logger.info("- Running 'flask db init'")
    os.system("flask db init")
    app.logger.info("- Running 'flask db migrate'")
    os.system("flask db migrate")
    app.logger.info("- Running 'flask db upgrade'")
    os.system("flask db upgrade")


@blueprint.cli.command("migrate_fresh_seed")
def migrate_fresh_and_seed():
    """Migrate fresh and seed the database"""

    os.system("flask custom migrate_fresh")
    os.system("flask custom seed")
