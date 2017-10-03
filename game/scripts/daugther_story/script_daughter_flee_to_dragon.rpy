### 16, 6->  = end of game ? ###
label daughterParentsFleeToDragon:
    scene dragonCave
    show adelaide

    ade "Uh, I am so tired! Why will this horse not go any faster! \
    I hate those animals, we should have already passed the border to Lancy by now! \
    If this continue, even Lancy will be at war with us and the border will be closed!"
    unknown "Roarrrrrr!"
    show adelaide surprise
    ade "Ah!"
    show adelaide angry
    ade "Stupid horse! You made me fall! Eh! Stop! Where are you going?"
    unknown "Booom"
    show adelaide scared
    ade "What is that?"
    unknown "Booom"
    show dragon at right
    unknown "Roarrrrrr!"
    show adelaide scared at left with moveinleft
    ade "A dragon! But none has been sighted in those mountain for at least a century!"
    dragon "Ssssss. A Little a human. \
    Not enough to satiate my hunger after sleeping so long but it will have to do…"

label daughterParentsFleeToDragon_firstChoice:
    ade "What should I do? I am going to die!"
    menu:
        "Thoughts: Really there is no choice there, \
        I can only attempt to flee and hope for the best…":
            $ daughterDragonDecision = 16
        "I should try to speak to it. I may be able to convince it not to it me… \
        It is not as if I have any other option…":
            $ daughterDragonDecision = 17

    if (daughterDragonDecision == 16):
        if(daughterWitch_option == 6):
            "As Adélaïde tried to flee, she felt a huge heat behind her and a brief pain. \
            She did not have time to realise that she was about to die."
            jump end
        else:#daughterWitch_option == 71,72,73,8
            jump daughterParentsFleeToDragon_decision

    else:#daughterDragonDecision == 17)
        show adelaide scared at left
        ade "No! Stop! As you said I am too little, it will practically make no difference if you eat me! \
        I can be of more use to you if you keep me alive!"
        dragon "Really? And pray tell me what use I have for a pest like you?"
        jump daughterParentsFleeToDragon_decision



label daughterParentsFleeToDragon_decision:
    #options 18 à 21
    ade "Umm.."
    ade "Thoughts: What should I do?"
    #{choix seulement possible si 7-1}20)
    #{choix seulement possible si 8 mais pas si 10-8}21)
    if(daughterWitch_option == 71):
        menu:
            "Really there is no choice there, I can only attempt to flee and hope for the best…":
                $ daughterDragonDecision = 18
            "I can cook for you!":
                $ daughterDragonDecision = 19
            "I can tell you story to distract you! You must be bored being all by yourself all the time!":
                $ daughterDragonDecision = 20
    elif(daughterWitch_option == 8 and ade_parents_choice != 10):
        menu:
            "Really there is no choice there, I can only attempt to flee and hope for the best…":
                $ daughterDragonDecision = 18
            "I can cook for you!":
                $ daughterDragonDecision = 19
            "I have this stone that a witch offered me! \
            I can give it to you in recompense for fighting the Arcla for my people! \
            \nThoughts: I may as well go all the way while I am at it…":
                $ daughterDragonDecision = 21
    else:
        menu:
            "Really there is no choice there, I can only attempt to flee and hope for the best…":
                $ daughterDragonDecision = 18
            "I can cook for you!":
                $ daughterDragonDecision = 19


    if (daughterDragonDecision == 18):
        "As Adélaïde tried to flee, she felt a huge heat behind her and a brief pain. \
        She did not have time to realise that she was about to die."
    elif(daughterDragonDecision == 19):
        dragon "What use do I have for that?"
        ade "Umm.."
        dragon "But alright, let’s try it! I just happen to have some meat on the side."
        "Adélaïde realised that she may not have thought this through when the dragon dragged \
        a human corpse out of his cave and set it atop a tree trunk."
        "Horrified and unable to resolve herself to “cut the meat”, \
        she could not react when the dragon pushed her on top of it and send them ablaze."
    elif(daughterDragonDecision == 20):
        dragon "..."
        dragon "Are you serious?"
        ade "Yes! I am a really talented story teller!"
        "Before the dragon’s incredulous look, Adélaïde hastened to launched into an elaborate story of \
        a dragon guarding a princess and roasting all the knight attracted by the famed promised to her rescuer."
        "After a time, she managed to get the dragon quite taken with the idea and ready to put it into practice."
        "It was not such a horrible life. The dragon fed her roasted lambs and fishes and \
        she got to devote her time to design and tell stories as she had always dreamed."
        "And, if after a while, she ended incorporating a Prince-dragon as the princess rescuer and future husband, \
        well none else would know of it."
    elif(daughterDragonDecision == 21):
        dragon "Umm… This is a powerful stone, worthy of being in my hoard… \
        And you only want me to roast some knights further down the river in exchange for it?"
        ade "Yes! \nThoughts: A powerful stone? Why did the witch just give it to me then?"
        dragon "In that case, we have a deal."
        scene background a
        "As expected, the dragon did a short work of the Arcla’s army. \
        By the end of it, even Adelide’s own people were begging her to become their \
        Queen and do them the honor of ruling them."
        "Of course, she may or may not have forgotten to share the fact that she did not, \
        in fact, control the dragon’s every move."
        scene background b
        "Her coronation was fantastic and Adelide looked quiete fetching with a crown on her head. \
        So much that even a certain Dark Lord gaze’s was caught. None noticed an old Lady sniggering at his side."

    jump end
