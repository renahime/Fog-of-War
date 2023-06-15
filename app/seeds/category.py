from app.models import db, Category, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_category():
    movies = Category(
        name='Movies')
    literature = Category(
        name='Literature')
    anime_manga = Category(
        name='Anime Manga and Visual Novels')
    videogames = Category(
        name='Video Games')
    tv_shows = Category(
        name='TV Shows')
    history = Category(
        name='History')
    religion_philosophy = Category(
        name='Religion and Philosophy')
    food = Category(
        name='Food')
    pet = Category(
        name='Pets')

    db.session.add(movies)
    db.session.add(literature)
    db.session.add(anime_manga)
    db.session.add(videogames)
    db.session.add(tv_shows)
    db.session.add(history)
    db.session.add(religion_philosophy)
    db.session.add(food)
    db.session.add(pet)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_category():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.categories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM categories"))

    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.thread_categories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM thread_categories"))

    db.session.commit()
