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
        text="""<p>Since Beato had become completely unresponsive and when Battler helped her drink the tea, I speculated that years ago he had caused an accident where Beato had become severely impaired. I thought the shackle on her ankle represented her disability to walk and the fantasy world was her way of expressing her dreams through imagination since she couldn’t talk. The servants and everyone else had participated in this dream of hers and constructed the murder mystery trying to bring her enjoyment and Battler was the only one refusing to play his role because he didn’t understand/remember the accident that had been partly his fault. I don’t think Asumu’s cause of death had been revealed at this point so I thought she might’ve died in this accident as well and that would’ve contributed to Battler’s ignorance/memory loss/trauma. This accident would’ve also been the cause for his fear of vehicles.</p><p>This theory made me so depressed I had to stop reading for a while. Maybe it’s funny that I resumed after thinking that it’d be priceless if this turned out to be true, but also part of Beato’s trolling plan. Back then I still wanted the two of them to continue their game endlessly while loving, hating and tearing each other to pieces.</p>
              """,
        user=user2,
        thread=thread1
    )
    db.session.add(post1)

    post2 = Post(
        subject='RE: Umineko - My theory about Jessicas true origins + detailed analysis',
        text="""<p>Okay a stupider theory, but one that is <i>hard to deny</i><br>After all the Ushiromiya family is one that faked people being dead to mess up with a girl who nearly drowned mere hours ago even tho she’s a bitch (Erika in arc6).<br>This is factual.<br>What kind of family is the Ushiromiya family?</p><p style="margin-left:40px;">So my theory now is that everyone put “roles” (such as, victim of the first twilight, or milf who gets to wave a gun around while screaming at people) on pieces of paper in a box and had everyone picking up a role.<br>Then they enacted a very elaborate fake murder scheme.<br>The reason why the story cuts off at midnight after october 5 is because after that Battler figures it out. “What the hell is wrong with you people”.<br>He decides his crazy family needs to be obliterated for the good of everyone else.<br>He sets up the bomb, tries to run away using the backdoor (Kuwadorian). Eva tried to follow him but he escaped first.<br>BOOOM<br>The seagulls became fried. UminekoTempura.<br>A family of crazy people who’d fake death to mess up with girls who nearly drowned hours ago was removed from being a danger to everyone else.<br>Happy ending.</p><p>Also I forgot to add this, but Yasu is completely innocent. Even the Shkanontrice playing multiple roles at once thing was forced on her by others. That’s why Battler tried to save her alone (from his crazy family) but she still felt guilty about participating even if against her own will.</p>""",
        user=user3,
        thread=thread1
    )
    db.session.add(post2)

    post3= Post(
        subject="RE: Umineko - Just Finished Episode 2 This Morning, Here Are My Thoughts So Far",
        text="""<p>Krauss, at one point, mentioned having invested in a resort complex that utterly failed.</p><p>That resort was actually Jurassic Park. Velociraptors snuck onto Krauss’ boat and started breeding on Rokkenjima. Since it’s fact that velociraptors are clever girls, all the locked room murders were actually done by velociraptors, who can unlock locked doors. The end.</p><p><br><img src="https://preview.redd.it/davtcmnmjzy71.jpg?auto=webp&amp;s=b8250807b10c0a63906b732dfbae77fdbd9d8b6e" alt="CDN media"></p>""",
        user=user2,
        thread=thread2
    )

    db.session.add(post3)

    post4= Post(
        subject="RE: Umineko - Just Finished Episode 2 This Morning, Here Are My Thoughts So Far",
        text="""<p>Well I do appreciate and believe in the true theory, but, just for fun, I wanted to think up of some other theory that I could call my own, but I haven’t really rechecked the red truths so see if it’s possible, but oh well!</p><p>My theory was that, while Sayo (possibly only Shannon) is still the main culprit, most of the murders were committed by other people for their own benefit or for some other emotional reason. Like, Shannon’s motivation just caused a chain reaction of events and thought processes for the rest of the family members, and at some point or another, every family member had the chance to commit the murders (Except for Battler of course). Like for example in the first game, assuming that Shannon and Kanon were different people, Eva and Hideyoshi killed the people for the first twilight, maybe to just kill off the competition for the money and to kill off Shannon, because they didn’t want George to be with her, assuming that they knew about it, and then Kanon killed them in the second twilight because he felt angry towards the pair because they killed Shannon, and etc etc. Of course in some parts this may sound similar to the truth, but y’know, was a little thing I thought of inspired by one of Agatha Christie’s books.<br>And again, I haven’t checked any of the red truths on this matter, so it probably would have tons of flaws.</p>
              """,
        user=user3,
        thread=thread2
    )

    db.session.add(post4)

    post5 = Post(
        subject="RE: Umineko - I figured it out. (first time)",
        text="""<p>not my original theory, but I liked the one where there was actually a tunnel underneath rokkenjima to the main land. this allowed a lot of things such as making bodies disappear and letting more people actually be in the island but they just quickly got “out” of the island so the red of the number of people was still valid.<br>the basis for it came when someone looked at some of the fines and noticed something like windows with blinking lights, kinda like when a train passes through a tunnel.</p>""",
        user=user2,
        thread=thread3
    )

    db.session.add(post5)

    post6 = Post(
        subject="RE: Episode 5 completed! Here are my theories and attempts at solving the mystery!",
        text="""<p>Lets see. The Ange Culprit Theory.</p><p>As someone once pointed out the “real truth” has a big flaw in that if the message bottles of the future were written in advance and Ange was excluded in the stories even though she only did not attend the conference due to sudden illness. This is why the true culprit is Ange, the true author of the message bottles.</p><p>You think a 6 yr old couldnt possibly be the culprit? Your right, because she was 4 when she planned it. (For those who might know, this scenario is largely inspired by an MTTH500 event from Crusader Kings 2. A newborn child turns out to be THE DEMON CHILD. (S)He then attracts several witch servants and then proceeds to kill every other heir to the throne and <i>your main character</i> to finally take the crown)</p><p>At the age of 4, its hard to find servants, but fortunately Ange has a lonely and superstitious cousin. After earning her trust and joining Mariage Sorciere, she meets another lonely soul; Beatrice. At first she simply used them as playmates and scapegoats for her evil (but childish) pranks. However by chance, during her usual eve-dropping to find weaknesses, she overheard a drunk and repentant Kinzo admit to a horrendous crime.</p><p>skeletons of the most accessable family members; her parents. Eventually Rudolf let slip that secret of Battler, putting another Ace in her hand. As her skills and tactics grew she eventually pieced together the incident 17 years past through loosened lips of the elderly and the tired.</p><p>Her hand now stacked, she only needed an opportunity. And it came in the form of an Epitaph.</p><p>Using her information she turned the witch into her furniture, crushing the all hope with the knowledge that even after 1000 years there could be no HUMAN FUTURE for the witch.</p><p>She subtly guilt tripped an old servant into helping the Witch recover the gold. All the gold and honor in the golden land could not repair a destroyed heart, so the witch remained a puppet to Ange. Using the one-ring puppet and taking hold of the financial failures of the son and the guild of the wife, Ange became the true ruler of Rokkenjima.</p><p>Having gained sufficient power, Ange planned to manipulate from the shadows and ascend after reaching adulthood. However after 2 years, news of the unexpected return of her elder contender breathed a sliver of hope into her puppet, which began to resist her control. She knew it was time to abandon this Beatrice.</p><p>First she broke her foolish cousin with mere words. The seeds of malice were not planted by mere negligent innocence (This clue was given in the story even!). This hatred and despair would be harvested into a weapon.</p><p>Then she contemplated multiple scenarios to use her puppets and assets to elimate the heirs contending her throne. Although it would be ideal if everyone else died, the hungry Sumedera’s was a threat that could not be ignored. Even with her evil intellect, that fact that she was 6 would be too disadvantagous; she needed a new puppet. After careful consideration, she chose her new Beatrice, Eva.</p><p>As to what happened on Oct 4-6. EP 7 - Bernkastel “This is all the truth”</p><p>Having rigged the switch in the Goldenland to activate regardless of what happened, Ange erased the Ushiromiya family and all the evidence. Her mother played the part she manipulated her to and in return a desperate and ever loyal Aunt was born. However Ange wanted Eva’s intellect and drive to expand her empire until her eventual ascension, without wasted energy on motherly love. So like the predecessor Beatrice, she broke her, and all it took was to reject a hug and convienently have 2 dirty bottles stuffed with conflicting lies “accidently” discovered.</p><p>While successfully creating a powerful autonomous servant, Ange unfortunately became a victim of her manipulations. For a time, she would be forced to eat mud. To endure this she continously reminded herself of her own Greed and spoke to it. Her hosts here would eventually die in a series of bizarre murders, however that is another tale.</p><p>Eventually she reached adulthood and promptly returned to claim her crown. With a few drops of poison, she secretly murdered her puppet, whom had also acted as a strawman to absorb hatred of those whom bled to feed Ange’s coffers so none would be directed towards her. With the gold, the ring and the title of Golden Witch, she only would need to finish her maternal relations.</p><p>Thus she lured them into a trap on that island that day. After cleaning up all lose ends, she decided that ruling from the shadows was best and arranged for one of Eva’s servants to be her puppet.</p><p>Before the tale could close however, a threat in the form of Hachijo Tohya forgeries remained. The possibility that the old Beatrice betrayed her caused her to grind her teeth night after night. Eventually she found the Tohya and invited him to the goldenland, where he would never return from…</p><p>The End</p><p>Ange satisfies Knox’s first as she is mentioned within the first few minutes of the game.(Take that Dlanor)</p><p>No trick is needed for the EP3 red where Evatrice removes everyone from the suspect list if ANGE was the culprit</p><p>All conventional solutions can still apply with an ANGE mastermind</p>
""",
        user=user2,
        thread=thread4,
    )

    db.session.add(post6)

    post7 = Post(
        subject="RE: Umineko master theory based on Question arcs (Spoilers for parts 1-4)",
        text="""<p><strong>The following theory is just for fun, never in a million years would I consider it seriously.</strong></p><p><strong>Episode 7 spoilers</strong></p><p>Kumasawa = original Beatrice.</p><p>This is based on the fact that our Beato inherited her Beatrice title from Virgilia (who is Kumasawa’s fantasy counterpart). Virgilia being former Beatrice herself is something notable because every Beatrice, whether it is in fantasy or in real life, is somehow related to the Ushiromiya family.</p><p>The idea is the following:</p><p>- Kinzo had violent/forceful tendencies even as a young man. We could say he got “too passionate” and sometimes couldn’t keep his hands of the original Beatrice. Furthermore, Kinzo was so obsessed with Beatrice, he was madly jealous and didn’t appreciate her attempts to communicate with other people, especially men. Beatrice got sick of it, and wanted to escape and so she begged Nanjo for help. However, she got pregnant.</p><p>- She made a deal with Doctor Nanjo, he would help her fake her death and then he would give her the baby and allow her to escape. However, before Beatrice could get to her baby, the situation got messy and the baby remained with Kinzo. Meanwhile, Kinzo truly believed his beloved Beatrice was dead.</p><p>- (this is where it gets really nonsensical) Beatrice got into an accident or something that disfigured her face. She also suffered heavy amnesia and she lived for some time with that amnesia without knowing her true identity. Nanjo kept the secret from her and supported her throughout her life, even helping with her face surgery. Eventually Nanjo decided that it would be best if Beatrice/Kumasawa stayed by her grandchild (Sayo) since the child had already lost its real mother. That is how Kumasawa got employed with the Ushiromiya famil not knowing she was by her own grandchild all this time.</p><p>And that’s it. Don’t kill me please, I just have a vivid imagination.</p>
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
