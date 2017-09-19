# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
# Declare characters used by this game.


# The game starts here.
label label_daughter_witch:
    scene background h
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

    ade "Who is there?!"

    unknown "Reassure yourself, child. It is only, I, an old Lady."

    ade "You have no right to be here! How did you manage to get into the castle? /\
    Oh, you surprised me! May I ask you what you are doing here?"

    oldLady "A bit of politeness would do you some good.\
    Just passing by…"

    jump end
