from app.models import db, User, environment, SCHEMA, Post, Thread
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_uzumaki_posts():
    user2 = User.query.get(2)
    user3 = User.query.get(3)
    thread1 = Thread.query.get(26)
    thread2 = Thread.query.get(27)
    thread3 = Thread.query.get(28)
    thread4 = Thread.query.get(29)
    thread5 = Thread.query.get(30)

    post1= Post(
        subject='RE: Speculating at the end of the Question Arcs',
        text="""<p>It felt like a waste of time. I know people like to use Lovecraft as an excuse. But that guy is a racist lonely guy who somehow found a woman miraculously. The fact that we have protagonists that care about each other already puts the work outside of lovecraftian incel territory. Pretty much every ody is dead except maybe her brother but he's not even conscious anymore so it doesn't even matter. I was hoping the two could've survived all that</p>
              """,
        user=user2,
        thread=thread1
    )
    db.session.add(post1)

    post2 = Post(
        subject='RE: Speculating at the end of the Question Arcs',
        text="""<p>Just finished last night.

What got me is that the two "main characters" spiraled together into what appears to be a point, but then disappear forever. I think it would have been more poignant to have them form a final piece to the spiral, finally assuming their place.

I think having them form the tip of the drill bit would be hitting the theme a little too hard on the head - a little to cliché. But seeing how they completed the structure, versus just kind of being added to the structure, would make it feel more like all that is, and ever was, the spiral.

Sorry for the disjointed thoughts. I've never mastered the ability to pen ideas and theories.</p>""",
        user=user3,
        thread=thread1
    )
    db.session.add(post2)


    post4= Post(
        subject="RE: Hey guys, just finished the four question arcs",
        text="""<p>What do you think Uzumaki is telling us to do?

Nietzsche hated when he read something in which the other wasn’t at least somewhat exhortative.

In Zarathustra, Nietzsche describes the last man: “the earth hath then become small. His species is ineradicable like that of the ground-flea; the last man liveth longest. ‘We have discovered happiness’ —say the last men, and blink thereby.

They have left the regions where it is hard to live; for they need warmth. One still love the one’s neighbour and rubbery against him; for one needeth warm.”

Uzumaki’s spiral’s are representations of the various trappings of the material world in a Gnostic way. Evangelion draws much from Gnosticism.

At the very end of Uzumaki, the people of the town have formed what is in my opinion a representation of “the last men”. That is, the preservation of life itself that becomes the only thing that matters – they live longer lives.

Our heroes are Nietzsche-esque supermen in this town, so they never succumb to the spiral. In the end, we see them eyes closed, holding one another while the blob of people turn to stone.

Uzumaki is let’s say post-Zarathustra reactionary because why not make stuff up. Ito is telling us to avoid all spirals and become great. The first thing to do is to leave the city before the spiral grabs hold. The cities are already captured by modern man’s spirals so supermen should just go to “regions where it is hard to live”.</p>
              """,
        user=user3,
        thread=thread2
    )

    db.session.add(post4)

    post5 = Post(
        subject="RE: Umineko - I figured it out. (first time)",
        text="""<p>awesome theory! do you think shuichi leaving town everyday in the beginning helped his resistance to the symptoms?</p>""",
        user=user2,
        thread=thread3
    )

    db.session.add(post5)

    post6 = Post(
        subject="RE: Episode 5 completed! Here are my theories and attempts at solving the mystery!",
        text="""<p>“Have you never contemplated, how many times an Ohtsutsuki who became a god, may have manipulated humankind’s memories” ? - Momo ch. 79

This is an amazing theory</p>
""",
        user=user2,
        thread=thread4,
    )

    db.session.add(post6)

    post7 = Post(
        subject="RE: Umineko master theory based on Question arcs (Spoilers for parts 1-4)",
        text="""<p>i love this idea! i'm pretty sure in the book, it was stated as a curse and i remember hearing some theories about the curse reseting every hundreds of years or something? i think that would make sense since the long houses in the town all connected into one big spiral, almost as if it was originally built like that, right? but i really love the idea of this combined with the curse theory!</p>
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
def undo_higu_posts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM posts"))

    db.session.commit()
