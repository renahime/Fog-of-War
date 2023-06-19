from app.models import db, Category, environment, SCHEMA, Thread, Post, User, SubCategory
from sqlalchemy.sql import text
from chancepy import Chance


# Adds a demo user, you can add other users here if you want
def seed_lit_threads():
    user = User.query.get(2)
    category = Category.query.filter_by(name='Literature').first()
    subcategory = SubCategory.query.filter_by(name='House of Leaves').first()

    thread1= Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        created_at=Chance.date(year=2022),
        updated_at=Chance.date(year=2022),
        subject="A first time reader's thoughts on the metaphysics of House of Leaves",
        text="""First time reader. I spent a lot of time this past week puzzling over the missing pieces left to fill in this void that this book's ending left when I finished it. I read a lot of theories, both here and on the old forums, and while some of them gave some clarity and some of them pointed out things I hadn't noticed, mostly it just gave me more questions. That led to something of a realization, about the very deliberate architecture of the story and how it subtly, and rather brilliantly, gets readers engage with it. Maybe I'm retreading old ground and this has all been discussed to death. I really have no idea, but I needed to get it out so here it is:

                I think out of everything, one of the most agreed upon theories/realizations is that the book itself is the house. I mostly agree with this. The book is the physical medium upon which the house exists for us - Things that happen in the story have a tendency to 'happen' to the book, and looking at the metaphysics of book = house means that you can make simple sense of a lot of things that otherwise wouldn't make sense.

                For example, why do Navidson's pets get rejected by the house? Well, because animals can't read. How did Navidson manage to escape the house for the last time? He finished the book, and then burned it so he couldn't go back. And if you subscribe to the theory that Zampano is Johnny's actual father, what are the odds that his estranged son would find and finish his work directly after he died? Not so big, considering that, from a certain perspective, they both live in the same 'house'.

                But, with a story like this, how can you really know what's real and what's not? Johnny is, of course, a demonstrative liar. Navidson might not even exist and Zampano is dead now, he can't offer answers. It's secrets are lost, and only the scraps of the truth remained. So you begin to examine the details, to fuss over the 'real' story, trying to figure out what was changed and what is missing.

                But here's the thing: Navidson didn't create any documentary. Zampano didn't strike out any red text. Johnny didn't change the story around, he didn't damage anything, purposefully or otherwise. None of them could have possibly done any of that, and on some level you already know this.

                House of Leaves is a work of fiction.

                Ok, yeah, no shit, Sherlock. Right? Stay with me for a moment.

                The editors (abbreviated Ed. - it's easy to forget and start reading 'Ed' as a name) frequently appear in the footnotes right alongside Johnny. In some places, they imply they've interacted with him in some capacity - Ex. Page 54, where they mentioned Johnny 'declined comment' on his passage. They're a part of the narrative, they bridge the gap between Johnny's completed manuscript and our ability to get our hands on it.

                So, knowing that, if you open the book and flip past that giant title to a page that can barely be called a page, right before the table of contents, the editors, the same ones who show up throughout the story, tell you explicitly that it's a work of fiction. You flip back to the title page, and right there with Johnny's name and Zampano's name is a name, one Mark Z. Danielewski.

                The real author. The real Johnny, the real Pelafina, the real author of The Navidson Record. The one who really wrote the book.

                But the thing about that answer is that it sucks. It's a bad answer. It breaks all the rules you follow when you engage with fiction. After all, there's got to be a 'truth' in the pages, there's too many loose ends, too many things that just don't make sense. How did Pelafina know Zampano? Why did Navidson have a copy of House of Leaves? Why did his have more pages than our copies did? What were the slashes next to Zampano's body when he died? Why did Zampano suddenly refer to himself from Tom's perspective that one time? What did that stupid check mark mean?

                It's all very deliberately designed. This interaction with the author is the fourth level of the story, that being the one you experience it on. Your intro to the book is, in all ways, a facade of a conventional mystery thriller novel, meant to hook you early and hard. But the ending?

                What ending?

                It meanders. It drifts away from you, gradually. It turns into footnotes, scraps, the loose pieces. An assortment of poems you squint at to make sense of. You hit Pelafina's letters that you probably already read. You hit a fucking index looking for more content. You could read it cover to cover and it would still feel like there was something more to this, something out there you missed. And you'd probably be right. I mean, how many people really combed through all those footnotes the first time? Glazed over some weirdly formatted text? Forgot to read part of a paragraph or two just trying to follow a single trail of thought at once?

                Obviously, you missed something.

                So you make the descent, again. You go back to the book and open it up and you take the plunge and maybe get some answers, maybe make up some answers, and get more questions. Maybe you started writing in the margins. Maybe you start looking up some of those hundreds of dead end sources. Maybe you manage to decode something, maybe something someone else never has.

                Sound familiar? You go back to the house and make the descent, even knowing full well what's already there. You don't, and will never, have enough of the story for the answers to the questions you're asking, even with the answer right in front of you. You knew from the moment you opened the book that it was a work of fiction, written by a guy named Mark Z Danielewski, and you chose to engage with it anyways.

                You want your Minotaur? There it is: It's the answers you'll never have, it's the growl in the dark that tries to convince you that one day you just might, as long as you keep looking.

                I believe Johnny got out, in the end. Worse for wear, maybe, fundamentally changed as a person - Probably, but he got out. Just like Navidson he burned his copy, and with it his narration ends.

                After I had this epiphany I closed my copy of the book and realized I had to be the one to end it, because the book won't do it for me. I passed my copy, and all it's notations and tabs, along to a friend of mine. I don't know whether he'll read it or not, or what will happen to it, but that's not up to me, anymore. Either way, it seemed fitting. And only after that did I feel satisfied enough to call my experience with it done.

                For now, at least. Who knows.
              """)

    db.session.add(thread1)

    thread2=Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        created_at=Chance.date(year=2022),
        updated_at=Chance.date(year=2022),
        subject="House of Leaves - I believe I've found the profound message at the heart of this book. I might also be insane. Who knows.",
        text="""I just turned the last page and I need to get my thoughts to "paper" before they settle. Here is my understanding:

                Humans by nature have a strong desire to create meaning in events to explain/cope with them. HOL plays with this by creating an infinite amount of connections that always ALMOST create understanding, but never do. This fills the reader with anxiety with their thoughts trying to piece together meaning through chaos.

                About halfway through the book, I realized I was slowly becoming Johnny. I was staying up late, I had a huge notebook full of notes. I couldn't concentrate on anything at work. I was filling in all of the intentional "gaps" or "spaces" purposefully left in the story in an attempt to make sense out of something that is impossible to understand.

                When I started to view what I was reading as meta and stopped trying to solve the puzzle, I began searching for the solution to the problem the book was presenting me with: "Look at what happens to you when you try to understand something that cannot be understood. Why is this happening?"

                I noticed I was:

                    - Filling the holes in the story with my own thoughts and theories (just as Zampano and Johnny have been doing)

                - Incredibly anxious and uncomfortable when I kept searching without any answers

                - It was becoming obvious whoever was telling me this story wanted me to feel this way
                At this point I knew I needed to quit trying to find meaning in the spaces between the story, and instead begin searching for the meaning to the real life consequences of what the story was creating in me.

                I believe the ultimate message of the book is this: the only thing that actually exists is the current moment. Everything else is leaves in the wind.

                Here's how I see it:

                An event happens < - someone interprets the event <- someone else interprets someone else's interpretation by filling in whatever gaps in the story with their own experiences/bias and so on.

                I believe House of Leaves is teaching us this both literally and metaphorically.

                I know I'm sounding out there, but hear me out.

                Something that may or may not have happened (The Navidson Record) leaves enough gaps/holes in its story that inspires Zampano (or whoever) to project his own meaning/understanding on them. Zampano leaves enough holes to inspire Johnny to fill them in with his own understanding and so the spiral goes until we get to ourselves, the reader.

                How the book eventually reaches the reader presents the first hurdle we need to overcome. The solution? To accept the fact that is impossible to know. The more you try to understand it, the more gaps you fill and the larger the labyrinth becomes. You will always be running around, trapped in the labyrinth like the Minotaur, stirring up more and more leaves with gusts of your thoughts. Someone along the way intentionally created these gaps to help the reader draw these conclusions themselves (with editing, removing pages, etc..). Similar to Karen, trying to create meaning in her story with omission, presentation, etc...

                As it is drilled into our heads by the end of the book: we create meaning by filling in the spaces in between.

                Once we come to terms with not knowing, we can begin to see the forest through the trees.

                The text begins to read like how the author expects our brain's to work. Johnny gives us the opportunity for a distraction from the boring slog of Zampono's analysis. Taking the place of our own thoughts that normally would have occupied this space. This layer is the most confusing as it further from the actual event. Playing around at this level will have you feeling like you are insane trying to put clues together. You brain will conjure up sexual thoughts, violent thoughts, anything to distract you from boredom. I believe Johnny was created as a result of the boredom from reading through Zampano's analysis. His mother was created by filling in the gaps of his story.

                The best solution is to ignore this "layer". Once you begin to ignore Johnny (and the equivalent in your brain), you begin to realize how ridiculous it is to react to this person. He/she is completely unreliable/unhinged, and only driven by anxiety, pleasure and anything else. It's best to ignore this person completely. I also think it's interesting how he fills in the 6 minutes of silence at the end of the Navidson record with his long tirade. Searching and searching for meaning but never getting there. This part of our brain (and johnny himself) cannot stand to be bored.

                Also notice how Johnny’s voice doesn’t appear when the story is interesting. The action sequences with all of the blank areas of the page are to highlight the absence of that voice in the back of your head.

                The next layer is Zampano's. Loneliness brought on by the result of over analyzing/trying to make sense of a single event. We stop focusing on what is happening and focus on fixing/solving something in the past. Isolation, obsession, and never moving past something.

                At the end of the Navidson record, Navy accepts he is scared. He stops trying to explore the labyrinth, restraining from stirring up any more leaves. He lets the house take him where it is going to. Just as we are intended to do with this book: he burns it.

                I know there may be pieces to the puzzle I am missing, or maybe some of my thoughts could be fleshed out a little better, but I hope some of this makes sense. I think part of the point is to beware of getting lost in the details as it leads you deeper into the labyrinth.


                """)
    db.session.add(thread2)

    thread3=Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        created_at=Chance.date(year=2022),
        updated_at=Chance.date(year=2022),
        subject='House of Leaves - The Author - A Unifying Theory',
        text="""Introduction

                After reading the House of Leaves I was completely blown away with what the author managed to accomplish. The book is truly a work of art, as I'm sure all who have laid eyes on it are aware. That being said, I was surprised with the confusion and competing theories about the underlying narrative. Because of this, I felt compelled to illustrate what I took away from my most recent reading. I feel this is my final theory on the book. I believe this perspective ties the entire work together in a cohesive union.

                How to Read House of Leaves

                After multiple reads, I confidently believe that there is a "correct" way to read House of Leaves. Because there are many simultaneous (extremely well written) narratives, it has been suggested online that its totally fine to read it in a segmented fashion. I completely disagree. If you are reading it for the first time, to get the most out of it I suggest you:

                Read the book from start to finish.

                When you encounter superscript referencing a footnote, immediately stop reading (even if mid sentence) and read the footnote.

                If footnotes chain, follow the chain.

                If an old footnote is referenced that you have previously read, at least go back and re-read the first few sentences to remind yourself of the context of the footnote.

                If an appendix item is mentioned in a footnote, immediately read that appendix item.

                If page numbers are mentioned in a footnote, immediately read those pages.

                If you are on your second read of the book and a chapter is mentioned in a footnote, immediately read that chapter. (I’m not positive on this one, I’ve got another read-through coming to verify if you should actually read the chapters out of order.)

                The pacing of the book is dramatically improved if you read the book in this way. You are provided with the information you need to know, in the moment you need to know it. Some chapters rely on the footnote chains heavily. To list just a few small examples:

                On page 72 footnote 78, you are instructed to read the Whalestoe letters. After reading the letters at this point, when you reach the check mark on page 97, you will not only understand its connection to the letters but begin asking yourself: Why is Johnny’s checkmark letter response to his mother on a page that was completely written by Zampanò?

                When reading Chapter IX, following the footnotes is paramount to experiencing the maze. The footnote chains are confusing, cyclical, and require some level of intuition to navigate.

                Again in Chapter IX, following the footnotes brings us The Song of Quesada and Molino. Seemingly missing from the appendix (as you will find most missing items are actually present in the narrative) you find in its stead The Pelican Poems in Appendix II-B and Poems in Appendix I-F.

                What Is The “True” Story Being Told?

                The House of Leaves is a story written by a woman who is attempting to process the grief and trauma she experiences after the death of her child. From here on out I will refer to this woman as ‘The Author’. The linchpin moment that reveals this information to us happens in Chapter XXI. In this chapter, Truant discusses the death of his friend and admits to making up a majority of the chapter. The lies continue until at the bottom of the page of 518, The Author admits they have no more lies left to tell and provides us with the only non-fantasy piece of narrative in the entire book. It begins with the sentence:

                Except this story, what I’m remembering now, too long from the surface of any dawn, the one Doc told me when I was up in Seattle -

                The ‘what I’m remembering now’ is colored purple and struck through. Upon getting to this point we have been conditioned to believe:

                All struck through text colored red is text Zampanò wrote but wanted to not include in the Navidson Record. Truant decided to leave it inserted anyways. All passages are related to the story of the Minotaur.

                The word house always appears in blue.

                Visually when you look at the purple, it comes across as a perfect combination of the red and blue. This is the first time we see a red struck through passage within Truant's story, implying that Truant and Zampanò are actually the same person. The passage is also blue, providing us the proof that the word 'house' is synonymous with 'what I'm remembering now'. What follows is a passage where The Author finally confronts the suffering she has been avoiding writing about the entire book. She tells the story of the birth of her son, how he was born with an incurable brain injury, and how she chose to pull the plug, unable to protect her son from death. Besides these three pages, the rest of the book is simply a story The Author has invented. It's a story that, although it does not describe true events, its one that expresses the emotion and horror of her trauma, allowing her a place to begin to let it out and process it in a hopefully more healthy way than some of her characters do.

                Central Themes

                There are several central themes to the book that you find reoccurring throughout the narrative she wrote. All of these themes arise out of the life experience of The Author. The themes interwoven with the stories of Navidson, Zampanò, and Truant communicate The Author’s story and trauma through allegory. Here are some of the main reoccurring themes in all three narratives and how they are an expression of The Author’s grief over the loss of her son.

                Theme One: The unreliability of all narrators. Throughout all three stories it is established that none of the three main characters can be trusted.

                Truant openly admits to making up stories and lying about his past.

                Truant admits to modifying Zampanò’s words to make them inaccurate.

                Zampanò constantly makes up citations and references.

                The House (representative of The Author’s memories) is continuously shifting, changing, and inconsistent.

                All of this is done intentionally by The Author to point our attention away from the three storytellers. None of them are reliable because all of them are made up. This point is hit home towards the ends of both the Navidson Record and Truant’s story when it is revealed that they both read The House of Leaves. This creates a narrative impossibility of storytelling. If the three stories were true, it would have been impossible for Navidson to record himself reading The House of Leaves before Zampanò watched the film and before Truant published it. This proves to us further that all three stories are not separate, but a single work of fiction by another voice.

                Theme Two: Head injuries. The Author reveals in those three pages that her son was "[b]orn with holes in its brain". Traumatized by her child being born with such a horrendous defect, she writes about damaged heads quite frequently in the novel. Just to list a few:

                The abandoned puppy that was thrown from the car had its head bashed in on a lamp post.

                Jed's death by getting shot in the head.

                The Minotaur. Child of the king, born with a human body and a deformed head.

                Lude's death, falling off a motorcycle and crushing his skull.

                The headless cat on the street that the other cat refused to leave.

                Truant's mother's mental illness.

                Truant's hospitalization as a child when his step father beat him so badly he chipped a tooth.

                And that only begins to scratch the surface of 'head' references. Just go to the index and look up head if you'd like more evidence. It's obvious The Author's son's birth defect had a huge impact on the story she wrote.

                Theme Three: Being tormented by past memories. The motivation for The Author to write The House of Leaves was to help her process the trauma she experienced when her son was born. She is tormented by the memories, sometimes finds them difficult to recall (or face). This comes through in many narratives.

                Navidson is tormented by Delial. A child he attempted to prevent from dying but was haunted by his belief that he could have done more to save her.

                Pelafina is tormented by a dark past history that is never fully explained. She is driven mad, constantly separated from her son, longing to be with him. She is powerless to protect him in any way and can only observe what is happening to him. She feels guilty for the pain she causes Truant (emotional and physical).

                Truant is tormented by a number of things, but largely violence and death. He was tormented by the abuse of his step father (who caused him head damage on multiple occasions). He grieved for the death of his family (father). He grieved for his mothers insanity and decent into incoherence. He grieved for what could have been with the drowning of his crew mate.

                The story of the Minotaur. The maze and story is explicitly said to represent repressing the memory of a deformed child. The House, its shifting walls, and the creature stalking them share the same meaning.

                Navidson feels wholly inadequate in comparison to his brother Tom after Tom successfully saves Navidson's child when he himself was unable to do so.

                As you can see, most of these are easily directly relatable to the death of The Author's son.

                Theme Four: Having difficulty navigating spaces. With the House representing memory, navigating space becomes analogous to recollection. The Author knew she was traumatized, most likely diagnosed with PTSD. Having PTSD myself, I'm all too familiar with the memory loss, denial, and avoidance mechanisms used to run from the trauma. The book is filled with people who have difficulty remembering, making up stories as coping mechanisms (HoL in its entirety being the ultimate example), and running from their problems. Just to name a few examples that have not already been mentioned:

                Karen's closterphobia navigating the house. It should be noted that it was her love for Navidson that eventually helped her overcome the fear of exploring those halls, driven to protect the one she loved.

                Truant and Pelafina's numerous stories used to mask the truth.

                Truant and Pelafina's moments of amnesia.

                Navidson keeping Delial a secret from everyone. (Delial sounds an awful lot like denial.)

                Navidson's avoidance of addressing Karen's adultery and his history with Tom.

                In every exploration sequence, people get lost in exploring the house, fearing to go deeper, knowing that there is something to fear in the center of it all. The House itself shifts, a repression mechanism, attempting to prevent those who choose to explore it.

                Theme Five: Loneliness and the longing for someone you love. I can only imagine the amount of loneliness and longing The Author felt after losing her son. The desire to be reunited with her son and the feeling of isolation and loneliness is felt by many characters:

                Karen's return to The House to rescue Navidson.

                Pelafina being trapped in the Whalestoe, unable to reach her son.

                Truant's sexual escapades that simultaneously express the longing for affection and the loneliness inherent in impersonal acts.

                Zampanò's living situation and lack of known connection to family.

                Zampanò's multiple love interests.

                Zampanò's blindness.

                Navidson and Tom's relationship.

                Hopefully this extremely shallow dive into the themes present in House of Leaves provides some validation and clarity into how the life of The Author permeates every page of the text.

                Final Thoughts & In Summary

                The House of Leaves was written by an unnamed woman I call 'The Author'. She gave birth to a son who died just a few days after birth. She wrote the book as a way to express her grief.

                The narratives of the Navidson Record, Zampanò's analysis, and Truant's commentaries are all contradictory to one another and can not exist independently. Each is a story derived from the mind of The Author, shaped by her experiences.

                All characters in the story are fictitious and inhabit traits of The Author. They all share her struggles. The themes listed before create cohesion between the stories and make them no longer contradictory.

                The stories all progress at the same rate and follow the path of overcoming and healing trauma. They first appear living their average life. Then, a discovery throws our characters off balance and shows them something is disturbing them. They all begin to explore what is disturbing them. Then, before becoming lost in the exploration, they break past the repression and confront what is at the root of their trauma. They come out the other side changed, but arguably better of then they were before.

                The House of Leaves in its entirety is an allegory of The Author's journey, most likely including all of these elements. Unfortunately, we only get to see her true voice for 3 pages when she finally faces her trauma head on instead of obfuscating her story in false narratives. Despite this, the emotions she felt and her journey were definitely expressed and known in feeling if not in word.

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
        subject="House of Leaves - Zampano's scratched floor",
        text="""Going through the reflection process after my first read through, as I'm sure anyone on this sub has experienced.
                Reading theories and analyses and so on. I'm sure most people here have read a bit about what the minotaur represents.
                While thinking about it though there is one loose end or red herring I've just recalled:

                The scratches on Zampano's floor. Naturally the point of this book is to get lost in speculations
                and answer-finding, but this point stands out to me because of how comparatively concrete a detail it
             is in relation to a lot of other question-generating aspects of the book. There's no obvious reason why
             Zampano would have made them, they do suggest claw marks. They are found by Johnny at a time before he's
            invested in Zampano's work, but the story in which he finds them is recounted in October of 1999 well
            into his spiral. Is there anything more to the scratch marks, or is it just a red herring suggesting a
             physically manifested creature that the book does not need to explain because of the nature of the narrator?
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
        subject="Creepy personal connections in House of Leaves",
        text=   """I finished House of Leaves this weekend and LOVED it. It was creepy as is, but then I found out something even creepier. My mom is a Bancroft. I texted her after I finished the book to find out if our family was related to Hubert Howe Bancroft (mentioned 3 times throughout the book, one as an image at the end). She confirmed, I'm a descendent of HH Bancroft. There's another image at the end of the book that contains a note about a party of people in the 1800s near Fort Vancouver who got lost after finding a a stairway, which was later destroyed in a St. Helens eruption. I live VERY close to the Fort & the mountain and have summited St. Helens three times. It just really creeped me out how this book started hitting close to home. Had to share with folks who'd understand.

                Aside from that, here's my theory on the book (SPOILER, maybe):

                I think Johnny made the whole thing up, without realizing it. I think Johnny really believed that he was reading the manuscript from Z, but actually just didn't remember writing it himself during a series of psychotic episodes. Certain themes kept popping up between the three characters that didn't really make sense. For instance, Johnny, Navidson, and Z all commented on women's wrists. Which doesn't make sense. Wrists aren't a common thing for people to be attracted to in other people. But because of Pelafina's attempt at strangling Johnny, maybe he now has a strange association with women's wrists. Evidence of Johnny appeared in all the characters in the form of "echos," such as the wrist thing. I have some other examples, but don't have the book with me right now.

                Feel free to agree or disagree. I'm not 100% attached to the above theory so would love to hear proof as to why I might be wrong.
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
def undo_lit_thread():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.threads RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM threads"))

    db.session.commit()