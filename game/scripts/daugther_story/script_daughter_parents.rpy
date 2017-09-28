# You can place the script of your game in this file.

# jump to daughterParents_option9 or daughterParents_option10 or daughterParents_option11
label daughterParent:
    scene background b
    show adelaide at left
    show king at right
    with dissolve
    king "My daughter, we have to leave the kingdom next week to go to Neterny"
    show adelaide surprised at left
    ade "What? Neterny? What for?"
    show adelaide at left
    ade "It is not foolish to leave the country while we are at war! \
    Arcla will certainly heard of this and take advantage of the situation!"
    king "Do not talk to me like this, daughter!"
    show adelaide angry at left
    ade "..."
    show adelaide at left
    ade "I apologise, Father. Could you please share with me the reasons that motivate your decision?"
    king "Umm! Alright. You Mother and I are going there to make an alliance with King Frederic. \
    As you noticed, we can use all the help we can find in this day and age…"
    show adelaide blushed at left
    ade "..."
    show adelaide at left

    menu:
        "Alright. I wish you luck in your travel then…":
            jump daughterParents_option9
        "Indeed, but it does not negate the danger!":
            jump daughterParents_option10
        "How annoying… I am sure something bad will happen.":
            jump daughterParents_option11

# jump to daughterParents_follow_1
label daughterParents_option9:
    $ ade_parents_choice = 9
    king "Ah… If this reassure you, we will go through the mountain. \
    That way Arcla will have no way to know that we have left!"
    ade "Thank you, Father. I already feel better knowing that."
    if (daughterWitch_option == 8):
        ade "thoughts : Should I also give him the witch’s stone?"
        menu:
            "No, the mountain road should be safe enough, \
            I had better keep it for a situation that really needs it!":
                $ daughter_stone_option = 12

            "Please also take this stone with you. \
            A witch told me that it was magical. \
            It may be able to protect you.":
                $ daughter_stone_option = 13
                king "Well, if this can reassure you…"
                show king laugh at right
                king "Women!"

    jump daughterParents_follow_1

# jump to daughterParents_follow_1 or # jump to daughterParents_follow_2
label daughterParents_option10:
    $ ade_parents_choice = 10
    king "Do not worry your pretty little head over this. \
    Duke Laurence will certainly be able to protect the kingdom in my absence"

    if (daughterWitch_option == 73):
        show adelaide angry at left
        ade "I have heard that a powerful mage wish to conquer the continent! \
        He will certainly use this time to act!"
        king "Alright. If you are so sure we will not go. \
        It is true that we cannot risk getting mages involved in top of everything else!"
        show adelaide at left
        ade "Thank you for trusting me, Father!"
    elif (daughterWitch_option == 6 or daughterWitch_option == 71 or daughterWitch_option == 72):
        ade "Are you sure he will be able to handle the situation by himself? \
        May I give him some advices on how to handle the situation?"
        if (daughterWitch_option == 6):
            show king laugh at right
            king "Balderdash! You had better leave politics to men, \
            gullible as you are! Ah, ah, ah!"
            show adelaide angry at left
            ade "Rah! I hate men!"
        else:
            king "Alright, if it make you feel useful… \
            Although do not be surprised if he does not listen to you! \
            He is the one with the experience after all!"
    elif (daughterWitch_option == 8):
        ade "At the very least take this stone. \
        A witch told me that it was magical. \
        It may be able to protect you."
        king "Well, if this can reassure you…"
        show king laugh at right
        king "Women!"
    jump daughterParents_follow_1

# jump to daughterParents_follow_1
label daughterParents_option11:
    $ ade_parents_choice = 11
    ade "thought : But, could it be my chance?\
    Surely the kingdom will have no other choice but to turn toward me!"
    ade "Alright father. You are right, this is silly of me, I should trust you to know better!"
    show king laugh at right
    king "Indeed! Eh, eh, eh! Do not worry, I will still bring you a souvenir!"

    jump daughterParents_follow_1

label daughterParents_follow_1:
    hide adelaide
    hide king
    hide text with dissolve
    show black with dissolve

    if (ade_parents_choice == 10 and daughterWitch_option == 73):
        jump daughterParentsStay
    else:
        jump daughterParents_follow_2

label daughterParents_follow_2:
    show knight blue at right with dissolve
    knightB "Your Highness, I am afraid that I have some very distressing news…"
    show adelaide at left
    ade "What is it?"

    if (ade_parents_choice == 9 and daughterWitch_option == 8):
        if (daughter_stone_option == 12):
            knightB "Their Majesties have been eaten by a dragon."
            show adelaide surprised at left
            ade "What???!"
            show adelaide at left
            knightB "I am afraid that you people are clamouring for a sacrifice to be made to appease the dragon."
            ade "..."
            knightB "A royal sacrifice."
            ade "..."
            knightB "Please follow me your Highness."
        else: #daughter_stone_option == 13
            knightB "Their Majesties have been taken prisoner by a dragon."
            show adelaide surprised at left
            ade "What???!"
            show adelaide at left
            knightB "I am afraid that you have no choice but to go and negotiate their release yourself."

    elif ((ade_parents_choice == 10) and (daughterWitch_option == 6 or daughterWitch_option == 71 or daughterWitch_option == 72)):
        knightB "Their Majesties have been assassinated by the King of Neterny."
        show adelaide surprised at left
        ade "What???!"

    elif (ade_parents_choice == 10 and daughterWitch_option == 8):
        knightB "Their Majesties have been able to conclude an alliance with Neterny…"
        ade "That sounds like very good news."
        knightB "Unfortunately, the King condition was your hand in marriage…"
        ade "thoughts: … I should have seen that coming."

    else: #ade_parents_choice == 11
        knightB "Their Majesties have been assassinated by the King of Neterny."
        show adelaide surprised at left
        ade "What???!"

    hide adelaide
    hide knightB
    hide text with dissolve
    show black with dissolve

    jump end
