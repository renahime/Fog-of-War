from app.models import db, User, environment, SCHEMA, Post, Thread
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_boys_posts():
    user2 = User.query.get(2)
    user3 = User.query.get(3)
    thread1 = Thread.query.get(21)
    thread2 = Thread.query.get(22)
    thread3 = Thread.query.get(23)
    thread4 = Thread.query.get(24)
    thread5 = Thread.query.get(25)

    post1= Post(
        subject='RE: Speculating at the end of the Question Arcs',
        text="""<p>I have nothing to add but huge plus for 20th Century Boys posts!!!! Really good write up.</p>
              """,
        user=user2,
        thread=thread1
    )
    db.session.add(post1)

    post2 = Post(
        subject='RE: Speculating at the end of the Question Arcs',
        text="""<p>I'm saving this for my next re-read!</p>""",
        user=user3,
        thread=thread1
    )
    db.session.add(post2)


    post4= Post(
        subject="RE: Hey guys, just finished the four question arcs",
        text="""<p>3 months late but I only finished the series the other day

The twist was that the kid who has supposedly died before dissecting the carp (Katsumata) didn't actually die - he was another one of Fukubei's friends that Fukubei essentially abused. I assume that after he told Katsumata that he had died, that Katsumata had to play the part of a dead kid by not interacting with anyone and wearing a mask similar to Sadakiyo so that no one would notice he was gone. So the majority of the time that we saw a kid in a mask with Fukubei, it was actually Katsumata (as Sadakiyo had already been kicked to the curb by Fukubei for messing up the bedsheet ghost and almost exposing him for not going to the expo)

This also explains that the ghost story that the kids had been talking about (the kid dies before the carp dissecting, then a dissected carp showed up in the science lab mysteriously), as Katsumata just going into the lab after hours and dissecting the carp, as he had missed it because he was 'playing dead'


.</p>
              """,
        user=user3,
        thread=thread2
    )

    db.session.add(post4)

    post5 = Post(
        subject="RE: Umineko - I figured it out. (first time)",
        text="""<p>Fukube died in 1971 during the failed resurrection. Katsumata took over as the friend ever since. He took on the Fukube persona exactly. On Bloody New Years Eve Katsumata was the one who took the photo and went to the rooftop with Kenji. When “Fukube”(katsumata) says “it's not Sadakio” as he falls off the roof. he is acting and playing tricks like he always does. The one wearing the mask at that moment was another member of the Friends that katsumata asked to play the part for him temporarily. “Fukube” (Katsumata) survived the fall using his tricks, then changed clothes to hop on top of the robot to confront Kenji. In vol 12 we clearly see the friend get shot and killed by Yamane. This was another one of the friend's tricks. Katsumata did the resurrection trick right this time, something Fukube was not able to do. When Friend (katsumata) became president of the world he abandoned the Fukube persona and reverted to his own original ideals because he already achieved what Fukube wanted, to become president of the world. Thus began the final act of the series. Katsumata died for real at the end of 20th century boys. Kenji played his song for the broken and dying katsumata because the wrote it together as kids. Long story short, The Friend indeed always was Katsumata. Hopefully this provides an explanation for the final chapter of 21st century boys.
</p>""",
        user=user2,
        thread=thread3
    )

    db.session.add(post5)

    post6 = Post(
        subject="RE: Episode 5 completed! Here are my theories and attempts at solving the mystery!",
        text="""<p>I can’t believe Magenta Magenta got stuck in that river, that’s when the series really surprised me.</p>
""",
        user=user2,
        thread=thread4,
    )

    db.session.add(post6)

    post7 = Post(
        subject="RE: Umineko master theory based on Question arcs (Spoilers for parts 1-4)",
        text="""<p>Well I think it was katsumata just that he had plastic surgery as a kid somehow</p>
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
def undo_boys_posts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM posts"))

    db.session.commit()
