label daughterParentsMeetDragon:
    if(daughter_stone_option==12):
        hide adelaide with moveoutleft
        hide knight blue with moveoutright
        show black with dissolve
        jump daughterParentsStay_adeDragonSacrifice

    else:#daughter_stone_option==13
        scene background b
        ade "Thoughts: What should I do?"
        menu:
            "I guess I have no choice, I have to try to negociate my parents release from the dragon, \
            they are family after all!":
                $ daughterParentsMeetDragon_firstChoice = 22
            "I am not mad enough to go anywhere near a dragon! \
            Too bad for my parents but they were sexist control freak anyway. Adventure here I come!":
                $ daughterParentsMeetDragon_firstChoice = 23
        hide adelaide with moveoutleft
        hide knightB with moveoutright
        show black with dissolve
        if (daughterParentsMeetDragon_firstChoice == 22):
            jump daughterParentsMeetDragon_option22
        else:#daughterParentsMeetDragon_firstChoice == 23
            jump daughterParentsMeetDragon_option23


label daughterParentsMeetDragon_option22:
    scene background ragonCave
    show adelaide scared at left
    ade "Dragon! Hey! Dragon!"
    dragon "Roarrr!"
    dragon "Boom!"
    show dragon at right with moveinright
    dragon "Boom!"
    dragon "Boom!"
    dragon "Ssssss. A Little a human. \
    Not enough to satiate my hunger after sleeping so long but it will have to do…"
    ade "Wait! I have come to negotiate the release of our King and Queen that you have taken prisoner!"
    dragon "Why should I want to give them away? They are excellent bait to lure food to me…"
    ade "..."
    ade "Umm, we have treasure! We can give you lots of gold in exchange!"
    dragon "Really? How much?"
    ade "…10,000 gold pieces?"
    "Unfortunately, the war that had been ongoing for years had depleted \
    the coffers of the kingdom and Adelaide was not in a position to offer more to the dragon."
    "Face with such an insulting offer, the dragon did not give her the time to flee and swallowed her whole."
    jump end


label daughterParentsMeetDragon_option23:
    scene background a
    show adelaide with dissolve
    ade "I do not like this path… Damned dragon! \
    Why did he have to block the North road out of the country? \
    There is not even a proper state down South!"
    ade "I should be close to the border by now…"
    show knight purple at right with moveinright
    knightP "Stop! Who goes there!"
    show adelaide surprised at left with moveinleft
    ade "!"
    ade "Umm… I am Adélaïde of Arcance! I have come to ask for asylum to your Lord! Lead me in front of him!"

    hide adelaide with dissolve
    hide knight purple with dissolve
    show black with dissolve
    scene background darkLordLair
    show darkLord at right with dissolve
    show adelaide scared at left with dissolve

    mLord "Well… what do we have here?"
    ade "… \nThoughts: I do not like this. He looks very intimidating."
    mLord "What has bring you to our humble city, your Highness?"
    show adelaide at left
    ade "I am seeking refuge from my people."
    mLord "Oh?"
    ade "They want me to 'negotiate' with a dragon. \
    But I have heard them talk about royal sacrifice appeasing the beasts and \
    I was not mad enough to stay there!"
    mLord "How sensible of you…"
    show adelaide scared at left
    ade "What is that?! Black magic!"
    mLord "Stupid little girl… You have come to the castle of a Dark Lord all innocent and ignorant."

    if(daughterWitch_option == 73):
        show adelaide at left
        ade "No, I have heard about you! In fact, I am quite delighted to have meet you!"
        ade "I beg you to take me as your apprentice! \
        I wish to learn magic to have the power to make choice of my own!"
        dLord "… you realise that you will have to submit to me and ober my every orders?"
        ade "You appear to be intelligent! I have no doubt that you would be willing to listen to what \
        I have to say and not dismiss my opinion just because I am a woman!"
        dLord "… very well."
        "Despite her initial suspicion, Adelaide was delighted to have the opportunity \
        to learn magic from the Dark Lord himself in the following years."
        "With such an exigent mentor, she was quick to make progress and gain a top spot in his army. \
        As expected, once she had proven herself, he treated her with at least as much respect as his men."
        scene background a
        "Together they made a short work of conquering Arcance, N eterny and Arcla. \
        From now on, the rest of the continent awaited them. \
        And Adelaide was quite seeing herself as the Consort of the future Emperor."

    elif(daughterWitch_option == 71 or daughterWitch_option == 72):
        dLord "Are you afraid of my power?"
        ade "No, no! In fact I quite like dark magic!"
        dLord "… very well."
        ade "Thoughts: I do not like that smile… What is he going to do…"
        "When the Dark Lord ended up using his dark magic to enslave her, \
        Adelaide was not surprised. She had no choice but to resign herself \
        to a life of humiliation and privation."

    elif(daughterWitch_option == 8):
        dLord "!"
        dLord "What is this?"
        ade "…an old witch gave me this stone."
        dLord "Helen… Always putting her nose where it does not belong…"
        dLord "Very well. You shall stay here."
        "Despite Adelaide's initial suspicion, \
        the Dark Lord proved true to his word and she was offered asylum as she had asked. \
        The Dark Lord himself kept her at arm length."
        "With time, she was able to glean a bit of magic from here and there \
        but she was no match for the Lord and his Court \
        and had to resign herself to look from the outside."

    else:#daughterWitch_option == 6
        dLord "!"
        dLord "What is this? You have been cursed!"
        ade "…an old witch gave this to me."
        dLord "Helen... I recognise her style…"
        dLord "Far be it from me to go against her decisions…"
        "After a flash of light, Adelaide felt as if her innards were ablaze. \
        She felt to the ground, her whole body twisting uncontrollably from the pain."
        "This seemed to last forever before she felt herself slip away, \
        the Dark Lord’s cruel laugh in her ears."

    jump end
