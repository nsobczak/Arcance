label daughterParentsDeadAdvice:
    scene background b
    show adelaide angry at left
    show knight blue at right
    ade "Why do they refuse to listen to me? I told them what would happen! I told them!"
    knightB "I am sorry your Highness, but you obviously do not understand the situation"
    knightB "You do not know the Neterny like we do."
    ade "Well you know them so well that you lost us the war!"
    knightB "Your Highness!"
    ade "What do they want now…"
    show adelaide at left
    ade "What is it?"
    knightB "We got news from His grace, the Duke Laurence."
    ade "..."
    ade "Well? What are you waiting for?"
    knightB "His Grace has been able to sign a peace treaty with Neterny…"
    ade "That sounds like very good news."
    knightB "Unfortunately, the King condition was your hand in marriage…"
    ade "...\nThoughts: I should have seen that coming."

    hide knight blue with moveoutright
    scene black
    show adelaide scared at left
    ade "What should I do? I have know all my life that marrying a complete stranger would be my fate, \
    but this does not make the situation more palatable… "
    menu:
        "I guess I have no choice but to comply…":
            $ daughterParentsDeadAdvice_choice = 24
        "I shall flee and attempt to accomplish my dream! \
        They will see that I am not an object that stay put when I am lay aside after use! \
        Neterny is blocking the North border but he South is still opened to me.":
            $ daughterParentsDeadAdvice_choice = 25

    if (daughterParentsDeadAdvice_choice == 24):
        if (daughterWitch_option == 71):
            scene background princeCastle
            "It was with a heavy heart that Adélaïde resigned herself to what awaited her."
            "Her dread proved to be founded as King Frederic proved to be even more controlling \
            and insulting than her parents, humiliating her in public and brutal in private."
            "Adelaide was happy when she found herself pregnant, imagining that he would become softer with her."
            "She was wrong."
            "In the end, her body and mind did not have the energy necessary \
            to pull her through the birth and she died with her stillborn child."
        else:#daughterWitch_option == 72
            ade "Thoughts: At least I will get the opportunity to put the witch advice to good use, \
            I should definitely plot against my future husband and take the throne for myself…"

    else:#(daughterParentsDeadAdvice_choice = 25):
        show black
        hide adelaide with moveoutleft
        scene background a
        show adelaide at left
        ade "I should be close to the border by now…"
        show knight purple at right with moveinright
        knightP "Stop! Who goes there!"
        show adelaide surprised at left
        ade "!"
        show adelaide at left
        ade "Umm… I am Adélaïde of Arcance! \
        I have come to ask for asylum to your Lord! Lead me in front of him!"
        show black
        hide knight purple with moveoutright
        hide adelaide with moveoutleft

        scene background darkLordLair
        show adelaide at left
        show darkLord at right
        mLord "Well… what do we have here?"
        show adelaide scared at left
        ade "…\nThoughts: I do not like this. He looks very intimidating."
        mLord "What has bring you to our humble city, your Highness?"
        show adelaide at left
        ade "I am seeking refuge from my people."
        mLord "Oh?"
        ade "They want me to ‘negotiate’ with a dragon. \
        But I have heard them talk about royal sacrifice appeasing the beasts \
        and I was not mad enough to stay there!"
        mLord "How sensible of you…"
        show adelaide scared at left
        ade "What is that?! Black magic!"
        mLord "Stupid little girl… You have come to the castle of a Dark Lord all innocent and ignorant."
        dLord "Are you afraid of my power?"
        ade "No, no! In fact I quite like dark magic!"
        dLord "… very well."
        ade "Thoughts: I do not like that smile… What is he going to do…"
        "When the Dark Lord ended up using his dark magic to enslave her, Adelaide was not surprised.\
        She had no choice but to resign herself to a life of humiliation and privation."

    jump end
