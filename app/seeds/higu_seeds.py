from app.models import db, Category, environment, SCHEMA, Thread, Post, User, SubCategory
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_higu_threads():
    user = User.query.get(1)
    category = Category.query.filter_by(name='Anime Manga and VNs').first()
    subcategory=SubCategory.query.filter_by(name='When the Cicadas Cry').first()
    thread1= Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        subject="Speculating at the end of the Question Arcs",
        text="""<p><span class="text-huge"><strong>Speculating at the end of the Question Arcs</strong></span></p><p><span class="text-big">I'm a new fan, having been going through the visual novels, without having seen either anime or read the manga. The afterparty at the end of Himatsubushi told me to speculate and come up with theories before proceeding, and not knowing anyone else at the same point in the story as me, I'm going to put my guesses up on reddit because I've found that fans of a series always enjoy seeing newcomers guess at things the older fans already know the answers to. Of course, I cannot prove that my guesses aren't informed by knowing what comes later, so other newcomers beware. And older fans, please don't give answers in the replies. (Or "vague" hints that can be put together by anyone who thinks about it for two seconds)</span></p><p><span class="text-big">My general theory so far is that there are two supernatural forces at work. One is Rika, to much noise has been made about her potentially being the incarnation of Oyashiro-sama, and her predictions were to accurate to discount. She has some capacity for future sight, but her comments about Ayakasa being unlikely to have survived his arc leaves me thinking that she sees a cloud of possibilities, not an absolute timeline. This theory would also line up with the Tips about her wishing for rain when the sun is forcast, because she doesn't like to know absolutely what will happen and hopes for the longshot possibility to come through. The different routes might be Rika mentally shuffling around different starting conditions in search of a happy ending in her predictions.</span></p><p><span class="text-big">The second supernatural force I'm going to refer to as "The Curse". I'm not sure exactly where it comes from, or what it seeks to accomplish. It might have originated from Rika as something to unleash on the dam project, but have grown out of her control, and she can't put it away now that the Sonozakis have handled the matter. Either way, I think the Curse acts a supernatural madness, altering the perceptions of anyone it takes hold of, and driving them to violence. I believe it hit Keichi in arc 1 and arc 3, and Mion (possibly Shion) in arc 2. Some of Rena's actions in arc 1 just don't seem to line up with her general slasher demeanor, worrying that Keichi was acting like Satoshi and standing outside his house apologizing for hours in the pouring rain feel like her trying to reach out to a friend becoming lost to paranoid delusions, not the acts of a murder. It's a similar case in arc 2 with Mion, though her comments about fighting a demon imply she was more aware of the Curse overwriting her mind.</span></p><p><span class="text-big">Some more random loose thoughts and theories, not connected to the big mystery. I would not be at all surprised to discover they pulled another Mion/Shion switchero on me in arc 2, and Shion was the one doing the killing and torturing. No real in setting justification, just a meta feeling that it'd be the sort of twist to happen.</span></p><p><span class="text-big">Rika's death in arc 3 might have been an assisted suicide, seeing that this timeline was fucked and deliberately sacrificing herself to wipe the slate clean. I took a long break between arc 2 and 3, so my memories of the former are fuzzy, but if she was indeed killed according to ritual in arc 2, there must have been some difference to prevent the gas explosion (assuming it is indeed a supernatural manifestation of wrath). Nobody seemed to have any killing intent towards her, so that's what I'm going with.</span></p><p><span class="text-big">Takano is up to something, even if I regard Keichi's perspective as unreliable regarding that night in arc 3, the implication that there was a body in her trunk was very strong. Maybe Tomitaka's, though unless details changed regarding his death in arc 1, it feels like it shouldn't quite line up. Either way, she's been fishy as hell in every other arc.</span></p><p><span class="text-big">While I don't think Rena was in murder mode during arc 1, I am pretty much certain that she is bat shit crazy regarding Oyashiro-sama. Mion's confession that the Sonozaki family was behind all the murders in Arc 2 doesn't seem to line up with the dam project already being canceled behind the scenes, so that casts doubt on the level of purging sinners they went to, especially killing Rika, so I take all the information delivered there with a grain of salt.</span></p><p><span class="text-big">I have absolutely no idea what to make of Keichi seemingly being able to curse people with death in arc 3, so I'm not accounting for it in my main theorizing, aware it could throw a wrench in it. If arc 4 took place in the same timeline as arc 3, then Ooishi still being alive casts doubt on it being causation, especially since Takano wound up in a burning barrel in Arc 2 anyways. (Though I seem to remember something about it not actually being her, the gap in how close I played them might be screwing me here because I can't remember). Arc 4 could just be a very similar timeline, since the conversation between Akasaka and Ooishi referred to multiple survivors, rather than just one, though that could have been village residents who were just out of town at the time and didn't warrant mention in Arc 3.</span></p><p><span class="text-big">Also, not a theory, but the song "fascism" is way to good, I'm jamming out to it instead of being scared during the most intense parts of the story.</span></p><p><span class="text-big">All told, I'm really enjoying the story, looking forward to playing the other parts of the VN, at which point I might watch the anime as a quick revisit to see what foreshadowing I may have missed.</span></p>""" )
    db.session.add(thread1)

    thread2=Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        subject='Hey guys, just finished the four question arcs.',
        text="""<h2><strong>Hey guys, just finished the four question arcs. Let's "discuss". (Spoilers)</strong></h2><p>I couldn't find any discussion threads for completing Higurashi games on Reddit, or elsewhere really. So here we are!</p><p>First off this series is so good. My progression of visual novel gameplay has the same order when listed either chronologically or in ascending order of personal rating. I got lucky because each game I played I decided it was my favorite, but then the next, from a personally objective point of view, blew my mind anew and overshadowed the previous. In order:</p><p>Ace Attorney. Danganronpa. Zero Escape. And now, Higurashi has taken the crown.</p><p>The escalation is great. I also love how clever the author is. I remember reading somewhere that the author was a hack. I strongly doubt that but I look forward to completing all of his works so I can look into that accusation without getting spoiled.</p><p>Anyway, his sense of misdirection is great, and he is clearly flaunting it with the Mion/Shion deception. Also, the open question of man/myth/mix is a great overall, thematic-level mystery.</p><p>I read that Onikakushi and Watanagashi are actually not that hard to solve? Has anyone actually been able to solve them? Did you discuss with your friends, or look up hints?</p><p>That moment in Tatarigoroshi's tips, when the child abuse statistics were being displayed, and then suddenly at the percentage of child abuses being sexual, the shrill music playing... That scared the shit out of me, and broke me. Throughout the entire second half of the game, I think I said that I would kill Satoko's uncle more times than Keiichi, and meant it.</p><p>I really like Akasaka by the way.</p><p>I've heard that everything gets answered, and also that there are only a few tiny plot holes fans have noticed.</p><p>By the way, what's with the 20 different arcs? I had though it was just 4 question arcs and 4 answer arcs. Are all of them translated in English, or if not, contained in the anime?</p><p>Here's a few theories I have, or at least the interesting ones. Even if they don't make sense together, or at all.</p><ol><li>Rika is actually Oyashiro-sama BUT she is limited in her abilities, and has no involvement in the crimes.</li><li>She is causing "time loops" (I think I was semi-spoiled about the idea of time loops, although I think the person who mentioned it only meant that different events happen in different games during the same time frame), so that she can manipulate variables and try to tease out different hints to solve the mystery.</li><li>However, the actual murders are by humans and are coincidental, and the Watanagashi is only used as a convenient front to that end.</li></ol><p>There's still so much I don't get though. Someone said in this sub that Onikakushi and Watanagashi are solvable with just a few insights (especially Onikakushi) but I can't begin to comprehend the time differential of the times of death in Watanagashi's ending, or why and what was injected into Keiichi and why he scratched out his neck and what was behind him.</p><p>My roommate theorized that it was a hallucinatory drug and most of the other arcs are somewhat hallucinated but come on that's way too cheap. And unless it gets explained I don't want to buy into the theory that there's magically a drug that cannot be detected by the police and yet is specific enough to get two different people to claw out their throats. Even the Yakuza can't have access to that kind of stuff.</p><p>Also I feel like Oryou Sonozaki is the kind of person I would hate in real life.</p><p>My mind is a complete jumble right now so for now, thanks for reading this mess of my stream of consciousness. By the way is it safe to browse around for posts that are not tagged as spoilers in this sub? Or should I stay off? I've had a bad history with spoilers and the previous VNs I've played.</p><p>Thanks and, please, I only want one thing.</p><p>Please find the truth.</p>""")
    db.session.add(thread2)

    thread3=Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        subject='Theories after reading Higurashi question arcs',
        text="""<h2><strong>Theories after reading Higurashi question arcs</strong></h2><p>Hello! I've finished reading the question arcs (and the first 6 or so chapters of Meakashi) and really enjoyed myself. I figured I'd post my theories here in case anybody enjoys reading those, and so I can easily look back on them after finishing the answer arcs. I'll admit, I'm at a loss as to most of what's going on, but I guess that's what makes the speculating fun.</p><p>To start, I have been spoiled on two things:</p><p>Someone confirmed that the "director" in Onikakushi is indeed Irie after I expressed some suspicions that it might be him. I didn't want it confirmed, but since I already suspected it, I guess it doesn't change too much.</p><p>There is a time loop occurring, although I don't know the details or extent of it.</p><h2 style="margin-left:0px;">Theories:</h2><p><strong>The Culprit:</strong></p><p>In Watanagashi Mion admitted to being directly or indirectly involved in most of those murders, along with the other 3 families, which I believe, at least for that chapter. But I don't think she's the mastermind, if such a person exists. I also doubt it's any of the main kids, but I still feel like I hardly know Rena, so who knows. Takano seems so fishy that I can't help but feel that it has to be a red herring. Besides, she strikes me as someone who enjoys observing the killings rather than directly causing them. Also, she dies half the time. Kimiyoshi is part of the three families, but I don't really know enough about him to even formulate a proper motive.</p><p>This leads me to Irie. I already know he's the "director", whatever that entails. He's also a doctor, and while that doesn't necessarily make him a pharmaceutical genius, it would provide some sort of connection to the syringe and the drug inside. About that...</p><p><strong>The Drug:</strong></p><p>My best guess as of now is that it either revives people or prevents them from truly dying. After all, we've seen multiple occurrences of people being seemingly resurrected at this point. Maybe it only works this way on Hinamizawa natives by awakening their inner demon. It would explain why Tomitake and Keiichi instead had a "bad reaction" and scratched their throats out. I also think this is what caused Rena and Mion's transformation at the end of Onikakushi, where their sprites had blue eyes and they were truly crazy. It would also explain why they seemed to respect the director, Irie, so much, if he is indeed their mastermind.</p><p>That said, I can't really think of a motive for Irie. He seems more sympathetic to the Houjous than nearly anyone else, and they are often the target of the annual killings/disappearances. That said, if the 3 families truly are responsible for the majority of those, it's possible his motives lie elsewhere, though I'm not sure what. Maybe he's just a cliche villain that wants an army of demons under his control, or something. Honestly, no one seems like a super obvious culprit at the moment, so I wouldn't be surprised if it's not him.</p><p><strong>The Disaster:</strong></p><p>I'm assuming this is related to the time loop that I've been spoiled on (although it is heavily foreshadowed in Himatsubushi). I'm thinking that Rika, having actually inherited divine powers, is using them to create the loop, maybe even unintentionally. She's likely trying to prevent her death and/or the disaster until a successful loop occurs where neither happens. I can't fathom why the culprit wants her dead though. Maybe the disaster is related to Onigafuchi somehow? Really vague on this in general.</p><p><strong>The Curse:</strong></p><p>This is where I'm at the biggest loss. Since I've read the first half or so of Meakashi too, the curse and "extra footstep" have been brought back to the forefront. My only guess is, maybe the footsteps are "echoes" from other time loops? And the curse is also being conducted by Rika, not to torment people, but to help prevent the disaster? Maybe all the main cast plays a part in preventing it, so this helps ensure they stay in Hinamizawa in order to do so? I could see the story heading in that direction. It would explain why the curse only affects certain people, and not, say, Rena's parents, who have no role to play. Since Satoshi was affected, maybe he needs to be revived like some other characters seem to have been?</p><p>Sorry, I know this got really longwinded, but if you read this far I hope you at least found my theories entertaining, regardless of how crazy or off-base they may be!</p><p>Edit: Thinking more about it, Takano is a nurse at Irie's clinic, so they could very well be accomplices. I always wondered why she only disappeared in Onikakushi, but was killed in Watanagashi. It's very possible she only faked her disappearance. But I still don't know what any of this means as a whole.</p>
             """
              )
    db.session.add(thread3)
    thread4=Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        subject="Let us discuss Higurashi Hou’s Question Arcs before Meakashi hits",
        text="""<p><span class="text-huge"><strong>I finished the Question Arc of Higurashi and wanted to share my thoughts with you</strong></span></p><p>I finally reached the halfway mark and I have to say it's been an absolutely amazing experience so far. I'm a big horror fan so I was a bit skeptical that a VN can actually induce some sort of terror in you but I have to admit Higurashi nails it. One of my favorite tracks is Demonic Institute and you just know shit is about to happen when it starts playing. Having read Umineko before I have to admit the OST is a bit basic in comparison but I really love it nonetheless. I'll try to sum up each episode regarding the mistery.</p><h2>Onikakushi</h2><p>A really good introduction and at first glance probably the chapter with minor ties to the main plot. It felt a lot like Umineko where you ge introduced into Hinamizawa and the residents. Looking back after finishing the arc though, it's the only chapter that mentions the Director and the Drug. I'm somewhat confident that he is behind the curse every year. Honestly speaking I was absolutely convinced Rika was behind everything. If you consider Knox's 1st (Gotta thank Umineko for that) it has to be one of the characters you see in chapter 1 and Rika felt like the only one who would fit the bill. After finishing chapter 4 though I have to disregard that theory, more to that later. Regarding their deaths I'm not really sure. Without going into spoilers either it's something like Umineko regarding the first four episodes or, a rather dumb theory of mine, parallel words.</p><p>Watanagashi</p><p>Mion's chapter and my personal favorite since I'm a huge Mion fan. I really loved the small romance between them, or at least from Mion sind Keiichi didn't really do much. Seeing Mion's more feminine side and her regret not being able to show it to the one she likes was heartbreaking. We also get to know about Shion. I have to say that last phonecall was the most chill inducing moment I felt and it's my favorite scene in the question arc. This is probably the chapter you should re-read the most especially with them swapping places all the time. As it was said in the teaparty I don't think the Sonozaki family is behind the curse each year. I have a big theory about the end though. I don't think it was Mion doing all the killing, it was actually Shion. I don't really have much evidence, especially without re-reading the chapter. One thing that strikes me odd is that she kills Oryou considering how close they seem in chapter 4. At first you think she has to do it in order to fully take over as clan head but as we learn in chapter 4 she already is the defacto leader so I don't really see the reason to kill her off. Also that she kills Satoko for no apparent reason. You already had your victims for the curse this year, so why go out of your way to also lure Satoko and kill her? I'm still contemplating if I should reread or continue to the answer arc.</p><h2>Tatarigoroshi</h2><p>And the mindfuckery starts. I think objectively this was the best chapter but subjectively it was the worst for me. I really appreciated that instead of going through 6 hours slice of life again, it gave you a lot of good character moments early on. Sadly I don't like Satoko so I didn't care much about her. It's really hard to say what was actually going on. This chapter was the reason I started considering parallel words. I'm very hesitant to even consider it since it means paranormal things exist but it would explain a lot. He actually kills Satoko's Uncle but somehow shifts worlds and ends up in a world where he went to the festival instead. It seems weird that things that happened in chapter 1 and 2 are mentioned here as well. The club game at the festival with Tomitake from chapter 1 and Shion's request at spending time with him from 2. In hindsight this chapter together with Himatsubushi is the reason I'm suspicious about Takano being behind the curses. Honestly speaking she is the only character left, who fits the bill. As a nurse she has the knowledge and means to create the drug. It is highly implied she killed Tomitake, which means she probably killed him in the previous chapters as well. She has a lot of knowledge about Hinamizawa Folklore, the curse in particular. Her death is the only one that you can easily fake by putting a false corpse and burning it. In chapter 1 she disappeared but that could be intentional. What speaks against it is, why show yourself and barge into the storeroom after faking your own death? I'm not really that convinced but like I said from all the available characters she is kind of the only one left. As a sidenote I'm pretty sure Satoshi killed his aunt. How exactly they ended up blaming someone else is another mistery though. Maybe they fed him drugs and made him confess something he didn't do. Ooishi's scene was extremely weird as well. I don't think they just followed Keiichi since he asked if this was really the right spot. So how exactly did they know where to look? How long where they standing there waiting for him? Why did they behave like that and just vanishing without a word after not finding anything? I'm not even starting with Keiichi being able to curse people. It feels a bit too much to be mere coincidence. Also what is the thing with the footsteps.</p><h2>Himatsubushi</h2><p>The chapter I felt like I wouldn't care but I ended up really liking it. Akasaka is an amazing character and I have a feeling he will somehow show up in the answer arc. This is also the chapter where Ooishi starts to shine. I'm still unsure how to see him. In chapter 1 he felt a little bit like a dick, using Keiichi as means to learn more about the curse. After that he got progressively worse with chapter 3 him being outright antagonistic. This time he was actually really cool and I'm starting to think he really just wants to solve the murder. We also got more infos about Rika. Regarding her I'm honestly at a blank. I have no idea how she was able to predict everything from the very beginning but this made me reconsider her being the mastermind behind everything. It feels more like she is also fighting against the curse in her own way. One thing I can say, the way she was speaking and holding herself in the CG she definitely didn't give the impression of a kid. She felt more like an adult. This again would be explainable with Parallel Worlds. If she somehow is able to switch between them after she dies it would make sense for her to have all the knowledge. Actually as I'm typing this out this sounds more like a time loop. Damn that makes much more sense than Parallel Worlds. If she is stuck in a time loop it would explain every episode. It's just one iteration she experiences. After she dies she basically resets to Episode 4 when the dam war was happening. This would explain her knowing everything that's about to happen. It would explain why she gives the impression of an adult, because at least in her mind she already is one. It doesn't explain everything but it feels like a solid foundation. I guess I have to rethink everything with that in mind.</p><p>All in all I feel a lot more confident about things compared to Umineko. It actually feels like you have a grasp on things, even though I'm probably spouting bullshit and have no idea about anything. I can't wait to dive into the answer arc and hopefully get some answers.</p><p>One special mention regarding the teaparty. Small spoiler for Umineko's first teaparty.</p><p>I absolutely loved Umineko's teaparties so I was quite miffed to see in Higurashi it's just the actors talking about the episode. In hindsight though that makes me appreciate Umineko even more. I can only imagine playing through Higurashi and enjoying the after parties with the cast. Then you start reading Umineko, finish the first chapter and look forward to another round of characters talking, which is exactly what happens. Until the twist comes with Beatrice melting everyone and Prison Strip starts playing, Battler screaming, telling you as a player exactly one thing:</p><p>This won't be a happy tea party and this definitely won't be like Higurashi at all.</p><p>This makes me a little bit sad I read Umineko first but it really left an impression on me.</p><p>If you made it all the way through, thanks for reading. As it was with Umineko there are a million more things I want to talk about but it would totally go way beyond a reddit thread so I'm stopping here.</p>
 """
        )
    db.session.add(thread4)
    thread5=Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        subject='Kakera Theory [Higurashi and Umineko Spoilers]',
        text="""<p>I think it’s pretty apparent that even besides Rika and Hanyuu, the characters in Higurashi are supposed to be the “same people” from world to world (although they don’t remember previous worlds). But I’m having a hard time figuring out exactly how that works.</p><p>The simplest way would be if Rika and Hanyuu were just “rewriting” the same world with a different possibility each time, but we know that each world continues even after Rika and Hanyuu leave it, so that can’t be the case. So then we might be tempted to think that the worlds really are completely separate, but that would disregard all the evidence that the characters are the same people from world to world.</p><p>So…here’s the best I can come up with at the moment:</p><p>When Rika and Hanyuu left their original world, they took the souls of the original world with them (or maybe just the souls of the people of Hinamizawa? It’s hard to say). Each time they go to a new world, those “traveling” souls merge with the “stationary” souls already in that world. Then when Rika dies, or shortly thereafter, the traveling souls part with the stationary souls and move onto the next world. And so on.</p><p>Thoughts?</p>
        """)
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