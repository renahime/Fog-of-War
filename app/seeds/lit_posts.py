from app.models import db, User, environment, SCHEMA, Post, Thread
from sqlalchemy.sql import text
from chancepy import Chance


# Adds a demo user, you can add other users here if you want
def seed_lit_posts():
    user2 = User.query.get(1)
    user3 = User.query.get(3)
    thread1 = Thread.query.get(6)
    thread2 = Thread.query.get(7)
    thread3 = Thread.query.get(8)
    thread4 = Thread.query.get(9)
    thread5 = Thread.query.get(10)

    post1= Post(
        subject="RE: A first time reader's thoughts on the metaphysics of House of Leaves",
        text="""Nice read, but the whole "it's just a work of fiction" argument falls short, as MZD makes himself part of his own fiction. All his books are part of a met-universe. E.G. VEM is present in all of his works.

                But to take your approach of "So you make the descent, again" to the next level:

                HoL explecitely mentiones Douglas Hofstadter in a fake interview, who is the auther of "I am a strange loop". His main idea is that self-consciousness arises from self-reference.

                HoL contains itself and it refers to itself

                HoL is a labyrinth without a minotaur - until you start reading. The reader becomes the Minotaur as he starts to inhabit the house

                HoL gains consciousness in the moment where a reader starts to inhabit it - your mind is the "software" on which it's self-referntiality can play out

                HoL is a kind of mental parasite that keeps you engaged with it and makes you to pass it on

                And that's why it's so scary.
              """,
        user=user2,
        thread=thread1,
        created_at=Chance.date(year=2022),
        updated_at=Chance.date(year=2022)
    )
    db.session.add(post1)

    post2 = Post(
        subject="RE: A first time reader's thoughts on the metaphysics of House of Leaves",
        text="""Great post. Such a clear and concise overview of what I believe is the real strength of the book: it’s ability to subsume the reader into the narrative. I’d like to add, if I may, some additional thoughts on why this works so well.

              The book is about trauma and how people overcome them (or don’t). Every character in the book grapples with some sort of regret or mistake or long suppressed pain from their past, and the House allows them to confront that issue head on. In the same way, by inviting the reader into the story, allowing them to shape the story as they perceive it, they too confront their own traumas or regrets. So many of the positive reviews for the book mention how it stuck with them or helped shape them in some way; that’s the power of the house and the book. The book’s themes allow it to echo into the reader’s life, which explains and justifies the meta nature of the book as a reflection of that reality. Ultimately, the answers to those unanswered questions can’t be found in the book, and that’s the point; only in reality do we know who wrote the book, Mark Z Danielewski. And only he has the ultimate answers, but each reader comes to terms with not knowing everything on their own and finds their own answers. Each reader confronts their Minotaur on their own. Each reader confronts their traumas and regrets on their own, often when feeling lost and confused, unable to find a way out, searching for answers that don’t exist and never will, stuck in a labyrinth of their own making.

              Of course, that’s just my interpretation. Anything anyone gets out of the book is also valid. :)""",
        user=user3,
        thread=thread1,
        created_at=Chance.date(year=2022),
        updated_at=Chance.date(year=2022)
    )
    db.session.add(post2)

    post3= Post(
        subject="RE: House of Leaves - I believe I've found the profound message at the heart of this book. I might also be insane. Who knows.",
        text="""I wholeheartedly agree. House of Leaves is predominantly about grief, and the desire to understand or find logic or reason in things that often reject understanding. You can try to understand or break down why someone passed away, just like you can go on countless expeditions to hopefully find the center of a maze, but in the end it will lead you right back to where you started. So much of this book is about letting go, as well as rejecting the notion that closure is a promise.""",
        user=user2,
        thread=thread2,
        created_at=Chance.date(year=2022),
        updated_at=Chance.date(year=2022)
    )

    db.session.add(post3)

    post4= Post(
        subject="RE: House of Leaves - I believe I've found the profound message at the heart of this book. I might also be insane. Who knows.",
        text="""I agree! It's not about literally ignoring Johnny or any part of the book. It's realizing that none of our unreliable guides can lead us through the labyrinth, because they are themselves lost within it. But by the time you realize the book is playing with these concepts, you are lost in it yourself, seeking answers blindly, just like the characters are. I think that bewildering experience is kinda the point.
              """,
        user=user3,
        thread=thread2,
        created_at=Chance.date(year=2022),
        updated_at=Chance.date(year=2022)
    )

    db.session.add(post4)

    post5 = Post(
        subject="RE:House of Leaves - The Author - A Unifying Theory",
        text="""Great post, I agree. Adding to this: „A novel“ on the book cover is printed in purple, hinting that the whole book is the work of The Author.

                It‘s pretty likely that The Author is Pelafina.

                As good as the theory is when you only consider HoL, it basically gets impossible when you consider the screenplays which where released around 2 years ago. In these, TNR is revealed to be a real film. On the other hand, I‘m not sure what to make out of this, as it could just be a move from MZD to make things even more impossible to interpret coherently by intention.""",
        user=user2,
        thread=thread3,
        created_at=Chance.date(year=2022),
        updated_at=Chance.date(year=2022)
    )

    db.session.add(post5)

    post6 = Post(
        subject="RE: Creepy personal connections in HOL",
        text="""Interesting take. I went the completely other way and thought that maybe Johnny didn’t exist... and the whole thing was written by Pelafina. But it’s been a couple years since I’ve read it so I’m trying to remember exactly why I came to that conclusion. I think it was because there’s a line in there somewhere about Pelafina and Zampano knowing each other, which obviously shouldn’t be possible if the book is taken at face value. So I thought she created all of Johnny’s world in the throes of her mental illness and grief of the loss of her child. But I also think that is possible to come to a completely different conclusion every time a person reads it.
            """,
        user=user2,
        thread=thread5,
        created_at=Chance.date(year=2022),
        updated_at=Chance.date(year=2022)
    )

    db.session.add(post6)

    post7 = Post(
        subject="RE: House of Leaves - Zampano's scratched floor",
        text="""This is a great question, and one which I hadn’t thought. I like the red herring idea, but here’s the first thing that popped into my head, it could be total nonsense, but I thought, “Never Ending Story,” or a book that comes to life.
        I think there might be points in the text to support this. I just finished reading HoL for the 4th time, but the first time in over a decade, and the first time since I got my English Degree. I’m going to go back through my annotated copy with this in mind. Thanks for the new inspiration. This book is so wildly dense, and I love this sub for posts like this.
        """,
        user=user3,
        thread=thread5,
        created_at=Chance.date(year=2022),
        updated_at=Chance.date(year=2022)
    )

    db.session.add(post7)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_lit_posts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM posts"))

    db.session.commit()
