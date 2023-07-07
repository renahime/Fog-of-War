from app.models import db, Category, environment, SCHEMA, Thread, Post, User, SubCategory
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_uzumaki_threads():
    user = User.query.get(1)
    category = Category.query.filter_by(name='Anime Manga and VNs').first()
    subcategory=SubCategory.query.filter_by(name='Uzumaki').first()
    thread1= Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        subject="Uzumaki Ending. Is it a display of lazy writing or completely fitting?",
        text="""<p>I just finished the story and went online to see what others thought of the ending.

I was surprised to see so many people hate the ending, especially for lacking an explanation.

The way I saw it, the story was fairly clear. Some cosmic entity known as the spiral had existed in the town for who knows how long. Every so often, it would make its presence known to the townspeople in order to rebuild itself. During this time, the town was under a curse, and horrible things would happen as people lost their homes and their humanity to the will of the spiral. Only after the spiral had rebuilt itself (through completion of the connection of old row houses on the surface and a subsurface structure), would the curse be over. But with that completion, all who were part of the town would perish with the spiral. Only after many more years went by would this process start over.

The portion of the ending that has gotten people miffed is the two protagonists giving up even though they seemed to be close to finding a reason and possibly a solution for how to end the curse. I've seen people say this is both lazy as well as pointless, because the characters had no impact on the story whatsoever. Furthermore, neither they nor the readers found any detailed answers for why the spiral would stop being dormant every so often in order to rebuild itself.

For me, this ending is very fitting. Everything in Uzumaki, the characters, the setting, even the plot, is captured by the spiral. Suichi mentioned how spirals trapped things naturally because of their shape, so that theme was extended to everything including the mechanics used in the writing, and I think it's pretty brilliant. Spirals are repeating shapes just as the town's curse is repeating, and just as the eye can't escape the center of a spiral, the townspeople couldn't escape the being devoured by the spiral either.

To me, Ito's intent was never to explain the spiral or the curse or anything beyond what we needed in order to enjoy each passing tale. Neither knowing the cosmic entity's (if it was that, we still don't have a real explanation for what the spiral was, either) intentions nor having a happy ending would have made the story better. I personally think adding lore would have watered Uzumaki down, and having a happy ending would have felt out of place, because it would not only ruin the entire spiral motif (spiraling out of control, for instance), it would have felt unlikely for these two people to make a difference that thousands of others couldn't. The spiral was something bigger than them and humanity in general, so making the characters helpless felt right.

I think the point of the main characters was to give the reader people they could identify with and share a journey with. But like a big storm or some act of god, the spiral was going to do what it was going to do regardless of whoever the main characters were.

There are some theories I have read online (or thought myself) about the spiral. Is it a metaphor for society or death? Conversations could go on for days on how to interpret the meanings presented in this story, but I rather not do that now. If I just took the story as literal, I'd still find plenty of substance.


</p>""" )
    db.session.add(thread1)

    thread2=Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        subject='A philosophical interpretation of the spiral in Junji Ito’s Uzumaki',
        text="""<p style="margin-left:0px;">Junji Ito is a popular horror manga artist for very good reasons, his art adds something new and unique to the medium. Everyone has their own story on how they first heard of Ito. For me, I first got into his work, as most people might have, by reading some of his short stories that get mentioned on social media or used for aesthetic blogging purposes. The first story I read of his was <i>Gyo </i>(2002) during my sophomore year in high school. It was extremely absurd, but still had a certain charm to it, I definitely consider it one of the best chemical warfare/sea monster horror spin-off stories out there, although can’t say I know many anyway. Ito seems to focus heavily on abstruse themes such as the dread of facing unexplainable and hopeless events. In some of his other works, such as <i>Hellstar Remina </i>(2015) and <i>The Enigma of Amigara Falls </i>(2002), one cannot quite get a clear cut reason for <i>why </i>and <i>how </i>his stories play out. Even though his characters can be rather bland, transparent and unrelatable, his stores still offer refreshing tales of cosmic horror.</p><p style="margin-left:0px;">I read one of his most popular works on an airplane a few summers ago. I was on my way to visit family in Albania, and the ride there from Pennsylvanian is always long and dull. I am also one of those people who has a difficult time falling asleep on a plane (poor us). While everyone else was asleep, as it was a bit past midnight, I was reading <i>Uzumaki</i> in the dim atmosphere, the only light I had to assist with my sight was the one overhead of my seat. I felt anxious at the possibility that my mom or the person sitting behind me would glance over and see the pages of grotesque body horror in front of me–that’s just how Ito rolls. <i>Uzumaki </i>can be hard to get directly into. The narrative style of Junji Ito can seemingly be non-linear and confusing, but this is also one of his strengths in creating an intriguing story.&nbsp;By the time I finished, the plane was preparing to land at my first stop on the outskirts of Frankfurt, Germany. I couldn’t stop thinking about it…the spiral…</p><p style="margin-left:0px;"><i>Uzumaki</i>, which is<i> </i>Japanese for spiral (うずまき), tells the story of Kurouzu-Cho, a small town that becomes contaminated with spiral patterns. The spiral structures manifest themselves not only in the physical environment but also on human bodies, sometimes consuming their whole being and reducing them to nothing. The ways in which the spiral gradually takes over the city is interesting; it evokes a visceral kind of terror. If you have ever spent some time looking at spirals, you would understand the deep, unsettling feeling you get from prolonged staring. Spirals are essential in any “how to do hypnosis 101” guide; it exhausts your eyes, your head gets dizzy, you physically can’t focus on it for any longer, and the moment you look away, your perception is temporarily altered. I recall a magician that was invited to my high school each year, and one of his acts always involved a spiral board that would visually deceive us; his head would either became smaller or bigger, his body would shrink or grow, or whatever other witchcraft tricks he had in his pocket. An animated spiral could just continue endlessly. It’s a “my small human brain can’t possibly fathom the unknownness of the center” type of experience. Junji Ito had a similar revelation. In the omnibus version of <i>Uzumaki</i>, Ito published a very short manga at the end of the book about his journey of, what he called, tapping into “the secrets of this enigmatic shape.”<i> </i>He states that he spent hours staring into the depths of where a spiral inwardly spins off to. He also tried to read all the references he could possibly find on this weird geometric shape. He ate foods that were spirals, stared at the spiral nature of a snail’s shell, but this all led him to nowhere in particular. He was left at the complete mercy of this metaphysically mysterious shape.</p><p style="margin-left:0px;">The story spins off with the main character’s, Kirie Goshima, boyfriend’s, Shuichi Saito, father who becomes increasingly fixated with the mesmerizing shape of the spiral. All his ceramic work suddenly takes form of a spiral and then he starts avidly collecting spiral objects. When his wife throws away his collection, he comes to the realization that he <i>himself </i>can transform his body into a spiral. This ultimately leads to his twisted death, as well as the initial point of chaos that wrecks the town.</p><p><br>The wife eventually falls ill after the funeral, convinced that her husband is trying to compel her to join him in this abject realm of the “spiral.” She finds that spiral patterns naturally belong in a lot of places of the world, such as her own body, which leads her to graphically remove body parts such as her fingerprints and the cochlea inside her eardrums. The pervasiveness of the spiral in this context could be analogous to extreme anxieties we experience in our normal lives that unravel us in overwhelming ways; the ultimate manifestation of our fears, obsessions, and desires. It can also represent the instability of the future. Life is in constant flux, this follows the never-ending motion of the spiral.</p><p><br>A more abstract interpretation of the spiral is that it embodies the inconceivable concept of infinity, and this is especially apparent in the conclusion. Every horrible event that has occurred in the story shall happen once again for an eternity. It is unavoidable and inescapable. This immediately reminded me of&nbsp;Friedrich Nietzsche. I had worked closely with his work in the beginning of my undergrad years. Our relationship is a little complicated; I don’t particularly enjoy his wailing nihilism or his view of women as weak, which seems to be a common theme in 19th century philosophy. Besides the point, he had this peculiar conception of eternal recurrence. Of course, he wasn’t the first one; he only offered a modern interpretation to something that has been contemplated by many ancient cultures and religions. This theory of the “eternal return” can be found in Indian religions, Ancient Egypt and certain Mesoamerican cultures.</p><p style="margin-left:0px;">Following the likes of Schopenhauer and Hegel, Nietzsche was influenced by Asian thought, especially Buddhism. His personal relationship with Buddhism followed polemic episodes and contentious misunderstandings, as well as conceptual inspirations, namely life as illusion (Samsāra), suffering, and emptiness. Although, Nietzsche’s cosmological idea of the eternal recurrence of existence takes the spot. One particular deviation in his concept of the eternal recurrence is that it is constituted by sameness, meaning our lives will play out exactly the same way, with no alterations, in the next round. This sounds pretty insensible. How can my life and everything that has happened on this world have occurred infinitely before and will continue to occur for infinitely more? Don’t we have free will? Don’t the actions of communities dictate the course of history and the future? Much to think about…</p><p style="margin-left:0px;">In <i>The Gay Science </i>(1882) Nietzsche offers this thought experiment:</p><p style="margin-left:0px;">“What if some day or night a demon were to steal into your loneliest loneliness and say to you: ‘This life as you now live it and have lived it you will have to live once again and innumerable times again; and there will be nothing new in it, but every pain and every joy and every thought and sigh and everything unspeakably small or great in your life must return to you, all in the same succession and sequence – even this spider and this moonlight between the trees, and even this moment and I myself. The eternal hourglass of existence is turned over again and again, and you with it, speck of dust!’”</p><p style="margin-left:0px;">Nietzsche’s perspective highlights the futility of existing at all; the universe was not made for us and we do not know where we fit, we just go through endless forlorness. The real test is if we can learn to have affirmation of our life in this infinite cycle that is the exact same each time (mostly by the balance of aesthetics in the aspect of the Dionysian and Apollonian dichotomy). He also thought that the eternal recurrence would overcome any empty moralities, dualism and Christian otherworldliness.</p><p style="margin-left:0px;">While Nietzsche exclaims that we should just try and find joy in a joyless life, Buddhist teleology imposes a complete removal from this eternal cycle of rebirth and suffering. The first of the Four Noble Truths states that the fundamental reality of life is qualified by Dukkha<i>,</i> or suffering. Mahāyāna Buddhism exemplifies that we are not supposed to accept this infinite cycle of suffering, we are to actively go against it in goal of salvation from the sickness of existence. One can achieve happiness and the absence of any physical and mental pain through Nirvana; it is the optimal state of healthiness, a state in which all things are unified and there is no differentiation.&nbsp;</p>
""")
    db.session.add(thread2)

    thread3=Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        subject='The nature of the Uzumaki spiral',
        text="""<h2>Dude, this story was incredible to read. I was scream crying (quietly) in the park at the end for like, a minute. I revisited the last few panels multiple times, just to experience the swell of emotions again.

That being said, I have a theory. Spoilers ahead.

So, no one can escape the town, right? Why? Because of the spiral. I’m going with the explanation that you can’t escape the town once you have the spirit of the spiral within you. Once you’re infected, you become a part of the spiral— and the ritual associated with it.

Note how the curse wasn’t over until Kirie and Shuichi finally gave in? It’s because they had the spiral within them. Throughout the story, people keep mentioning how the “spiral is inside them”. The spiral needs every piece of itself in order to be complete. That is why the spiral doesn’t let anyone escape. If anyone left with a piece of spiral, the ritual would never be complete.

Kirie and Shuichi didn’t suddenly become infected in the last pages— they had been infected for a long, long time. Think of it like, being asymptomatic, but still infectious. When Shuichi sees his dad in the spiral of the tree stump, we know he’s infected. He’s manifesting the same symptom his mom had. To be honest, Shuichi has probably been infected since the beginning. His family was ground zero, after all. But, due to seeing the deterioration of his parents, Shuichi chose to resist the spiral from the outset. His strong, willful resistance is why, despite being infected, he didn’t manifest visual symptoms. As for Kirie, we know she was infected earlier on— since the hair chapter.

Other notes on the idea of transmissibility: the first snail chapter. It wasn’t random people who turned into snails. It was the people who fucked around/harmed the snail people. Meaning they contracted the spiral from the snail people, or the interaction provided the catalyst for the spiral already within them. Also— it’s always family/friends/people in close contact that manifest symptoms next.

The hair chapter is what I want to talk about, though. This is one of the few instances I can think of where the spiral manifested physically, but the manifestation was able to be reversed (well, at least for Kirie). The only other one I can think of right now is the warts chapter. There may be more, though.

Going into this chapter, Kirie’s hair is spiraling. The spirals take all of her energy, and refuse any attempts to be destroyed. It’s only after fighting another student with active spirals that the hair is capable of being cut, and the symptom is stopped. The spirals are no longer draining her energy, and Kirie is able to return to normal.

Now, there are a few ways to interpret this. Going with the “the spiral acts like a spiritual virus” theory, we have two infected individuals interacting with each other. Oftentimes, more exposure to a virus leads to more rapid disease and a higher likelihood of severe symptoms. sauce So that would explain why after direct contact, the other girl’s condition worsens expeditiously. However, it doesn’t explain why Kirie’s affliction seemingly has the opposite effect, and disappears. Which leads me to the conclusion— Kirie unknowingly transferred enough spiral spirit to alleviate her own symptoms, and consequently, worsen those of the other girl’s.

Now, I’m not saying Kirie was free of the spiral’s influence after the fight. She could’ve still had some influence remaining, left over. It simply would’ve been residing within her, dormant for the time being. A big part of not manifesting symptoms is willpower, right? Well, throughout the rest of the story, Kirie is actively fighting the spiral’s influence. However, when the hair was stealing all her energy, she didn’t have the strength to maintain that resistance. But the important part is, she was able to transfer an amount of it, and had less after the fight then before.

This alters my analogy for the spiral’s influence. Instead of modeling it as a virus, imagine it as a bacterial infection. Something that has a more centralized origin of infection. Something where, if you target the source, you can eliminate the illness.

Hear me out: If some of the influence in a host can be removed, why not all?

Which leads me to my new theory: “Purge the Poison”.

The spiral’s influence can be purged from a person’s body. I don’t know how, or why. Maybe it has something to do with the nature of the spiral, and how it pulls everything in. So when one instance of the spiral encounters another, the influence of one is pulled into the stronger of the two. Following this theory, it stands to reason that a particularly strong influence could pull out the host’s influence entirely— curing the host. At that point, whether or not the host would have immunity or be at risk for reinfection, I can’t say. But, theoretically, the spiral’s influence can be cured.

Alright, we have a theory. Now, how do we apply it? Basically, there would have to be a conduit. A host-object, that is VERY strongly infected with spiral influence. Like, ultra potent. This conduit would act almost as a black hole, dragging in everything around it.

After obtaining said object, the user would have to somehow transfer the spiral influence within their own body into the object. How, I don’t know— Kirie did it with the girl unknowingly. But the channel for transfer would have to be opened, consciously or unconsciously.

After purging the influence into the object— get the fuck out of town. The former host would have to leave as QUICKLY as possible, to minimize the chance of reinfection. And it is possible to leave, if the spiral hasn’t infected you. After the first two storms, a mass of people moved out of town, opening up space for Kirie and her family to move into one of the rowhouses. The people who left, assuming they were successful, got out before being infected.

Now, how could this theory be incorporated into the story? It’s clear that objects can be influenced— see, Kirie’s father’s pottery made of clay from the lake. So a literal object, thing, item could be the conduit. However… there’s a more compelling option.

Junji is not a stranger to cults, and apocalypse induced mob mentality. Sensor and Remina are excellent examples of that. Junji’s also used conduits before, in his work. And in those instances, the conduits… were women.

You’re telling me, in a hell scape of tornados and snail people, not a single group of survivors have formed a cult? People search for explanations. Disasters and dystopia make people search for something, anything, to restore a sense of order and power. It’s why conspiracy theories are a thing. It especially makes sense for such an organization to form when the inciting event is literally warping their minds. So here’s my proposed, alternate ending for Uzumaki.

It’ll be in the chapter after facing off with the tornado gangs. Kirie and her group run into a cult. Either 1. This cult worships the spiral and chooses to sacrifice Kirie to the center, or 2. The cult formed after someone managed to escape, they determined the need for a conduit, and have chosen Shuichi due to his long exposure. You can add as much “the spiral told me”, “you’re the chosen one”, etc. for flavoring as you want. In the case of situation #2, there could be a line like “You father was the first to turn, wasn’t he?… And your mother wasn’t too long after that, either… yes, it all makes sense. You would make the perfect vessel”. Make them batshit unhinged, go ham.

The group is abducted, and the ritual begins. Through some clever deus ex machina, the ritual goes terribly wrong and backfires on the cult. All the cult members a melted and morphed into one being, like the people in the rowhouses eventually end up. They have become the conduit, and Kirie and the group have been purged of the spiral’s influence. They immediately escape, not looking back.

Is it as poetic, romantic, and beautiful as the actual ending? No. Not even close. I’m not Junji, and not going to lie, I’m spitballing right now. But— it lets Kirie and Shuichi live regular lives. Traumatized, but free.

FREE. The part that made me so sad was how fucking HARD they tried, man. They tried SO hard to beat the spiral, it sucks to see them fail. You know the joke about how people in horror movies are dumb, and make stupid decisions that get themselves killed? Kirie and Shuichi DIDN’T do that. They did everything they possibly could, and it wasn’t enough, and that’s fucking HEARTBREAKING. Let them be free!! They earned it!! They deserve to move on and have as close to regular lives as they can. Let Shuichi see a fucking therapist, like goddamn. They deserve to heal.

And that concludes this post. Thanks for stopping by, let me know what you think :) stay away from spirals.</h2>"""
              )
    db.session.add(thread3)
    thread4=Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        subject="I just finished Uzumaki and I have a theory (spoilers)",
        text="""<p>Hey guys, before you keep reading this is a major spoiler alert if you haven't read it yet!!!

.

.

.

.

.

.

.

.

So, I'd like to start a conversation on the nature of the entity encountered at the end of the manga. Here are my thoughts thus far:

- Uzumaki, which is what I will be calling 'it', is akin to an elder evil. If you haven't read H. P. Lovecraft, it is clear Junji Ito draws inspiration from him, particularly in this work. Essentially in Lovecraft's writing, he describes the elder horrors encountered by himself (writes in the first person, much like Junji writes himself in as the main male character) as unspeakable and unknowable. Extrapolate that to Uzumaki and you have manga that allows the writer a means to express themes swirling spirals and horror together. Uzumaki, in essence, is Junji Ito's equivalent an unspeakable and unknowable entity.

- Junji did a lot of research into spirals, and I mean a lot. In the manga, the characters theorize this event has happened before, perhaps every couple hundreds of years. But, upon pondering this I came to the conclusion that perhaps it is always happening. What happens when light reaches a black hole? IT SPIRALS.

The photon sphere is located farther from the center of a black hole than the event horizon. Within a photon sphere, it is possible to imagine a photon that's emitted from the back of one's head, orbiting the black hole, only then to be intercepted by the person's eyes, allowing them to see the back of their head. For non-rotating black holes, the photon sphere is a sphere of radius 3/2 rs. There are no stable free fall orbits that exist within or cross the photon sphere. Any free fall orbit that crosses it from the outside spirals into the black hole. Any orbit that crosses it from the inside escapes to infinity or falls back in and spirals into the black hole.

... essentially time ceases to exist for particles that reach the asymptote of the event horizon. So Uzumaki is essentially a timeless, extra-dimensional entity.

- This where I start to get a little crazy. Now imagine that our universe is one of many potential universe that are simultaneously happening at any given moment in time. There are an infinite amount of possibilities due to an endless amount of actions that can be performed by anything everywhere in the known universe. Therefore there are an endless amount of timelines that Uzumaki can inhabit.

- Getting a little more back to the horror topic, what if Uzumaki travels to infinite alternate timelines of Kurōzu-cho in order to consume matter to support it's endless spiral? Ergo, it's always spiraling and always consuming.

Hope this isn't too long or quacky for everyone, I'd love to hear what you all think.</p>"""
        )
    db.session.add(thread4)
    thread5=Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        subject='Secret history of the Uzumaki boruto theory (part 1)',
        text="""<p>Let’s see if this gets downvoted:

The Uzumaki are said to live for a “really long time before dying.” However, due to constant war and people fearing them due to their superior “Sealing Jutsu”, the Uzumaki Clan was wiped out. The ones that remained took refuge in various parts of the world - Naruto wiki

The reason I put this here is:

if the uzumaki’s specialty is “sealing jutsu”, does that mean “all sealing jutsu” including ones that give you a power up? ( bykugou seal, curse mark, karma ?) in the time travel special, urashiki could not steal chakra from kid Naruto, and Sasuke implied that it was because of the seal on Naruto’s stomach, which was created by the Uzumaki Clan, are they implying that sealing jutsu is the way to defeat a Ohtsutsuki?

Naruto as a adult would have his seal undone due to his and Kurama’s relationship, which is why momoshiki was able to steal his chakra so easily.

So how were the Uzumaki Clan defeated, and even more important why didn’t the leaf village help them?

Theories aren’t concrete on this one. Some say they we dealing with their own conflicts, which is possible, but I still think It’s kinda weird that as big of allies as they were they wouldn’t help them, unless they don’t remember everything about the conflict.

I believe that the Uzumaki WERE wiped out but not by some no-name clan, they were wiped out by an Ohtsutsuki; why? If they were on the verge of creating their own versions of “Karma” it possible that they were taken out because they were getting too close to the truth about the world;

But why don’t we remember this? Answer: “Omnipotence” history was rewritten in the past and momoshiki knows this, which is why he says:

“Have you never contemplated, how many times an Ohtsutsuki who became a god, may have manipulated humankind’s memories” ? - Momo ch. 79

Something to think about …</p>""")
    db.session.add(thread5)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_higu_thread():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.threads RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM threads"))

    db.session.commit()
