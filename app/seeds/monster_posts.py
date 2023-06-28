from app.models import db, User, environment, SCHEMA, Post, Thread
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_monster_posts():
    user2 = User.query.get(2)
    user3 = User.query.get(3)
    thread1 = Thread.query.get(16)
    thread2 = Thread.query.get(17)
    thread3 = Thread.query.get(18)
    thread4 = Thread.query.get(19)
    thread5 = Thread.query.get(20)

    post1= Post(
        subject='RE: Deconstructing Naoki Urasawa’s Monster: a Psychological Study',
        text="""<p>This was a fantastic analysis of the character! If you have anything further to add I would love to hear.</p>
              """,
        user=user2,
        thread=thread1
    )
    db.session.add(post1)

    post2 = Post(
        subject='RE: Speculating at the end of the Question Arcs',
        text="""<p>Necro post, but just wanted to day thanks for writing that, it really helped me connect some dots!!</p>""",
        user=user3,
        thread=thread1
    )
    db.session.add(post2)


    post4= Post(
        subject="RE: Hey guys, just finished the four question arcs",
        text="""<p>The twins’ pasts are all explained in the last 15 or so episodes though.</p>
              """,
        user=user3,
        thread=thread2
    )

    db.session.add(post4)

    post5 = Post(
        subject="RE: Umineko - I figured it out. (first time)",
        text="""<p>The twins’ pasts are all explained in the last 15 or so episodes though</p>""",
        user=user2,
        thread=thread3
    )

    db.session.add(post5)

    post6 = Post(
        subject="RE: Episode 5 completed! Here are my theories and attempts at solving the mystery!",
        text="""<p>I also didn't like monster's ending, i was really furious when tenma saved johan, i mean really what was the point of the whole series if he escaped again. That was a good read, keep up the good stuff.</p>
""",
        user=user2,
        thread=thread4,
    )

    db.session.add(post6)

    post7 = Post(
        subject="RE: Umineko master theory based on Question arcs (Spoilers for parts 1-4)",
        text="""<p>beautifully written. thank you for this! it reminds me why i love monster so much.</p>
""",
        user=user3,
        thread=thread5
    )

    db.session.add(post7)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_monster_posts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM posts"))

    db.session.commit()
