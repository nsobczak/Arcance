﻿# You can place the script of your game in this file.
# TODO: find right image size

# ==============================================

# background
image black = "#000000"
image white = "#ffffff"
image background a = "backgrounds/Arcance a.png"
image background b = "backgrounds/Arcance b.png"
image background c = "backgrounds/Arcance c.png"
image background d = "backgrounds/Arcance d.png"
image background e = "backgrounds/Arcance e.jpg"
image background f = "backgrounds/Arcance f.png"
image background g = "#ffffff"
image background h = "#ffffff"
image background i = "#ffffff"
image background j = "#ffffff"
image background k = "#ffffff"
image background darkLordLair = "backgrounds/Arcance dark lord lair.png"
image background dragonCave = "backgrounds/Arcance dragon cave.png"
image background princeCastle = "backgrounds/Arcance prince castle.jpg"
image background title = "backgrounds/Arcance page de titre.png"


# avatars
define avatarXAlign = 0.5
define avatarYAlign = 0.649
define left = Position(xpos=0.0, ypos=avatarYAlign, xanchor='left')
define center = Position(xpos=0.5, ypos=avatarYAlign, xanchor='center')
define right = Position(xpos=1.0, ypos=avatarYAlign, xanchor='right')
#$ top = Position(xpos=0.5, xanchor='center', ypos=0.0, yanchor='top')
image adelaide = Image("avatars/Adelaide avatar.png", xalign=avatarXAlign, yalign=avatarYAlign)
#image side adelaide = Image("avatars/Adelaide avatar.png", xalign=avatarXAlign, yalign=avatarYAlign)
image adelaide angry = Image("avatars/Adelaide colere avatar.png", xalign=avatarXAlign, yalign=avatarYAlign)
image adelaide scared = Image("avatars/Adelaide effrayee avatar.png", xalign=avatarXAlign, yalign=avatarYAlign)
image adelaide blushed = Image("avatars/Adelaide rougit avatar.png", xalign=avatarXAlign, yalign=avatarYAlign)
image adelaide surprised = Image("avatars/Adelaide surprise avatar.png", xalign=avatarXAlign, yalign=avatarYAlign)

image mage = Image("avatars/Mage avatar.png", xalign=avatarXAlign, yalign=avatarYAlign)
image witch = Image("avatars/old lady.png", xalign=avatarXAlign, yalign=avatarYAlign)
image darkLord = Image("avatars/dark lord avatar.png", xalign=avatarXAlign, yalign=avatarYAlign)

image dragon = Image("avatars/dragon avatar.png", xalign=avatarXAlign, yalign=avatarYAlign)
image knight blue = Image("avatars/knight bleu.png", xalign=avatarXAlign, yalign=avatarYAlign)
image knight purple = Image("avatars/knight violet.png", xalign=avatarXAlign, yalign=avatarYAlign)
image knight green = Image("avatars/knight vert.png", xalign=avatarXAlign, yalign=avatarYAlign)

image king = Image("avatars/Arcance king avatar.png", xalign=avatarXAlign, yalign=avatarYAlign)
image king laugh = Image("avatars/Arcance king rit avatar.png", xalign=avatarXAlign, yalign=avatarYAlign)
image prince = Image("avatars/Prince avatar.png", xalign=avatarXAlign, yalign=avatarYAlign)


# ==============================================
# Character
define king = Character('King', color="#665AB0", window_left_padding=250, show_side_image=im.Composite((config.screen_width, config.screen_height), (0, config.screen_height-150), im.FactorScale("avatars/Arcance king avatar.png", 0.5, 0.5)))
define queen = Character('Queen', color="#cc00b4", window_left_padding=100)
define mage = Character('Head mage', color="#c8ffc8", window_left_padding=100, show_side_image=im.Composite((config.screen_width, config.screen_height), (5, config.screen_height-150), im.FactorScale("avatars/Mage avatar.png", 0.5, 0.5)))
define ade = Character('Adelaide', color="#EF7955", window_left_padding=100, show_side_image=im.Composite((config.screen_width, config.screen_height), (5, config.screen_height-150), im.FactorScale("avatars/Adelaide avatar.png", 0.5, 0.5)))
define unknown = Character('...', color="#d0d5d7", window_left_padding=100)
define witch = Character('Old lady', color="#A8A4A3", window_left_padding=100, show_side_image=im.Composite((config.screen_width, config.screen_height), (5, config.screen_height-150), im.FactorScale("avatars/old lady.png", 0.5, 0.5)))
define guard = Character('Guard', color="#849294", window_left_padding=100)
define knightB = Character('Blue knight', color="#5e76a1", window_left_padding=230, show_side_image=im.Composite((config.screen_width, config.screen_height), (5, config.screen_height-150), im.FactorScale("avatars/knight bleu.png", 0.5, 0.5)))
define knightP = Character('Purple knight', color="#7f5ea1", window_left_padding=230, show_side_image=im.Composite((config.screen_width, config.screen_height), (5, config.screen_height-150), im.FactorScale("avatars/knight violet.png", 0.5, 0.5)))
define knightG = Character('Green knight', color="#5b9570", window_left_padding=230, show_side_image=im.Composite((config.screen_width, config.screen_height), (5, config.screen_height-150), im.FactorScale("avatars/knight vert.png", 0.5, 0.5)))
define dragon = Character('Dragon', color="#AEFFF0", window_left_padding=230, show_side_image=im.Composite((config.screen_width, config.screen_height), (5, config.screen_height-150), im.FactorScale("avatars/dragon avatar.png", 0.5, 0.5)))
define prince = Character('Prince', color="#398D01", window_left_padding=180, show_side_image=im.Composite((config.screen_width, config.screen_height), (5, config.screen_height-150), im.FactorScale("avatars/Prince avatar.png", 0.5, 0.5)))
define mLord = Character('Mysterious Lord', color="#949494", window_left_padding=200, show_side_image=im.Composite((config.screen_width, config.screen_height), (5, config.screen_height-150), im.FactorScale("avatars/dark lord avatar.png", 0.5, 0.5)))
define dLord = Character('Dark Lord', color="#9a280e", window_left_padding=200, show_side_image=im.Composite((config.screen_width, config.screen_height), (5, config.screen_height-150), im.FactorScale("avatars/dark lord avatar.png", 0.5, 0.5)))
# $ art = Character("King Arthur", what_font="MyFont.ttf")


# ==============================================
# The game starts here.
label start:
    show background title with Dissolve(1.0)
    #show dragon at right with dissolve
    #show darkLord at left with dissolve
    $ renpy.pause()
    show background a with Dissolve(1.0)
    "Once upon a time, in the magnificent kingdom of Arcance, lived a King and a Queen. \
    Both had just acceded to the throne after the death of the old King and they were greatly loved by their people."

    scene background b
    "In those hard times, the presence of a strong figure at the head of the kingdom was reassuring. \
    Only the absence of an heir could threaten their stability. \
    Therefore, when the queen announced that she had conceived, everyone was delighted and big rejoicings occurred in the whole country."

    scene background c
    "The king was overjoyed to learn the news, but a small worry still clouded his mind. \
    Would a boy or a girl be better under the current circumstances?"

    "A boy could lead the army in his stead and take some of pressure of him so that he could focus on diplomacy and politics, \
    while a girl would allow him to conclude a strong alliance with one of his neighbours and play them against each other by dangling this opportunity in front of them…"

    scene background d
    "His mind made up, the King consulted his mages and mages. Following their advices, the King decided that he would:"


label label_king_choice_menu:
    menu:
        "dance in a circle of dolmens during each of the full moon that would occur during the pregnancy, holding a crone of saffron.":
            $ king_choice = 1

        "sacrifice three swans and pour their blood on the ground to appeal to his ancestors during the summer solstice.":
            $ king_choice = 2

        # "grind seven rubies  in the goddess of the Arcance’s lands’ temple as an offering.":
        #     $ king_choice = 3
        #
        # "make his Queen drink elixirs of diluted occamy venom during each of the black moon of the pregnancy.":
        #     $ king_choice = 4


# ======
label king_choice:
    scene background d
    "The King diligently carried out his task, hoping for the best."

    scene background e
    "When the pregnancy came to its term, everyone gathered with excitation in the Queen’s antechamber, waiting for the news. \
    The King kept pacing around listeining anxiously to the agony cries of the Queen."

    scene background f
    "After several hours, the Head mage burst out of the chamber, a small bundle in his arm."

    show mage at left
    if (king_choice == 1):
        mage "Congratulation your Majesty, it’s a girl!"

    else:
        mage "I am afraid that I have terrible news, your Majesty. The child was stillborn…"
        hide mage

        "The King was devastated by the news. Nevertheless, he resolved to try another time and, soon, the Queen was pregnant again.\
        This time, the King decided to"

        scene background d
        jump label_king_choice_menu

    hide mage
    scene background a
    "The birth was celebrated in the whole kingdom for days. \
    It was seen as a sign of hope, a bright light shining before the darker times to come… "

    show black
    with Dissolve(1.5)
    $ renpy.pause(1.0)
    hide text with dissolve

    scene background a
    with Dissolve(1.0)
    "Years passed and with them went the peace and prosperity of the kingdom. \
    Nevertheless, the child grew and learnt."

    show adelaide with dissolve
    "Adelaide was a beautiful child, with hairs as bright as flame and eyes as green as emeralds. \
    Even so young she was already coveted by all the princes in the neighbours, a fact her father the King was very proud of."

    "Until one day, she they were declared to be of age. \
    However it was no time to party as the kingdom was under siege from all side…"

    hide adelaide #with dissolve
    show black with Dissolve(1.5) #$ renpy.pause(1.0)
    hide text with dissolve
    jump daughterWitch


# ======
label end:
    "Game Over"#This is the end of the game."
    return
