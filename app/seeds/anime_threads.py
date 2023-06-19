from app.models import db, Category, environment, SCHEMA, Thread, Post, User, SubCategory
from sqlalchemy.sql import text
from chancepy import Chance


# Adds a demo user, you can add other users here if you want
def seed_threads():
    user = User.query.get(1)
    category = Category.query.filter_by(name='Anime Manga and Visual Novels').first()
    subcategory=SubCategory.query.filter_by(name='When the Seagulls Cry').first()
    thread1= Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        created_at=Chance.date(year=2022),
        updated_at=Chance.date(year=2022),
        subject="Umineko - My theory about Jessica's true origins + detailed analysis",
        text="""Spoilers! Please don't read if you haven't read at least Episode 5.

              Let met tell you straight away that Natsuhi is one of my favorite characters, who I believe ate an immense share of the suffering cake that is the Ushiromiya family's curse.

              And let met expose my theory, that Jessica... is not Krauss' daughter.

              Natsuhi, was in an increasingly desperate state - that her only role as an Ushiromiya wife, being a womb and give birth to a successor can still not be fulfilled - that reached its climax 7 years after trying when she's presented a baby that isn't hers. But then, less than a year after that, Jessica was born. And all that comes before it is described as "filthy" by Natsuhi. Let me write what I think.

              Krauss is sterile. There's an interesing discussion between 'Beatrice' and Natsuhi in Episode 5 (Natsuhi really was alone, Beatrice representing her inner conflicts in a fantasy narration - as stated by Bernkastel), that Natsuhi repeatedly tells that it's all her fault they couldn't have a child as she has a dysfunctional body - and Beatrice repeatedly answers that it's not her fault, as there are 2 people needed in a couple to make a baby. The ironic proof that Beatrice was right is that Jessica finally was born after more than 7 very long years, a proof that Natsuhi's body is working perfectly and which hints that Krauss was the one at fault.

              Natsuhi is sexually frustrated with Krauss. The scene with Natsuhi and Beatrice drinking tea in the rose garden (where in reality Natsuhi was alone), where Natsuhi remembers the distant past, when Krauss and her were just married and often went to foreign countries at the start of their relationship. What she particularly remembers on the day when Krauss lets her taste an areca nut, is their torrid night that came after that. In reality, she longs to come back to these days, cursing the reality that she and Krauss now both spend the night in separate rooms and separate beds... which is, peculiar for a couple their age, isn't it? Also, her seemingly candid reaction to the "Sucker merry barrels" joke in Episode 3, where she's blushing when she's the last one to understand, points that such sexual matters are something she hasn't experienced enough in a practical way for a very long time.

              Natsuhi cheated on Krauss after the cliff incident. In about every episode, Natsuhi reacts strongly when someone brings up the subject of Kinzo's mistress, stating adamantly that such a thing would be too filthy. One might think she's protecting Kinzo's honor, but there's more to it : even in E7, at church, when Kinzo is really alive and everyone think that Beatrice as a mistress would be romantic - as his wife was brought to him by an arranged marriage - she carefully disguises the matter by employing the words "Kinzo's in her debts" : and there, Kinzo is alive, not a delusion of Natsuhi telling her to protect his honor. And, "filthy" is what all she remembers of herself before Jessica was born. Moreover, in Episode 6, Kanon states that Natsuhi is strict and severe towards female servants, but kind towards male servants. This one is a dead giveaway, as it's a common 'Cheating Flag' used in literature depicting a lord or a lady and his/her servants (telling us that the lord has a cheating trait, not that he cheated with the mentioned female servants themselves).

              ==> I believe that Natsuhi, driven into a corner after the cliff incident, has a huge inner conflict that translates into breaking her high values, so that even if she loves Krauss, she's desperate to give birth to a baby AND is already sexually frustrated with him (Krauss, in my opinion, is not a sexual person in the first place. Natsuhi and Krauss' sexual life after the first few years post-marriage being, more or less, a mere "We try to make a baby", without any particular joy for her). The point is that she does love Krauss, contrary to Erika's claims in Episode 5, and that's what makes her state of mind at the time all the more believable as to why she never tells him. There's also the possibility that herself isn't sure who's the baby's father.

              I have 2 theories about who's Jessica's father.

              Rudolf. Rudolf was a serial cheater, and mentions in about every episode how Jessica is a very beautiful "Natsuhi-esque" woman, even in E7 Tea party, the 'truth'. He also states numerous times how Natsuhi herself is beautiful, even to Kyrie, and that he values her highly. There's also the fact that some of Jessica traits are similar to Rudolf's : Being easygoing, employing a bordeline impolite language. Not to say that Jessica, of the 5 cousins, is the one that inherited the least of their parents' character or attitude. Battler inherited the easygoing-mode, relaxed language from Rudolf (look how Battler and Jessica look alike in that regard) and is successful too with girls, George inherited Hideyoshi's fortitude, Maria inherited Rosa's childish character when she was young, Ange is a smart kid like her mother. This is my favorite theory of the two. The "Sucker merry barrels" joke holding a whole different meaning is also interesting to note.

              Kinzo. Erika has a passion of debunking gentle lies and all of Episode 5 is very important to consider. We know that she was wrong in that Natsuhi was not the culprit, but all her assessments of Natsuhi being a cheater (again an important argument to consider in this theory!) have probably a glint of truth in it. If we take Erika's reasoning at face value, she slept with Kinzo while being dressed like Beatrice : considering Jessica's age, I'm not a fan about him sleeping with her 18-19 years ago, but if we think about it, it's perfectly valid : After the cliff incident, Natsuhi hates Kinzo for forcing the baby on her, but also feels extremely guilty as she was entrusted by him and that her only role in his eyes, being a womb or a least a mother for a successor, failed, again. Because of that, she wanted to make amend and propose to him, in a last hope to bring a baby, that would be a source of relief for both Natsuhi and Kinzo. Kinzo, passionate, looking at Natsuhi dressed as Beatrice, willing to sleep with him, brings him a temporary sense of alleviation, as it would overwrite for a time his horrible misdeed with Beatrice 2, who was not consenting.

              Feel free to discuss about it!
              """)

    db.session.add(thread1)

    thread2=Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        created_at=Chance.date(year=2022),
        updated_at=Chance.date(year=2022),
        subject='Umineko - Just Finished Episode 2 This Morning, Here Are My Thoughts So Far',
        text="""As the title says, I've just finished reading Episode 2, and wanted somewhere to spew out my thoughts about what's happened so far. I'm really starting to love the game and excited to see what Episode 3 has to offer.

                My history with this game is a little weird. Well over a year ago, I finished Episode 1 after bouncing off it multiple times and coming back hoping to like it more. I came off of it somewhat enjoying it, but felt like I had to slog through somewhat exhaustive amounts of text and characters I didn't necessarily like following to get to a few really great moments near it's climax. I overall didn't know if it was for me, and when I started Episode 2 and saw it opened with more of the same slow intro I had dreaded in the first one, I decided that the game just wasn't for me.

                Part of this is my limited exposure to other kinetic VNs like this. Most of the visual novels I've played and loved in the past have been far more interactive and far less descriptive and much faster paced in their actual writing.

                I played Umineko based on the recommendations of youtubers I liked (shout out to Red Bard) and my boyfriend who once watched a roommate play part of it. The only real things I knew about Umineko going in was that it was a very long murder mystery VN with witches, that gets a bit crazy and not much more.

                Coming off of Episode 2 however, I think I'm really starting to love this game. I find myself sitting at work on slow days thinking about it somewhat incessantly, piecing together details and crafting theories for what exactly is happening on Rokkenjima (that are usually probably wrong) and getting excited for each and every reading session.

                Red Truths are such a simple but smart mechanic for story telling, especially in a murder mystery like this. I absolutely love how much it's introduction cuts down on what would otherwise be a repetitive line of thinking at the start of each argument, and I LOVE how quickly it's spun on it's head by Battler. I got so excited the first time he said something along the lines of "let's hear you repeat THAT in that red text of yours, Beatrice."

                Out of all the character arcs in Episode 2, my favorites of the bunch were easily Kanon and Aunt Rosa's. Kanon's "no longer furniture" bit was so bittersweet, but such a great conclusion to his story in Episode 2. Really hoping him and Jessica get a happier ending by the end of things but I guess we'll see.

                I feel so conflicted on Aunt Rosa and I think that's great. She's a horrible mother, and a lot of the scenes between her and her daughter were among the hardest to read in the episode, but yet I still just couldn't hate her. She's been dealt such a bad hand in life, and while I don't think you could justify how she feels with the frustration her circumstances have caused, those frustrations are justified. I think her attempted escape at the very end of the episode was fantastic and easily one of my favorite scenes that I've read in a VN (though the punishment she and her siblings get in the tea party afterwards is so horribly cruel).

                Also the music has been absolutely incredible. I've been listening to Golden Slaughterer so much, but there's so many other tracks in the episode that really helped sell some really great scenes.

                If you read all this, I hope you enjoyed my disorganized ramblings, and feel free to ask any questions if there's anything else you'd like to know my thoughts on. I'm really starting to love this game and excited to see what else it has in store.


                """)
    db.session.add(thread2)

    thread3=Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        created_at=Chance.date(year=2022),
        updated_at=Chance.date(year=2022),
        subject='Umineko - I figured it out. (first time)',
        text="""I am about halfway (I think) through Episode 6 (post first twilight) and I believe I have the gist of everything. Feel free to laugh at me in the comments if this is stupid.

                Not going to get too far in the specifics because it is very late and I'm bound to forget something or two or a lot. So this will just be broad swathes and conclusions.

                Without love, it cannot be seen.

                I am assuming that this is like Higurashi where there are multiple culprits depending on the fragment but one "mastermind" who commits murders and is the driving force behind the conflict.

                Shannon and Kanon are the same person. Which is the real one, I don't know. Probably Kanon because I think it would be quite hard to conceal those massive boobs (yes seriously, boobs are a clue in Umineko apparently). They are never seen on screen in the same place by Battler and I believe not by Erika either. This explains most locked room mysteries, as they likely had two master keys ("there are 5 keys, one for each servant").

                They are the culprit of Legend. It's pretty simple. The only one who saw Shannon's corpse was Hideyoshi, which was suspicious from the start even before it got convoluted.

                The mastermind of Turn is the same, though I believe Rosa might have played a part. We are shown at the end that she is very willing to have monetary incentives as a motive, as she struggles between holding the gold, her gun, and Maria. She appears to confess her sins to Maria in a roundabout way as death approaches. She was probably bribed (we know the mastermind has access to the gold because it was placed in the chapel).

                Banquet was mostly solved by Battler. Eva probably got into a dispute with Rosa and ended up killing her in the heat of the moment then murdered the witness, Maria. The Shannon/Kanon theory explains Nanjo's death. As for Hideyoshi, it's possible Kyrie killed him after realizing he was an accomplice, hence her motive for leaving the mansion despite not caring about the food. The mastermind probably killed George.

                I actually still need to think about Alliance. I have the least memory of the events in it and still need to devise my theories on it. However I doubt it will change my overall conclusions because according to Knox the answer had to be foreshadowed from the start, meaning by Legend (the same logic Battler used to conclude it was one of the 18). Haven't worked through End either. Maybe I'll make an update post or a comment to this one if people are interested after I parse through them.

                Now this is where it gets good. "Beatrice" is also Shannon/Kanon. They give Maria the letter while dressed as her. But even more than that, They are BEATRICE, the Golden Witch. Without love it cannot be seen. The sin of six years ago. This character was in love with Battler, foreshadowed by George's musings on Battler's childhood relationship with Shannon. The reason one's happiness comes at the expense of the other's is because they are the same person, and Beatrice is also them. That is the metaphor of the game they play during the first twilight of Dawn; Battler wants the new Beatrice to realize it. They showed themselves to Battler at the end of Alliance after testing Jessica and George's love and ending up unsatisfied. Battler failed to realize his sin, so they killed him too. That is the nature of the fickle witch.

                And there you have it. That's my general theory going into the endgame.


                """
              )
    db.session.add(thread3)
    thread4=Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        created_at=Chance.date(year=2022),
        updated_at=Chance.date(year=2022),
        subject="Umineko - Episode 5 completed! Here are my theories and attempts at solving the mystery!",
        text="""General theories I have

              Battlers sin: Not going to lie this kinda had me stumped for a while until I went back and reread some chapters. As far as I know, his sin is lying to Shannon about coming back to Rokkenjima and saving (?) her. I came to this conclusion by noticing her wording "So you can't remember things that happened 6 years ago very well? **I can remember as clearly as if it was yesterday**" then George said " "Well, your memory's great, after all. You remember the kind of things Battler did and said back then pretty clearly, don't you?" then Shannon went on to say "Let's see... I'm sure that he said something like this when he left. 'I'll be back, <see you again>. I'll surely come for you riding a white horse'." Note the white horse, who usually rides white horses in fiction?KNIGHTS IN SHINING ARMOR! So that's my reasoning for battlers sin, this is honestly the only thing I can see being Battlers sin.

              Shannon is Kanon (or vice-versa): While working out the mystery throughout the episodes, Shannon and Kanon have always been high on my culprit list. Their alibis are always shaky, they're never in the same room when Battler is present, and Kanon straight up disappeared in ep 2 and was never shown dead in Episode 1 (and while Shannon was shown dead in ep 1 their face was half smashed and Battler never saw them). There's also the fact that Shannon has a "real" name and Kanon doesn't, so "Sayo" is the real ShaKa [;)] and whenever it's announced that "Shannon" is dead or "Kanon" is dead that doesn't mean they're dead, it only means the person named "Shannon" or "kanon" is dead and as previously stated, ShaKa doesn't exist, only Sayo does. Therefore the red truth doesn't affect them.

              On to the mystery:
              Episode 1

              Twilight 1: this one is pretty easy to explain. Any of the servants could have done it, I’m going to say it is Shaka because of what I previously said about Battlers sin and Shannon being the only one battler doesn’t see.

              Twilight 2: Note Battler never saw the chain intact, he only saw it when it was broken, so It’s entirely possible (jre reference) that Kanon and Kumasawa (she did not kill anybody, she was simply there) went into the room and killed both Eva and Hideyoshi without it going against the Red Truths.

              Twilight 4: Like I previously said, Battler never saw Kanon with the stake in him. He could’ve simply faked his death. Nanjo is an accomplice, he covered for Kanon and falsely claimed his death.
              Twilight 5: Kinzo was already dead.

              Twilight 6-8: Kuwasama or Nanjo could’ve put the letter on the table. Kanon went to the parlor and killed everybody.

              Natsuhis death: Kanon lured her out to the lobby and shot her with one of the rifles from Kinzos study.

              Why-dunnit: For Nanjo and Kumasawa it’s pretty easy to guess why they followed along with Sayos plan. Money. It was shown in the 5th game that Nanjo knew Kinzo was dead and was either bribed or blackmailed into keeping his mouth shut. Kumasawa was interested in the money as shown in the 4th episode, if Sayo promised a huge payout I can see her going along with it. Nanjo needed the money for his grandchild’s surgery (?) and Kumasawa I assume she just wanted enough for her children and herself.

              Episode 2

              Twilight 1: Rosa went into the cousin’s room to take the key, then Shaka disguised as Beatrice worked with Rosa and lured all of the siblings to the Chapel under the ruse that she was going to show them where the Gold is. By Using the toxins in Kinzos room ShaKa created a drink that was used to knock all of the siblings out, they then went on to slice them open.
              Twilight 2: Kanon went with Jessica to Beatrice’s room and killed her. Rosa, Genji, and Shannon all reported that they saw Kinzo and he was in good condition, which is a lie. This backs up my previous theory that Rosa is an accomplice.

              Twilight 4-5: Shannon and Genji killed Kumasawa and Nanjo. Refer to the previous twilights to see why I said this.

              Twilight 6-8: Shannon killed both George and Gohda then went on to kill herself.

              Why-dunnit: Rosa wanted money. This is prevalent throughout all of ep 4 (ROSA BEST MOM) and the ending of ep 2. Genji is following Shannons orders (who he perceives as Beatrice).

              Episode 3:

              Twilight 1: ShaKa kills everybody. Since Battler doesn’t see the bodies it is assumed that their keys are grouped together or there was a body double that was smashed in like in episode 1 so confirming the identity isn’t possible.
              Twilight 2: ShaKa caught Rosa by surprise and killed her then subsequently strangled Maria.

              Twilight 4-6: ShaKa killed Rudolph and the others. George was called by Shannon from outside the window, blinded by his emotions, he jumped out the window and was lead to the Mansion where he was killed. Somebody then locked the window behind him.
              Twilight 7-8: Shannon came back and lured Natsuhi and Krauss outside then killed them. ( I have a theory that before killing George, Shannon convinced him that the Killers were Natsuhi and Krauss, then when Shannon tricked them into coming outside they ambushed them and headed back to the mansion).

              Web of Truth: Shannon Killed Nanjo then pretended to be Kanon and led Jessica to the parlor where he killed her. Eva and Battler find them dead, and see Shannon in the parlor standing over George and Jessica, Shannon then shoots Battler in the back then Eva shoots Shannon and heads to Kuwadorian.

              Episode 4

              Episode 4 was honestly a fuckfest of a game. So I’m not going to spend too much time decoding the murders and mystery, even though at this point it pretty much solves itself.

              Twilight 1: ShaKa appears as the new family head and is recognized as “Kinzo”. Rosa and Sayo then go on to kill the first six and let Kumasawa and Gohda go.

              The rest of the twilights: I feel like Kyrie and Krauss are being held at gunpoint, or are being tricked into thinking they will let the children live if they follow along with them or something. (Sidenote: I feel like Nanjo was killed before the rest of the children since he was so far away). They go on to call Jessica and the others and read off the script informing them of the plan to pass on the headship. Jessica and George follow the instructions, then Rosa goes and kills George. Rosa then tells Jessica to tell Battler that this was all done with magic, she then finishes her off. Shannon does the same thing Rosa did. Sayo then goes on to kill both Krauss and Kyrie. Sayo impersonates Beatrice and tells Maria and Battler their instructions. Sayo kills Maria with poison.
              I don’t have an answer to the final riddle as of yet, maybe a timed bomb idunno.

              Conclusion.

              This is just my go at solving the mystery. I'm going to attempt to solve Battlers sin, his identity, the meta world, why Beatrice gave up after Episode 4, etc. After I'm done with episode 6. When I am done with ep 6 I plan to reread all the episodes to refreshen my Memory and look for clues to those aforementioned questions. So look forward to another one of these posts in the next couple of weeks!

              Please feel free to critique my attempt, if there's anything I'm missing or got wrong please say so!


              """
    )
    db.session.add(thread4)
    thread5=Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        created_at=Chance.date(year=2022),
        updated_at=Chance.date(year=2022),
        subject='Umineko master theory based on Question arcs (Spoilers for parts 1-4)',
        text="""First of all: DON'T SPOIL ANYTHING AFTER CHAPTER 4. I haven't started the answer arcs, so don't tell me if I'm correct or incorrect, just point out any major flaws in my theory.

              Before I start chapter 5 of Umineko, I'm gonna present what I think happened on Rokkenjima.

              I made a similar post yesterday but I was kind of being sarcastic at parts. After listening to a few podcasts and talking to some friends, I have revised my theory heavily and think I have figured it out. We will see if I am right. Here is my final serious theory before I head into the Answer arcs.

              Who is Beatrice?

              There are at least 3 Beatrice's. Beatrice 3 = Shannon = Kanon. From now on I will be referring to "Beatrice" as B3SK for obvious reasons. How did I come to this conclusion? Well it starts with Battler's "sin". According to people I have talked to, it is possible to figure out Battlers sin by the end of Chapter 4. There is very little information about this sin except that it was committed 6 years ago. The game doesn't really give you any info about how Battler was like 6 years ago and if he did anything. That is, except that he promised Shannon that he would ride back on her with a white horse. Since his mother died, he didn't. He broke his promise to Shannon. That is the only thing Battler has done 6 years ago that could be classified as a sin. Ok so we know Battler's sin now. So why does Beatrice suddenly get so upset when Battler forgets? The answer is simple. Beatrice is Shannon. Beatrice states that she did not exist 6 years ago, but she is still mad at Battler. Therefore, Beatrice is Shannon. Ok now we know that these two people are the same person. Or rather, these two personalities are the same person. Beatrice 1 is B3SK. So why is Kanon part of this? Because Kanon clearly faked his death in Chapter 1, Battler never saw his body, and Kanon decided to kill everyone for some reason. No other body disappeared in Chapter 1. On top of that, Battler has never seen Kanon and Shannon toghether, which is not accidental I bet. B3SK Is definitely the culprirt of Chapter 1. So who is Beatrice 1 and 2? Beatrice 1 is Kinzo's orginal mistress. He was obssesed with her and she probably gave him gold or something. Beatrice 2 is the Beatrice that died in 1968 on Rokkenjjima and lived in Kuwadorian. This is straight up confirmed with red truth. Beatrice 2 is the illegtimate daughter of Beatrice 1 and Kinzo. Another thing, Beatrice is a title, not a name, which supports my theory even more.

              TLDR:

              Beatrice 1: Kinzo's mistress

              Beatrice 2: Kinzo's illegimate daughter

              Beatrice 3: B3SK. The Beatrice we see in Chapter 2 and the end of Chapter 4. Also Shannon and Kanon.

              Who is the culprit?

              B3SK is the culprit. I still don't know B3SK relations with the Ushiromiyas, but there is probably some weird connection this B3SK has. Notice how we never see Kanons body? Kanon is the culprit, so B3SK is the culprit.

              What is the motive?

              Remember how Battlers "sin" was a partial cause of the murders? B3SK is mad that Battler did not keep his promise to her. B3SK is probably also mad at Kinzo for some reason. Basically, B3SK wants to take revenge on everyone.

              Who are the accomplices?

              Nanjo, Krauss, Natsuhi and Maria. I'm just gonna paste my previous reasoning for this. In total, there have been 5 characters who haven't died in the first twilight. Battler (I don't think its him., George, Jessicca, Maria and Nanjo. Notice something strange? Nanjo is the only one who isn't a child who is spared every single time at the begging. Therefore, Nanjo is probably an accomplice. Who else is an accomplice? Krauss and Natushi are extremely suspicious. They cover up Kinzos death, they must have a motive for doing that. Finally, I think Maria could also have been an accomplice. Maria is shown to have split personalities, and by 1986, the trauma of her abusive mother could cause her to aid Kanon in killing everyone/

              Who is Battler?

              Battler's mom is Kyrie most likely. Simplest explanation.

              Who did Battler see on the Rooftop?

              B3SK

              Who wrote the letters and wrote in the Diary?

              B3SK

              How is Battler killed at the end of Chapter 4?

              Poisoning from the food, possibly the same way Maria was killed

              Please point out any glaring flaws without spoiling (if possible)! Thanks for reading!


              """
            )
    db.session.add(thread5)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_thread():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.threads RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM threads"))

    db.session.commit()