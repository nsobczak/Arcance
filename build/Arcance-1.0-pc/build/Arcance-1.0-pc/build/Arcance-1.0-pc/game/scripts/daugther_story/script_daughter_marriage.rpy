label daughterParentsMarriage:
    scene background b with dissolve
    show adelaide scared at left
    ade "thoughts: What should I do? I have know all my life that they would want me to get married to a stranger"
    menu:
        "I guess I have no choice but to comply…":
            #$ daughterParentsMarriage_choice = 14
            jump daughterParentsMarriageAlliance
        "I shall flee and attempt to accomplish my dream! \
        They will see that I am not an object that stay put when I am lay aside after use!":
            #$ daughterParentsMarriage_choice = 15
            jump daughterParentsFleeToDragon

label daughterParentsMarriageAlliance:

    show adelaide at left
    show prince at right
    prince "Well, princess, I am positively delighted to make your acquaintance."
    ade "..."
    ade "So do I."
    prince "We are going to have a lot of fun tonight, you and I!"
    ade "..."
    ade "thoughts: He is positively odious! \
    Nevertheless I have already decided to go through with this wedding…\
    What should I do about him now?"

    menu:
        "The most reasonable option surely is to seduce him and exercise power through, but can I pull this off?":
            $ aboutPrince = 29
        "Who care about reasonable? I shall not suffer him any longer than absolutely necessary! \
        I am getting rid of him as soon as possible and I will then be the regent until his nephew gain his majority!":
            $ aboutPrince = 30

    if (aboutPrince == 29):
        show adelaide blushed at left
        ade "My King, please allow me to compliment you on:"
        menu:
            "Your handsome form. You must surely exercise a great deal with your knight to be so fit!":
                $ aboutPrince = 31
            "Your impressive army! You have been able to bring so many people here and on so short a notice,\
             your country must be so well organised and ruled!":
                $ aboutPrince = 32

        if (aboutPrince == 31):
            "Surprisingly, this actually worked and Adelaide could see the King puffed his chest smugly in answer."
            "Well, as long as she managed to stroke his vanity with some appearance of vanity she was fine after all!"
            "And so, Adelaide started her married life in this way. By always having a compliment ready for him, \
            she quickly managed to ingratiate herself to King Frederic and to secure her position in the Court of Neterny."
            "She managed to get some independence but she had to forgo all her childhood dreams."
            "And a few years later even this modest peace was threatened \
            when rumours of a new Dark Lord hell bent on conquering the whole continent started to emerge…"
        else: #aboutPrince == 32
            "Unfortunately for Adelaide, the King was not so impressed by this \
            but instead saw this as an attempt at spying on Neterny for Arcance."
            "How he could have come to this conclusion baffled Adelaide, \
            but she could not help but feel some trepidations when she thought of her future by his side."
            "Her dread proved to be founded as King Frederic proved to be even more controlling and insulting than her parents, \
            humiliating her in public and brutal in private."
            "Adelaide was happy when she found herself pregnant, imagining that he would become softer with her."
            "She was wrong."
            "In the end, her body and mind did not have the energy necessary to pull her \
            through the birth and she died with her stillborn child."

    else: #aboutPrince == 30
        ade "thoughts: That’s decided, I am going to:"
        menu:
            "Make him think he is so extraordinary that now that he is the heir to the Arcance throne\
             he can conquer all his neighbours without any difficulties":
                $ aboutPrince = 33
            "Play his vassals against him. \
            There are bound to be some that held a grudge against him and only need a little encouragement!":
                $ aboutPrince = 34

        if (aboutPrince == 33):
            ade "thoughts: He is bond to end up getting himself killed in one of those battles."
            ade "thoughts: In addition I have heard that some of those Southern states have been making mysterious manoeuvre recently. \
            Neterny may even be defeated!"
            hide adelaide
            hide prince
            scene black with dissolve
            "Everything worked according to plan."
            "In the following months, under Adelaide’s encouragement, \
            her new husband King Frederic declared war on his closer neighbour, the King of Letria."
            "After he came back from a bloody campaign, swollen by his victory, \
            he was easy to convince to invade the next kingdom."
            "And then the next one."
            "And the one after that."
            "Adelaide was starting to lost all hope of King Frederic dying when she finally received the news \
            that he had been struck down by black lightening while attempting to besiege one of the Southern city-state \
            that just happened to be ruled by a Dark Lord!"
            "She could not believe her luck!"
            "However Neterny now had a lot of enemy and she could not savour her triumph for long."
            "And so she decided to go in person meet this new Dark Lord and see if she could not establish an alliance with him."
            "The rest of the continent was still vast after all…"

        else: #aboutPrince == 34
            ade "thoughts: And the advantage of this is that it is going to be quick!"
            hide adelaide
            hide prince
            scene black with dissolve
            "It was indeed quick."
            "A bit too quick."
            "Unfortunately for Adelaide, her new allies proved to be too green and naïve \
            and had to pose with his dagger held above the King to declaim the reasons of his betrayal, \
            thus giving enough for the Neterny guards to interrupt him."
            "Torture was also quick to untie his tongue after that and he told the King of Adelaide role in the plot."
            "She was not executed as her presence was needed to secure the Neterny-Arcance alliance \
            but King Frederic then lost all pretence of being a passable husband."
            "He proved to be even more controlling and insulting than her parents, \
            humiliating her in public and brutal in private."
            "Adelaide was happy when she found herself pregnant, imagining that he would become softer with her."
            "She was wrong."
            "In the end, her body and mind did not have the energy necessary to pull her \
            through the birth and she died with her stillborn child."

    jump end
