from app.models import db, User, environment, SCHEMA, Post, Thread
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_higu_posts():
    user2 = User.query.get(2)
    user3 = User.query.get(3)
    thread1 = Thread.query.get(11)
    thread2 = Thread.query.get(12)
    thread3 = Thread.query.get(13)
    thread4 = Thread.query.get(14)
    thread5 = Thread.query.get(15)

    post1= Post(
        subject='RE: Speculating at the end of the Question Arcs',
        text="""<p>It's always great to read newcomers' theories :) Since you're heading towards the answer arcs which give a bunch of reveals, you might consider revising/expanding your theories of every single question arc after every answer arc. Have fun :)</p>
              """,
        user=user2,
        thread=thread1
    )
    db.session.add(post1)

    post2 = Post(
        subject='RE: Speculating at the end of the Question Arcs',
        text="""<p>As far as Takano's burnt body in Watanagashi goes, the police analysis mentioned at the end of Watanagashi suggests she was dead -before- the festival.</p>""",
        user=user3,
        thread=thread1
    )
    db.session.add(post2)


    post4= Post(
        subject="RE: Hey guys, just finished the four question arcs",
        text="""<p>Higurashi is an older series, so a lot of people won't be as spoiler-conscious. I'd be careful about lurking around anywhere until you get to the end. Stay off Wikis.

As for the extra arcs, a lot of them are arcs that were released exclusively for console versions of Higurashi in Japan. A lot of them deal with other characters who are only tangentially connected to any of the main series cast, but there are others that expand a great deal upon the cast, and there's also an alternate ending that some people (myself included) like more than the "actual" ending (it resolves a lot more character arcs and involves the entire cast a lot more).

Your theories are very interesting. I think you'll be satisfied with the ending either way.</p>
              """,
        user=user3,
        thread=thread2
    )

    db.session.add(post4)

    post5 = Post(
        subject="RE: Umineko - I figured it out. (first time)",
        text="""<p>Man I wish I was in your situation once again. I was enjoying each chapter so much and was totally clueless that chapter 6 and 7 were even better than the previous ones</p>""",
        user=user2,
        thread=thread3
    )

    db.session.add(post5)

    post6 = Post(
        subject="RE: Episode 5 completed! Here are my theories and attempts at solving the mystery!",
        text="""<p>Glad to hear that Mion is your favourite character. Personally, I don't recommend re-reading now and just go through Kai, as all answers will be revealed there. You can still re-read it afterwards when you finally know how things are actually going, it's honestly fun once you find out the truth.</p>
""",
        user=user2,
        thread=thread4,
    )

    db.session.add(post6)

    post7 = Post(
        subject="RE: Umineko master theory based on Question arcs (Spoilers for parts 1-4)",
        text="""<p>I think Rika describes the phenomenon as literally, “rewinding time”. I disagree with her phrasing for several reasons, but mainly because certain arcs continue <strong>after Rika’s death</strong> (which is when I assume time rewinds, as it is her and Hanyuu’s last memory in the new “timeline”) although I guess that from the girls’ perspecitves, time is rewound for them. For example in Tsumihoroboshi-hen where Rena is interviewed by Akasaka and Ooishi, the epilogue takes place long after the Great Hinamizawa Disaster.<br>Another reason is that minor discrepancies exist in each separate “timeline” - For example despite Minagoroshi-hen being directly proceeded by Matsuribayashi-hen, Houjou Teppei does not return to Hinamizawa (which he did in the previous arc). Or how Akasaka had managed to save Yukie (his wife) in some arcs, but not in others (an event that would’ve occurred before the “rewind point” in some arcs).</p><p>This leads me to the theory that the different arcs may instead exist as a series of <strong>parallel dimensions</strong> - each one slightly different than the others. This would make Rika and Hanyuu a pair of <a href="http://haruhi.wikia.com/wiki/Sliders">Sliders <span style="background-color:rgb(53,53,53);color:rgb(157,157,157);">9</span></a>, who jump to a similar world replacing their counterparts there, or rather replacing their memories (since Rika doesn’t age abnormally). Things that combat this interpretation include the fact that other characters begin to remember the events of previous arcs - which can’t be explained by parallel dimensions, unless it’s related to Hanyuu’s ability to carry across Rika’s memories? Also, the spin-off game Higurashi Daybreak features a “Time Freeze” as one of Hanyuu’s special abilities: implying some sort of control over time… but the authenticity to the original canon is debatable.</p><p>Late into Higurashi, these separate worlds are officially named “<strong>Fragments</strong>”- a term returned to in Umineko. The exact meaning of the term is up for speculation, but Umineko seems to imply that Fragments [Spoiler]may not necessarily exist in reality, and provides a number of possible interpretations: perhaps the fragments exist as <strong>different works of fiction</strong> (like the VNs in the Real World?), <strong>different interpretations of factual events</strong> or more abstractedly, <strong>fantastical games between magical beings</strong> in planes that transcend our own. Importantly, this question is never answered, which leaves the reader free to interpret the events of the stories as any of these possibilities[/Spoiler].</p><p>For my personal interpretation; I think it’s a bit depressing to imagine that each arc is a self-contained world and that for every happy ending there are an infinite amount of unhappy equivalents - something I thought about a lot when reading another VN, Steins;Gate. In the case of Umineko, [Spoiler]only one “True World” really exists, and thus fragments can’t represent reality. If we look at Higurashi from that perspective, perhaps Rika and Hanyuu really did rewrite time, taking certain memories and experiences with them, but ultimately erasing the bad ends[/Spoiler]. But I feel that the true meaning of fragments is much larger than we can understand - they’re a deliberately abstract concept, much more than any of the definitions provided here. My understanding of fragments is that they <i>can’t be understood</i>. Call it a plot hole if you will, but it explains why we can’t come to an exact conclusion on how they work. Thus, if the fragments themselves can’t be explained, neither can Rika and Hanyuu’s ability to move between them, or the phenomenon causing people’s memories to carry across.</p><p>Side note: I feel these discussions get dangerously meta, mainly thanks to Umineko. I almost wrote a paragraph describing each fragment as a different Visual Novel written by Ryukishi because <strong>that’s what they actually are</strong> and therefore we shouldn’t worry about fragments since they’re just a narritave device; <strong>which they actually are</strong>. Oh wait, I did write it after all. Help.</p>
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
