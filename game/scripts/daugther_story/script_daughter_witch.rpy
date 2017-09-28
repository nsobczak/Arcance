# You can place the script of your game in this file.

# jump to 4 or 5
label daughterWitch:
    scene background b
    show adelaide with dissolve

    ade "I hate this kingdom! \
    Why do they have to treat me as an ornement or a broodmare, just good enough to give to the highest bidder and produce children! \
    And then Mother and Father get upset because I do not accept the situation and follow all their order with a smile!"

    ade "Everyone is the same in the kingdom! \
    Just because I am a girl they presume they have a right to dictate my every thought and actions and to dispose of my person as they wish. \
    From the lowest commoners to the noblest of Dukes they are all the same!"

    ade "I wish I had the courage to flee and decide for myself what I wish to do with my life… I could become"

    menu:
        "The best artist in the land and make a name for myself!":
            $ ade_witch_choice = 1
        "The best diplomat in the land, someone that could persuade anyone of anything!":
            $ ade_witch_choice = 2
        "Someone powerful who would not have to follow anyone’s order!":
            $ ade_witch_choice = 3

    unknown "Mmm, what an ambitious wish…"
    show adelaide at left
    show witch at right with moveinright
    with dissolve
    ade "Who is there?!"
    witch "Reassure yourself, child. It is only, I, an old Lady."

    menu:
        "You have no right to be here! How did you manage to get into the castle?":
            jump daughterWitch_option4
        "Oh, you surprised me! May I ask you what you are doing here?":
            jump daughterWitch_option5

# jump to 6 or 7
label daughterWitch_option4:
    witch "A bit of politeness would do you some good."
    ade "She looks suspicious, is she a spy or an assassin? What should I do?"

    menu:
        "Guards!":
            jump daughterWitch_option6
        "I apologise, but we are at war. I am afraid that we cannot afford to lower our caution…":
            jump daughterWitch_option7

# jump to 7 or 8
label daughterWitch_option5:
    witch "Just passing by…"
    ade "She looks suspicious, is she a spy or an assassin? What should I do?"

    menu:
        "I apologise, but we are at war. I am afraid that we cannot afford to lower our caution…":
            jump daughterWitch_option7
        "In that case, please do not let me detain you.":
            jump daughterWitch_option8

# jump to end
label daughterWitch_option6:
    $ daughterWitch_option = 6
    ade "Ah! What is this light? What have you done?"
    witch "This aught to teach you to respect your elder."
    guard "Your highness, is there a problem?"
    ade "This witch cursed me!"
    hide witch with moveoutright
    ade "..."
    ade "Where did she go?!"
    jump daughterWitch_end

# jump to daughterWitch_witchEscape
label daughterWitch_option7:
    witch "I understand. Here is a piece of advice that may help you in those dark times."

    if (ade_witch_choice == 1):
        $ daughterWitch_option = 71
        witch "Even if men cannot appreciate a woman’s talent, they are not the only creature to inhabit this Earth!"
        witch "Nor are they the mightiest despite what they may choose to think…"
        ade "Yet I have heard that magic can make of human something more, able to challenge anything!"

    elif (ade_witch_choice == 2):
        $ daughterWitch_option = 72
        witch "You may despise being underestimated for your sex, \
        but I have often find that normal men easily underestimate their wife \
        and present them their back without second thoughts…"
        witch "As long as there is a child to be regent for… Something to think about, eh?"

    else:
        $ daughterWitch_option = 73
        witch "Magic is the answer to your problem. My Lord went from an orphanage to a castle\
         and he will soon reign over the whole continent thanks to his powerful magic. \
        Starting so high yourself, you aught to be able to make something of yourself."

    jump daughterWitch_witchEscape

# jump to daughterWitch_witchEscape
label daughterWitch_option8:
    $ daughterWitch_option = 8
    witch "Not so quick. You appear to be a good girl and I wish to help you.\
    Here take this stone. It aughts to make thing… interesting."
    jump daughterWitch_witchEscape

# jump to end
label daughterWitch_witchEscape:
    witch "He, he, he"
    hide witch with moveoutright
    ade "Ah! What is this smoke?"
    ade "Uh? Where did she go?"

    show black with Dissolve(1.5)
    $ renpy.pause(0.5)
    hide text

    jump daughterWitch_end


label daughterWitch_end:
    jump daughterParent
