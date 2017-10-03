label daughterParentsMeetDragon:
    if(daughter_stone_option==12):
        hide adelaide with moveoutleft
        hide knightB with moveoutright
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


label daughterParentsMeetDragon_option23:


    jump end
