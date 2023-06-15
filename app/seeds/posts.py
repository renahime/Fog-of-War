from app.models import db, User, environment, SCHEMA, Post, Thread
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_posts():
    user2 = User.query.get(2)
    user3 = User.query.get(3)
    thread1 = Thread.query.get(1)
    thread2 = Thread.query.get(2)
    thread3 = Thread.query.get(3)
    thread4 = Thread.query.get(4)
    thread5 = Thread.query.get(5)

    post1= Post(
        subject='RE: Umineko - My theory about Jessicas true origins + detailed analysis',
        text="""Krauss probably does have some fertility issues given how Natsuhi got herself checked without any doctors seeing any issues with her but that doesn’t mean he’d have to be completely sterile.

              “Natsuhi oba-san is pure and faithful.” - red truthed in the episode 5 ??? Natsuhi also mentions she’s never been with anyone other than her husband and at no point is this contradicted. Red truths can be tricky but I don’t think there’s a satisfactory way to weasel out of this one.

              Married couples having separate beds is actually relatively common in Japan, especially for older couples.

              Going to need some context for the “filthy” quote. Full sentence and when was this?

              Natsuhi supposedly being kind to male servants was explicitly called a rumor rather than fact and we know at the very least it didn’t apply to Kanon. Sounds more like malicious, probably baseless gossip about a bad female boss than anything else.

              Kinzo being the father would make Jessica and Kanon half-siblings. If they were that closely blood-related that probably would have come up more directly as an issue. Also it’s really not in keeping with the sense of wrongness we’re clearly supposed to view Erika’s theory with. “Oh, she’s not sleeping with her father-in-law ANYMORE, how dare you!” doesn’t have much bite to it. In general I don’t think Erika cared much about finding the truth so much as using things she can construct as being “the truth” in order to bully people.


              """,
        user=user2,
        thread=thread1
    )
    db.session.add(post1)

    post2 = Post(
        subject='RE: Umineko - My theory about Jessicas true origins + detailed analysis',
        text="""If Jessica was Kinzo's child, then there would be no reason for the epitaph to come out as she would have defaulted into the headship anyways. Also the plot doesn't validate that Krauss was sterile, and in reality it's pretty normal for fertile couples to struggle or take time conceiving children. In this case there were perverse psychosomatic issues affecting both Klauss and Natsuhi too. Also there's the issue someone else mentioned that if Jessica was a consequence of Lion falling off the cliff, then there is no reason for her to exist in game 7 because Lion lived.""",
        user=user3,
        thread=thread1
    )
    db.session.add(post2)

    post3= Post(
        subject="RE: Umineko - Just Finished Episode 2 This Morning, Here Are My Thoughts So Far",
        text="""Great to hear that you're enjoying the vn. I had similar problems when I first started reading it, I thought the beginning was kinda slow so I ended up stopping like an hour or 2 in cause I just lost interest. Then a couple months later, I just decided to finish the 1st episode on a whim and it was the best decision I've made. Umineko is my fav visual novel now after reading it and I hope you enjoy your time with it too.""",
        user=user2,
        thread=thread2
    )

    db.session.add(post3)

    post4= Post(
        subject="RE: Umineko - Just Finished Episode 2 This Morning, Here Are My Thoughts So Far",
        text="""yay! love reading people's opinions as they go through :) i think episode 2 is the one that really hooks you in and holds on (at least it was for me!), but as others have said, episode 3 is even more exciting and fast-paced - although it's still as wordy as the rest of umineko!
              i read your comments about who you think the culprit(s) might be, but i want to ask what you think about the mysteries you've seen so far. do you think the murders were possible without magic? have you had a go at solving the epitaph?
              """,
        user=user3,
        thread=thread2
    )

    db.session.add(post4)

    post5 = Post(
        subject="RE: Umineko - I figured it out. (first time)",
        text="""Good!
        But. I assume you've played Higurashi, and know that Okonogi is not a guy to be taken up as a beacon of wholesome moral integrity. Nevertheless, he is the one who repeats this thing about love most throughout the story. Can you add this up somehow in your theory?

        I think you'll very much enjoy Ep7 opening, all in all.""",
        user=user2,
        thread=thread3
    )

    db.session.add(post5)

    post6 = Post(
        subject="RE: Episode 5 completed! Here are my theories and attempts at solving the mystery!",
        text="""Great writeup! You say that Battler never sees Shannon and Kanon in the same room, but there is a scene at the beginning of EP 5 where everyone on the island is present, how does that work?
            Episode 6 gives away quite a lot of the mystery, so I'd advice you to do your attempts at answering the other questions sooner rather than later.
            """,
        user=user2,
        thread=thread4
    )

    db.session.add(post6)

    post7 = Post(
        subject="RE: Umineko master theory based on Question arcs (Spoilers for parts 1-4)",
        text="""In Episode 1, Krauss dies on the first twilight. Do you think that Natsuhi would be an accomplice in a plan involving her husband's death? What about Episode 2 where they both die in the first twilight?
                In Episode 3, how do you explain Nanjo's death? Shannon, Kanon, Nanjo, Krauss, Natsuhi, and Maria are all exempted via red truth.
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
def undo_posts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM posts"))

    db.session.commit()
