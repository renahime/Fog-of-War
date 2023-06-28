from app.models import db, Category, environment, SCHEMA, Thread, Post, User, SubCategory
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_boys_threads():
    user = User.query.get(1)
    category = Category.query.filter_by(name='Anime Manga and VNs').first()
    subcategory=SubCategory.query.filter_by(name='20th Century Boys').first()
    thread1= Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        subject="[20th Century Boys] - Friend's Identity Theory",
        text="""<h2 style="margin-left:0px;">Introduction</h2><p>The open ending of the series leaves up a lot of room for interpretations and theories regarding the identity of Friend. The most common interpretation is the first Friend being killed by Yamane and Katsumata replacing Fukubei as the second Friend. Others believe that Katsumata was always Friend because Fukubei died in 1971.</p><p>But what if I tell you that <strong>Katsumata</strong> <i><strong>is</strong></i> <strong>Fukubei</strong>? I came to that conclusion after a lot of comtemplating and I'll explain the reasons why Katsumata and Fukubei could be the same person.</p><h2 style="margin-left:0px;">#1 Fukubei / Hattori is not his real name</h2><p>In <a href="https://imgur.com/a/k0Hpc9A">Chapter 26</a> when Fukubei introduced himself to Kenji, Kenji tried to guess his name and says: <i>"Fukubei?!"</i>. Fukubei replied: <i>"Don't call me that. I'm too old for that Nickname."</i></p><p>In <a href="https://imgur.com/a/e3GBrmw">Chapter 135</a>, Yoshitsune remembers that Fukubei was always telling them to call him by his real name: <i>"I'm not Fukubei. I'm Hattori."</i></p><p><i>But doesn't this prove that Fukubei/Hattori is a different person than Katsumata?</i> No because no evidence suggests that Hattori is Fukubei's real name. The only source we have is Fukubei himself and we all know that Fukubei is a pathological liar. It's also extremely unlikely that his real name is Hattori because Fukubei would've been exposed quicker when his real name is Hattori while hiding behind a Hattori mask as Friend. Another fundamental factor that makes Hattori being Fukubei's real name even more unlikely, is Fukubei's struggle with identity but that's a topic I'll adress later.</p><h2 style="margin-left:0px;">#2 Yamane didn't kill Fukubei in the science room in 2015</h2><p>In <a href="https://imgur.com/a/CVSFUXl">Chapter 119</a>, according to Kiriko, modern history will end in 2015 if Friend isn't stopped.</p><p>In <a href="https://imgur.com/a/QM5TC65">Chapter 125</a>, Yamane tells Otcho that he and Friend use a book for secret correspondence. A book that always stays in the library and will never be borrowed.</p><p>In <a href="https://imgur.com/a/eBOV3Re">Chapter 126</a>, Otcho finds a note that fell out of the book which Yamane was referring to that says: <i>"Meeting of the secret society. Time: The night of January 1st 2015, the last year of modern history. Place: The science room."</i></p><p>In <a href="https://imgur.com/a/QuC8UyT">Chapter 128</a>, Yamane says that Friend will come to the science room to kill him and wants to keep it a secret.</p><p>In <a href="https://imgur.com/a/oUXpPuG">Chapter 138</a> when Kiriko asks Yamane about the New Book Of Prophecy, she says: <i>"When the 'world president' is created..."</i></p><p>In <a href="https://imgur.com/a/qlY92iV">Chapter 146</a>, Takasugi says that the death of Friend was never written in the New Book Of Prophecy.</p><p>In <a href="https://imgur.com/a/3XEHbXO">Chapter 176</a>, Fukubei cites the New Book Of Prophecy: <i>"He will die and come back to life."</i> and says: <i>"The last day of our next summer vacation, a miracle will happen."</i></p><p>In <a href="https://imgur.com/a/diRi87c">Chapter 221</a> when the second Friend wants to take off his mask, Kanna tells him: <i>"They performed plastic surgery. No doubt you look exactly like him."</i></p><p>In <a href="https://imgur.com/a/OjUpKWv">Chapter 232</a>, In the New Book Of Prophecy, it says <i>"...and then the world president was born."</i></p><p><i>But what does this have to do with Fukubei's death?</i> Don't you think it's weird how an extremely intelligent guy like Fukubei puts himself in such an obvious dangerous situation? He doesn't wear a bulletproof vest, he doesn't have any bodyguards nearby, he wants to kill Yamane personally instead of banishing him through his connections, he wants to keep this meeting a secret, etc. Then we have the New Book Of Prophecy and the secret note saying: "<i>The world president will be born." "Modern history will end in 2015."</i></p><p>As a child, Fukubei cites the New Book Of Prophecy: <i>"He'll die and come back to life to life."</i> What does this quote refer to? To the 1971 science room incident? Or to the birth of the world president and the end of modern history? But didn't Takasugi mention that Friend's death was never mentioned in the New Book Of Prophecy? What are the possible reasons for this seemingly contradiction?</p><p>First Friend's backstory was never shown in an objective narrative way. It was shown through the reading system the second Friend was using. It's all data that was saved from Friend's memory and Friend's memory is not fully correct as <a href="https://imgur.com/a/VRiUN8K">in the virtual attraction, the mansion of the hanging hill incident took place in 1971 instead of 1970</a>. So maybe he never wrote <i>"He'll die and come back to life"</i> in the New Book Of Prophecy.</p><p>Friend deleted that section from the New Book Of Prophecy so he can convince the whole world that he died and came back to life.</p><p>Friend's henchmen never read the whole New Book Of Prophecy.</p><p>Friend's death was planned from the start. Friend needed to die in order to come back to life. That was the only way to become a world president and end the modern history. Fukubei knew that and that's why he sent one of his doppelgangers there that were created through either plastic surgery or human cloning.</p><h2 style="margin-left:0px;">#3 Similiarites between Fukubei and Katsumata</h2><p>In <a href="https://imgur.com/a/ErRWMpr">Chapter 28</a>, we see Kenji picking up an album of T. Rex that belongs to Fukubei. Kenji says: "<i>This takes me back. '20th Century Boy'."</i></p><p>In <a href="https://imgur.com/a/7VmBgR0">Chapter 16</a> of <strong>21st Century Boys</strong>, Katsumata wants to commit suicide but changes his mind after hearing the song "20th Century Boy" by T.Rex.</p><p>In <a href="https://imgur.com/a/1K5GFp0">Chapter 75-76</a>, Kenji and Maruo listen to the tape that Fukubei left there, playing "20th Century Boy"</p><p>In <a href="https://imgur.com/a/AKVkT1s">Chapter 222</a>, second Friend calls himself a "20th Century Boy."</p><p>In <a href="https://imgur.com/a/RgJhkNx">Chapter 129</a>, first Friend is holding baby Kanna.</p><p>In <a href="https://imgur.com/a/FZxV6EW">Chapter 221</a>, second Friend tells Kanna how he held her up when she was a baby.</p><p>In <a href="https://imgur.com/a/vXA1LhK">Chapter 173</a>, Fukubei sees himself faceless in the mirror multiple times.</p><p>In <a href="https://imgur.com/a/it5EAIS">Chapter 173</a>, Fukubei sits in front of a mirror and questions his identity: <i>"Who are you?" "Are you Sadakiyo?" "Are you Katsumata-kun?"</i></p><p>In <a href="https://imgur.com/a/ILy7VxK">Chapter 9</a> of <strong>21st Century Boys</strong>, Katsumata is faceless in the virtual attraction.</p><p>In <a href="https://imgur.com/a/f7x1NN0">Chapter 2</a> of <strong>21st Century Boys</strong>, Yamane wants to know what Friend is planning. Fukubei replies: <i>"It's not something I can tell just people. Even if I told you guys, you might not understand me."</i> Yamane keeps asking Friend what he is thinking and Fukubei responds: <i>"Hehe, should I tell you, hehe."</i> Shortly after that when Fukubei and Yamane went away, Katsumata says: <i>"Then a flying saucer flew in, and faced off against the giant robot. Boom! And with that the peace of mankind was ensured."</i> After Katsumata said this, he repeated Fukubei's words, implying that this was what Friend was planning.</p><p>Fukubei listens to T. Rex. Katsumata changed his mind about committing suicide when he hears the song "20th Century Boy" by T. Rex. Though this is not proof that Katsumata is Fukubei, it's still a hint that Urasawa intentionally gave us.</p><p>Shortly before the identity of the first Friend was revealed, Kanna remembered how her father held her up as a baby. Years later when Kanna met second Friend, Friend acted like he's the real father and also mentioned how he held her up as a baby. Many people believe that second Friend tried to become Fukubei through the reading system when Fukubei's backstory was shown. But what if second Friend <strong>is</strong> Fukubei? How did second Friend know how he held Kanna up as a baby? Why did he still act like he's the real father even though he knew Kanna's opinion?</p><h2 style="margin-left:0px;">Conclusion: Fukubei never existed and was nothing but a persona invented by Katsumata</h2><p>Fukubei, Hattori, Friend. All names made up by Katsumata in an attempt to fill his lack of identity.</p><p>The death of Friend, the resurrection of Friend, the end of modern history. In order to pull this off, Friend needed to convince even his closest henchmen. That's why they believed that Friend was unable to predict his death. He sacrificied one of this doppelgangers that were most likely human clones created by Yamane, to convince the whole world that Friend has died. That was the only way for Friend to become a god and end modern history.</p><p>Katsumata struggles with identity. Katsumata wants attention and power. Katsumata is timid. That's why he created Fukubei and Friend. That's why he acted so cocky towards Sadakiyo. That's why he was obsessed about the Expo. It wasn't Katsumata who bullied Sadakiyo. It wasn't Katsumata who was concerned about the Expo. It was his alter Ego Fukubei. Fukubei is what Katsumata always wanted to be, similiar to the protagonist of Fight Club and Tyler Durden. That's why Friend said that Fukubei is a part of him and that Fukubei's concerns aren't his. Because his invented persona Fukubei cared about the Expo, not Katsumata.</p><p>Katsumata died and haunts the science room as a ghost. When Donkey went to the science room, what did he saw? That's right. Fukubei being dead and coming back to life. Fukubei is Katsumata.</p>
""")
    db.session.add(thread1)

    thread2=Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        subject='Question about 20th Century Boys.',
        text="""<p>Going into this I knew that it would be good, from all the high ratings it gets. But to be honest I didn't expect it to be <i>that</i> good, and it was. I couldn't recommend this enough to anyone. This was the first thing I read by Urasawa and I'm more than impressed. He's a great character writer, and a genius at writing complex, huge-scale stories. Also had some amazing artwork too. 10/10</p><p>But I'm not doing a review on anything, I just wanted some things clearing up...</p><p>Like who even is Katsumata?</p><p>The whole volume dedicated to Fukubei and Sadakiyo's past was great, and I loved it, but nothing was mentioned about a 4th kid as far as I can remember. It just came out of no where. Even then, the scene where Kenji unintentionally saves his life as a kid was a sweet moment, one of many. In fact it's hard to pick a favourite moment because of how much actually happened.</p><p>In fact the only problems I have with the story was friends identity not being explained well, and the bomb under the base- because it was a sort of ending <i>after</i> the ending (although everything else in 21stCB like Kenji going into the simulation was great, and everything got rounded off nicely). I'm nitpicking at this point though.</p><p>But seriously if someone can clear up who exactly the final imitation of friend was, that'd help.</p>
""")
    db.session.add(thread2)

    thread3=Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        subject='21st Century Boys Perfect Edition has a different ending?!',
        text="""21st Century Boys Perfect Edition has a different ending?!

So I got the Perfect Edition of 20th Century Boys to re-read the series for the 3rd time but... I got to the ending of 21st Century Boys (the epilogue for the main series) and IT HAS A DIFFERENT ENDING?!

Can anyone explain how this ending fits the story? I don't think it makes sense. In this ending, it is stated that Fukubei died when he was a child (I suppose during his "science room resurrection"?) and then Katsumata replaced him at that time and became "Friend". How does this make any sense? If this was true, then the "1st Friend" would be Katsumata, since Fukubei is dead. But then... who is the "2nd Friend"?! In theory, the "1st Friend" was shot to death by Yamane in 2015. So, according to this new ending, it is Katsumata who dies there. So who the **** is the "2nd Friend"?! Then only explanation is that Katsumata survived Yamane's shot but... I don't know.

Does anybody has any good explanation for this?"""
              )
    db.session.add(thread3)
    thread4=Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        subject="The ups and downs of 20th century boys",
        text="""<p><strong>The ups and downs of 20th century boys</strong></p><p>Spoilers for the entirety of the series.</p><p>I was enraptured reading Naoki Urasawa's 20th century boys. It was my second manga by hm after the also fantastic 'Pluto'- but Pluto's terrible ending left me with a sour taste in my mouth, but also a taste for more. So i decided on 20th century boys, over the likes of 'Monster' and 'Billy Bat' to be my second series by him.</p><p>For a while, it was genuinely one of the best manga i have ever read. The paneling is simply unmatched- Urasawa is the greatest manga panelist of all time in sheer panel composition. Everything leads into the next panel, page, anything, so perfectly. Reading his manga is so brisk, exciting, suspenseful. He could make a man taking a excruciatingly agonizing shit entertaining. His characters as always are deep and interesting- Kenji (at one point...) was my favorite MC ever behind Guts. The story of the main character basically being an overgrown child and being hellbent on turning the playful dreams of a kid in summer creating a shonen-style world destroying event they can beat together into reality is a very unique and interesting idea (also, an idea i had once for a short story... So funny to see it here, also lol). 'Friend' was a mysterious yet compelling villain and i was completely hooked in the present storyline, the past storyline, and how they connected to eachother. I wanted to know who Friend was- <i>why</i> friend was, <i>how</i> friend was. The first arc and a half is phenomenal mature shonen (i hesistate to call it seinen but i guess it is, kind of a borderline between them), but then it just goes on....and on....and on....and on.... There are <i>2</i>(!) time skips in this series, and the series effectively stops and re-starts like a half-broken jalopy both times. The first arc is a nearly perfect self-contained story, the second is a worthy continuation for most of it, other then Kanna being a terrible unlikable protag with magical ESP powers that are literally never explained, a Spunky Girl With Magic Powers Who Is A Bit Grumpy But Not Too Grumpy, Always Does The Right Thing, And Always Wins No Matter What. Sound familiar? Within 50 chapters shes gambled and won the entire casinos money, got an entire army of gangsters to unite behind her, and united the two mafia lords who hate eachothers guts into a peace the city has never seen. Yeesh. I began to get bored at when this story about a man fighting his former school rival with his old friends turned into the man's neice combining powers with the mafia to protect the pope (...what?) and it just goes downhill from there. The third story arc turns the story into a post apocalyptic dystopian nightmare. But Friend is fucking dead at this point, and the main characters have failed twice. Imagine if Luffy walked up to Arlong, got his ass beat, walked up to him again, and got his ass beat even worse. I wouldnt care about the third fight at that point, im bored. The series somehow pulls off being 50-60 chapters too long, while feeling extremely rushed, which is borderline impressive on how he pulled that off. The ending (i will not bother to read 21st century boys- i barely pushed through 20th, and if he needs an auxillary series to amend his failure of an ending that is the fault of the author and not the reader) felt anticlimactic with no real release felt. Kenji comes back from the dead (?!?!?!) as does Sadakiyo(!?!?!?!?) because i guess Urasawa got bored with Kanna. Except this time Kenji is a bored brainless bum who just walks around and does almost nothing but play guitar. The series ends with them literally re-making Woodstock, abandoning every character arc other then Kanna's and Kenji's. God, or Kami, ended up being a walking plot device, the cop was nearly completely useless and forgotten about, the transsexual was forgotten about, the teenage brats storyline was either dropped or was so unmemorable i forgot about it, the manga writer trio except for Barton Fink was almost completely useless and even then Barton barely did anything after he escaped jail, 'Friend's Daughter/Clone' storyline was compeltely dropped, he expects us to beleive that Katsumata was there the whole time but was so unmemorable that he was literally completely wiped from everyones memories completely, we never learned how this unlikable smug middle school freak became the worlds biggest cult leader besides 'Charisma' (that he didnt have). He literally seduced a woman and i guess had such a bomb dick he convinced her TO MAKE A WORLD DESTROYING VIRUS FOR HIM.</p><p>Seeing this story crumble from tightly written masterwork to overextended mess that the author has literally no idea how to end right in front of my eyes chapter by chapter was tragic. It genuinely felt like he was winging it chapter by chapter. The story somehow feels like it was wrung of any and all moisture until it was drier then Arizona in the summer, and also somehow incomplete and unsatisfying. Naoki has an issue where he just keeps on introducing new ideas and abandoning old ones- overextending his series until he writes himself into a corner that he cant get out of, ending the series usually on a limp or unsatisfying note (apparantly this continues with Monster which i havent read). I feel so, so, so dissapointed. Maybe these are answered in 21st century boys but i cant be bothered</p>
"""
        )
    db.session.add(thread4)
    thread5=Thread(
        user=user,
        categories=[category],
        subcategories=[subcategory],
        views=0,
        subject='[20th Century Boys] - Friends Fate',
        text="""<p><strong>[20th Century Boys] - Friend's Fate</strong></p><p>TL;DR: <i><strong>Friend's fate is unknown and he may be alive</strong></i></p><h2 style="margin-left:0px;">Introduction</h2><p>It's unclear what has happened to Friend in certain instances. What happened to Fukubei after he slipped during the hanging trick in 1971? What happened to Fukubei after he fell from the rooftop during the bloody new years eve? Was Fukubei really killed by Yamane?</p><p>This thread doesn't necessarily answer these questions but rather offers possibilities about what may have happened.</p><h2 style="margin-left:0px;">The Lie of 1971</h2><p>Did Fukubei die after he slipped during the hanging trick in 1971? He most likely didn't die because we have seen<a href="https://imgur.com/a/XGtHZo8"> Fukubei with Manjoume during a flashback that took place in 1972</a>. It certainly can't be Katsumata during the flashback as not only does he have the same appearance as Fukubei, he also has the same demeanor as Fukubei. It's thought that Fukubei died and Katsumata copied Fukubei's appearance and demeanor but he can't possibly do that within 1 year, especially at that age. They didn't even have the means to perform plastic surgery on Katsumata to look exactly like Fukubei during this period of time. <a href="https://imgur.com/a/he3zqQb">In a different flashback that took place in 1980, Fukubei visited Manjoume and introduced himself as Hattori</a>. If this was Katsumata, how could he look like a hypothetical adult Fukubei so accurately? If Katsumata looks completely different from Fukubei, there is no way he could look like this. <a href="https://imgur.com/a/wtw7m8r">Shortly before Friend was shot by Yamane in the science room, Yamane told him that he didn't die but actually has failed in his lie</a>. Based on these facts, we can conclude that Fukubei survived after he slipped during the hanging trick in 1971.</p><p>The reason why it's believed that Fukubei died after he slipped during the hanging trick in 1971 or off-screen after the elementary school graduation in 1972, is because Kenji said that Fukubei died. This is wrong because Kenji lacks knowledge and wasn't being literal. Based on what does Kenji know about what happened to Fukubei? Not even the rest of the Kenji Faction knows what happened to Fukubei after he slipped during the hanging trick or after he graduated from elementary school and there is nothing that suggests that Kenji has found out these things at this point. For those who believe that Fukubei died off-screen, do you really believe that Naoki Urasawa would randomly kill a character <i>this important</i> without any explanation? I certainly don't.</p><p>Fukubei died in a symbolic sense and not in a literal sense. When Fukubei gave Katsumata the death penalty, Katsumata didn't die but was forgotten and believed to be dead similiar to Sadakiyo. Both were forgotten and died in a symbolic way. <a href="https://imgur.com/a/lThrt0i">Sadakiyo wasn't noticed by his old classmates and considered himself dead and not-existent</a>. Neither he nor Katsumata died. Fukubei did. <a href="https://imgur.com/a/GS7g70N">Yoshitsune and Keroyon had no trouble remembering Katsumata</a> and <a href="https://imgur.com/a/7wRhD03">Sadakiyo was remembered by Sekiguchi-Sensei</a> and Kenji but what about Fukubei? Kenji only could guess his name and <a href="https://imgur.com/a/bBwuNBE">Yoshitsune's first memory of Fukubei was the 1997 reunion</a>. Unlike Fukubei, Katsumata wasn't actually forgotten and that's why it was Fukubei who died and not Katsumata.</p><h2 style="margin-left:0px;">Bloody New Years Eve</h2><p>What happened to Fukubei after he fell from the rooftop during the bloody new years eve? Either wires were attached to Fukubei that allow him to get inside the building when he fell just like <a href="https://imgur.com/a/28IqWAo">Friend was attached by wires that allow him to float</a> or it was a doppelganger of Fukubei who sacrificed himself in order to make the Kenji Faction believe that he has died. <a href="https://imgur.com/a/ajiKxVp">Kanna asked Friend how many people like him are pulling the strings behind the scenes and tells him that they performed plastic surgery on him to look like Fukubei</a> so it's possible that Friend has doppelgangers.</p><p>It's reasonable to believe that Fukubei wouldn't risk his life by going out there all by himself. During the showdown between Kenji and Friend, who knows if that was actually Fukubei and not just a doppelganger? Why would Fukubei risk his life and plans laid out by the New Book of Prophecy if he could just send a doppelganger there? Friend isn't supposed to die at this point. His death is supposed to happen in 2015. He most likely sent a doppelganger there in order to make everyone believe that he saved the world.</p><h2 style="margin-left:0px;">The 2015 Secret Society Meeting in the Science Room</h2><p>In elementary school, <a href="https://imgur.com/a/QM5TC65">Yamane told Otcho about a book used for secret correspondance that always stays in the library and never borrowed by anyone</a>. When Otcho found and opened the book in 2015, a note fell out saying: <a href="https://imgur.com/6ZWtMaN">"Meeting of the Secret Society. Time: The night of January 1st, 2015, the last year of modern history. Place: The science room."</a> In a video that was recorded in 2002, <a href="https://imgur.com/a/CVSFUXl">Kiriko says that modern history will end in 2015 if Friend won't be stopped</a>. The birth of the world president was written in the <a href="https://imgur.com/a/OjUpKWv">New Book of Prophecy</a> and mentioned by <a href="https://imgur.com/zN6kIcb">Kiriko</a> and <a href="https://imgur.com/TpDwyrp">Manjoume</a>.</p><p>From the beginning of 20th Century Boys, all events that were mentioned in the Book of Prophecy and New Book of Prophecy actually happened and were orchestrated by Friend. He planned all of this including the end of modern history and birth of the world-president. The only thing that hasn't been mentioned is the means by which this goal will be achieved. In order to end modern history and become the world-president, the only way pull this off was dying and coming back to life. In 1970, <a href="https://imgur.com/a/3XEHbXO">Fukubei cites the New Book of Prophecy: "He will die and come back to life."</a> which means that Fukubei had the idea of Friend being able to die and coming back to life since 1970. It's unclear if this statement refers to the lie of 1971 or the 2015 Expo but since the New Book of Prophecy was always about the future, it's more likely about the 2015 Expo. This statement however was most likely deleted by Friend from the New Book of Prophecy in order to fool the whole world including his own staff or his own staff never read the whole New Book of Prophecy.</p><p>Knowing all this, why would Fukubei go into the science room alone with no security and bulletproof vest to kill Yamane who betrayed him and whom he could have banished through his connections? Why would Fukubei go into the science room knowing about the secret society meeting note and the New Book of Prophecy? The answer is, he didn't go there. He sacrificed one of his doppelgangers in order to fool the whole world that Friend has died. That was the only way to become the world-president and end modern history. All of this was planned and has happened. He became the world-president and the AD calendar ended and was replaced by the new calendar; "Friend Era". It's extremely unlikely that it was the actual Friend who was shot and killed by Yamane</p><h2 style="margin-left:0px;">The Superpowers of Katsumata</h2><p>This section isn't necessarily related to Friend's fate but serves as a response to those who believe that Katsumata had superpowers which is related to the many deaths of Friend.</p><p>It is believed that unlike Fukubei, Katsumata actually had superpowers such as ESP, precognition and more. I've read theories saying that Katsumata doesn't have just ESP but also has other superpowers such as being able to survive the fall from the rooftop during the bloody new years eve or resurrecting from the dead. If you truly believe that Katsumata used his superpowers to revive himself after being shot by Yamane, then you must believe that he didn't actually die in 3F as well because he could've used his superpowers to revive himself just like he did in 2015.</p><p>The only superpowers Katsumata might have are ESP and precognition. When Fukubei slipped during the hanging trick in 1971, we could see all the future events such as <a href="https://imgur.com/a/SLcNbKz">Friend himself, the deaths of Donkey and Yamane, the bloody new years eve, baby Kanna, etc.</a> It's unclear if Katsumata saw this when he was using the reading system or Fukubei in 1971. I'd like to point out that I believe that Fukubei and Katsumata are actually the same person. I've made a <a href="https://www.reddit.com/r/manga/comments/zwk7np/20th_century_boys_friends_identity_theory/">thread</a> where I theorize about this very thing.</p><p>Friend having superpowers would defeat the whole purpose of the series, which is about him being a fraud who uses tricks in order to make everyone believe he has superpowers. Friend couldn't actually predict the future as the events were all orchestrated to happen by him. Friend's followers believed that he could predict the future because they lacked the knowledge that it was Friend who caused all the predicted events. Superpowers that enable him to survive the fall from the rooftop and resurrect from the death are vastly superior superpowers than being able to float and bend spoons. Friend couldn't even float or bend spoons so why should he use his inferior tricks to deceive everyone if he could just use his superior superpowers to achieve a greater impact?</p><p>Friend is so great at deceiving people that not only did he deceive everyone in 20th Century Boys but he also deceived us readers.</p>
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
