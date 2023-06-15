from app.models import db, Category, environment, SCHEMA, Thread, Post
from sqlalchemy.sql import text

# Adds a demo user, you can add other users here if you want
def seed_threads():
    category = Category.query.filter_by(name='Anime, Manga, Visual Novels').first()
    thread1= Thread(
        subject="My theory about Jessica's true origins + detailed analysis"
    )
    thread2=
    thread3=
    thread4=
    thread5=

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_category():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.threads RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM threads"))

    db.session.commit()
