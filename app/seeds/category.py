from app.models import db, Category, environment, SCHEMA
from sqlalchemy.sql import text
from app.models import SubCategory


# Adds a demo user, you can add other users here if you want
def seed_category():
    literature = Category(
        name='Literature')
    anime_manga = Category(
        name='Anime Manga and VNs')
    videogames = Category(
        name='Video Games')

    db.session.add(literature)
    db.session.add(anime_manga)
    db.session.add(videogames)

    book1 = SubCategory(
        name='House of Leaves',
        categories=literature
    )

    book2 = SubCategory(
        name='Sharp Objects',
        categories=literature
    )

    book5 = SubCategory(
        name='And Then There Were None',
        categories=literature
    )

    book3 = SubCategory(
        name='The Murder of Roger Ackroyd',
        categories=literature
    )

    book4 = SubCategory(
        name='Seven and a Half Deaths of Evelyn Hardcastle',
        categories=literature
    )

    videogame1 = SubCategory(
        name='Dangan Ronpa',
        categories=videogames
    )
    videogame2 = SubCategory(
        name='Zero Escape',
        categories=videogames
    )
    videogame3 = SubCategory(
        name='Return of the Obra Dinn',
        categories=videogames
    )
    videogame4 = SubCategory(
        name='The Case of the Golden Idol',
        categories=videogames
    )
    videogame5 = SubCategory(
        name='13 Sentinels',
        categories=videogames
    )

    anime1 = SubCategory(
        name='When the Cicadas Cry',
        categories=anime_manga
    )
    anime2 = SubCategory(
        name='When the Seagulls Cry',
        categories=anime_manga
    )
    anime3 = SubCategory(
        name='Monster',
        categories=anime_manga
    )
    anime4 = SubCategory(
        name='20th Century Boys',
        categories=anime_manga
    )
    anime5 = SubCategory(
        name='Uzumaki',
        categories=anime_manga
    )


    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    db.session.add(book4)
    db.session.add(book5)
    db.session.add(videogame1)
    db.session.add(videogame2)
    db.session.add(videogame3)
    db.session.add(videogame4)
    db.session.add(videogame5)
    db.session.add(anime1)
    db.session.add(anime2)
    db.session.add(anime3)
    db.session.add(anime4)
    db.session.add(anime5)





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

    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.thread_sub_categories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM thread_sub_categories"))

    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.subcategories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM subcategories"))

    db.session.commit()
