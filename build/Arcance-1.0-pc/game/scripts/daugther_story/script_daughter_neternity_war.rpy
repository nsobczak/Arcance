label daughterWarAgainstNeternity:
    scene background b
    show adelaide at left
    show knight blue at right
    knightB "What is your decision, your Highness?"
    show adelaide surprised at left
    ade "Oh? Now that there is something wrong, I am the one who is responsible?"
    ade "Thoughts: Umm, what should I do?"

    menu:
        " I have no choice, if we do not retaliate by declaring war against Neterny, \
        everyone who is not already at war with us will see that as a weakness and attack…":
            $ daughterWarAgainstNeternity_decision = 26
        "We cannot afford to be at war with even more people! \
        Even if we are not in a good position to do so, \
        I have to try to negotiate with Neterny…":
            $ daughterWarAgainstNeternity_decision = 27
        "The situation is doomed! They always insult me and refuse to listen to me \
        and now they dare ask me to take responsibility? Damned them! \
        I shall flee the country and leave them to deal with this mess themselves!":
            $ daughterWarAgainstNeternity_decision = 28

    hide knight blue
    hide adelaide
    show black
    scene background a
    if (daughterWarAgainstNeternity_decision == 26):
        "Troups were quickly called back from the Arcla front and they marched toward Neterny. \
        Despite all protest, Adelaide insisted to lead the army herself. \
        She was not going to leave her future in the hands of incapable politicians!"
        if (daughterWitch_option == 6):
            "Unfortunately, bad luck met them at every turn, \
            delaying them and weakening them even before the battle, \
            to think hat that she was cursed…"
            "None was expecting them to win and so none was surprised when they were massacred. \
            Adelaide herself died on the battle from a stray arrow."
        elif (daughterWitch_option == 8):
            "Contrary to all expactations, all seemed to turn in Adelaide’s favour. \
            Despite all their disadvantages, her army went from victory to victory, \
            becoming more and more enthusiast and enamoured with her."
            "Before long, Adelaide found herself besieging the capital of Neterny. \
            Yet, after only one week, the city decided to surrounder \
            and murder their King as a sign of good will."
            "One year after her parents’ murder, Adelaide was crowned Queen of Arcance and Neterny."
            "It was a very prestigious ceremony, all the sovergns of the neighbour countries \
            were present, even the King of Arcla who started to talk about a peace treaty."
            "And to crown it all, Adelaide may or may not have caught the eye of \
            the mysterious Mage leading the city-state on Arcance’s South border. \
            She would certainly not say to them learning more about each other…"
        else:#daughterWitch_option == 71, 72, 73
            "The battle was tight. Nevertheless, Arcance was too disadvantaged, \
            its soldiers weary from their march and their long years fighting Arcla before that."
            "They lost and Adelaide was captured. As a condition to peace, \
            the King of Neterny demanded that Adelaide marry him and give him the Arcance kingdom."
            "It was with a heavy heart that she resigned herself to what awaited her."
            scene background princeCastle
            "Her dread proved to be founded as King Frederic proved to be even more \
            controlling and insulting than her parents, humiliating her in public and brutal in private."
            "Adelaide was happy when she found herself pregnant, imagining that he would become softer with her."
            "She was wrong."
            "In the end, her body and mind did not have the energy necessary \
            to pull her through the birth and she died with her stillborn child."

    elif (daughterWarAgainstNeternity_decision == 27):
        "Adelaide was surprise but still suspicious when The King of Neterny \
        accepted to come to Arcance to disscuss his murder of her parents."
        "When he brought his army to the meeting, she could not protest. \
        And when he demanded that in exchange of his protection of Arcance \
        she marry him to join their kingdom, she also had to accept."
        "It was with a heavy heart that Adelaide resigned herself to what awaited her."
        scene background princeCastle
        "Her dread proved to be founded as King Frederic proved to be even more \
        controlling and insulting than her parents, humiliating her in public and brutal in private."
        "Adelaide was happy when she found herself pregnant, imagining that he would become softer with her."
        "She was wrong."
        "In the end, her body and mind did not have the energy necessary \
        to pull her through the birth and she died with her stillborn child."

    else:#daughterWarAgainstNeternity_decision == 28
        #TODO: finish this part
        show adelaide at left
        jump darkLordEnding


    jump end
