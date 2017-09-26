# You can place the script of your game in this file.
# TODO: find right image size

# ==============================================
# background
image black = "#000000"
image white = "#ffffff"
image background a = "backgrounds/Arcance a.png"
image background b = "backgrounds/Arcance b.jpg"
image background c = "backgrounds/Arcance c.jpg"
image background d = "backgrounds/Arcance d.jpg"
image background e = "backgrounds/Arcance e.jpg"
image background f = "backgrounds/Arcance f.jpg"
image background g = "#ffffff"
image background h = "#ffffff"
image background i = "#ffffff"
image background j = "#ffffff"
image background k = "#ffffff"
image background darkLordLair = "backgrounds/Arcance dark lord lair.jpg"
image background dragonCave = "backgrounds/Arcance dragon cave.jpg"
image background princeCastle = "backgrounds/Arcance prince castle.jpg"



# avatars
image adelaide = Image("avatars/Adelaide avatar.png", xalign=0.5, yalign=0.649)
image side adelaide = im.FactorScale("avatars/Adelaide avatar.png", 0.5,0.5)
image side adelaide angry = im.FactorScale("avatars/Adelaide colere avatar.png", 0.5,0.5)
image side adelaide scared = im.FactorScale("avatars/Adelaide effrayee avatar.png", 0.5,0.5)
image side adelaide blushed = im.FactorScale("avatars/Adelaide rougit avatar.png", 0.5,0.5)
image side adelaide surprised = im.FactorScale("avatars/Adelaide surprise avatar.png", 0.5,0.5)

image side mage = im.FactorScale("avatars/Mage avatar.png", 0.5,0.5)
image side witch = im.FactorScale("avatars/old lady.png", 0.5,0.5)
image side darkLord = im.FactorScale("avatars/dark lord avatar.png", 0.5,0.5)

image side dragon = im.FactorScale("avatars/dragon avatar.png", 0.5,0.5)
image side knight blue = im.FactorScale("avatars/knight bleu.png", 0.5,0.5)
image side knight purple = im.FactorScale("avatars/knight violet.png", 0.5,0.5)
image side knight green = im.FactorScale("avatars/knight vert.png", 0.5,0.5)

image side king = im.FactorScale("Arcance king avatar.png", 0.5,0.5)
image side king laugh = im.FactorScale("Arcance king rit avatar.png", 0.5,0.5)
image side prince = im.FactorScale("Prince avatar.png", 0.5,0.5)


# ==============================================
# Character
define king = Character('King', color="#6e6ef7", show_side_image=Image("avatars/Arcance king avatar.png", xalign=0.5, yalign=0.649))
define queen = Character('Queen', color="#cc00b4")
define mage = Character('Head mage', color="#c8ffc8", show_side_image=Image("avatars/Mage avatar.png", xalign=0.5, yalign=0.649))
define ade = Character('Adelaide', color="#f96c9b", show_side_image=Image("avatars/Adelaide avatar.png", xalign=0.5, yalign=0.649))#, xalign=0.5, yalign=0.5))#"adelaide") #window_left_padding=165,
define unknown = Character('...', color="#d0d5d7")
define witch = Character('Old lady', color="#966c69", show_side_image=Image("avatars/old lady.png", xalign=0.5, yalign=0.649))
define guard = Character('Guard', color="#849294")
# $ art = Character("King Arthur", what_font="MyFont.ttf")


# ==============================================
# The game starts here.
label start:

    show background a
    with Dissolve(1.0)
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

        "grind seven rubies  in the goddess of the Arcance’s lands’ temple as an offering.":
            $ king_choice = 3

        "make his Queen drink elixirs of diluted occamy venom during each of the black moon of the pregnancy.":
            $ king_choice = 4


# ======
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

    else:
        mage "I am afraid that I have terrible news, your Majesty. The child was stillborn…"

        "The King was devastated by the news. Nevertheless, he resolved to try another time and, soon, the Queen was pregnant again.\
        This time, the King decided to"

        jump label_king_choice_menu


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

    show adelaide
    "Adelaide was a beautiful child, with hairs as bright as flame and eyes as green as emeralds. \
    Even so young she was already coveted by all the princes in the neighbours, a fact her father the King was very proud of."

    "Until one day, she they were declared to be of age. \
    However it was no time to party as the kingdom was under siege from all side…"

    show black
    with Dissolve(1.5)
    $ renpy.pause(1.0)
    hide text with dissolve
    jump label_daughter_witch


# ======
label end:
    mage "At the end of the story, this is the end of the game."
    return
