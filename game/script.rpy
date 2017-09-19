﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image black = "#000000"
image white = "#ffffff"
image background a = "Arcance a.jpg"
image background b = "Arcance b.jpg"
image background c = "Arcance c.jpg"
image background d = "Arcance d.jpg"
image background e = "Arcance e.jpg"
image background f = "Arcance f.jpg"

# Declare characters used by this game.
define king = Character('King', color="#aaffc8")
define mage = Character('Head mage', color="#c8ffc8")


# The game starts here.
label start:

    scene background a
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
            jump king_choice

        "sacrifice three swans and pour their blood on the ground to appeal to his ancestors during the summer solstice.":
            $ king_choice = 2
            jump king_choice

        "grind seven rubies  in the goddess of the Arcance’s lands’ temple as an offering.":
            $ king_choice = 3
            jump king_choice

        "make his Queen drink elixirs of diluted occamy venom during each of the black moon of the pregnancy.":
            $ king_choice = 4
            jump king_choice


#======
label king_choice:
    scene background d
    "The King diligently carried out his task, hoping for the best."

    scene background e
    "When the pregnancy came to its term, everyone gathered with excitation in the Queen’s antechamber, waiting for the news. \
    The King kept pacing around listeining anxiously to the agony cries of the Queen."

    scene background f
    "After several hours, the Head mage burst out of the chamber, a small bundle in his arm."

    if (king_choice == 1):
        mage "Congratulation your Majesty, it’s a girl!"
        jump end
    else:
        mage "I am afraid that I have terrible news, your Majesty. The child was stillborn…"

        "The King was devastated by the news. Nevertheless, he resolved to try another time and, soon, the Queen was pregnant again.\
        This time, the King decided to"

        jump label_king_choice_menu



#======
label end:
    mage "At the end of the story, this is the end of the game."



    return