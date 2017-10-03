﻿# You can place the script of your game in this file.

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

# jump to or
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

    jump end

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
    jump end

label daughterParents_option11:
    $ ade_parents_choice = 11
    ade "thought : But, could it be my chance?\
    Surely the kingdom will have no other choice but to turn toward me!"
    ade "Alright father. You are right, this is silly of me, I should trust you to know better!"
    show king laugh at right
    king "Indeed! Eh, eh, eh! Do not worry, I will still bring you a souvenir!"
    jump end


jump end
