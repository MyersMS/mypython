from sys import exit

##################

def start():

    print "You just arrived in Yum Yum Yimma and asked to be dropped off"
    print "based on a number you choose between 0 to 10, what's your pick?"

    valid_input = False
    while not valid_input:

        print ""
######
        drop_off = int(raw_input(">"))
######
        print ""

        if drop_off >= 0 and drop_off < 6:

            ajegunle()
            valid_input = True

        elif drop_off >= 5 and drop_off < 11:

            ikoyi()
            valid_input = True

        else:

            print "Do you know how to read? Open your eyes %s" % name

        print ""

####################################################################### For the path to Ajegunle

def ajegunle():

    print "Low expectation, low results. You are dropped off in Ajegunle."
    print "This is the rough part of Yum Yum Yimma %s, and you definitely need to stay safe," % name
    print "what do you pick for protection? juju, a water gun or wisdom?"

    valid_input = False
    while not valid_input:

        print ""
######
        protection = raw_input(">")
######
        print ""

        if "juju" in protection:

            print "Very smart idea to pick something you don't know how to use."
            print "You light yourself on fire and burn to ashes."
            exit(0)

        elif "gun" in protection:

            print "Have you ever used a water gun before? You accidentally shoot your knee"
            print "You're left stranded and eaten alive by fire ants"
            exit(0)

        elif "wisdom" in protection:

            wisdom()
            valid_input = True

        else:

            print "Do you know how to read? Open your eyes %s" % name

        print ""

##################

def wisdom():

    print "Good choice, you would need to be street smart to survive around here."
    print "Let's see how you use this wisdom. So you get stuck at 2am in a very sketchy place"
    print "and you have no money. The only was back is a bus that would cost N500, it's your"
    print "lucky day and you see a N500 note crumbled below you. What do you do?"
    print "Pick it up, ignore it or steal the bus?"

    valid_input = False
    while not valid_input:

        print ""
######
        bus = raw_input(">")
######
        print ""

        if "pick it up" in bus:

            print "Bad idea to pick up items you don't own here."
            print "You magically transform into a piece of yam and"
            print "used to make  porridge to feed your neighbors dog."
            exit(0)

        elif "ignore" in bus:

            print "You get kidnapped and because friends and family don't like you,"
            print "you get sold for N0 to a Hannibal Lecter who slowly cuts you to pieces"
            print "and eats you for breakfast every day."
            exit(0)

        elif "steal" in bus:

            print "Great job! Stealing feels GREAT! Let's drive off into the sunset!"
            final()

        else:

            print "Do you know how to read? Open your eyes %s" % name

        print ""

##################

def final():

    print "Well you're not really driving into the sunset yet"
    print "In the bus you find a one way ticket package to go anywhere in the world."
    print "This package comes with $1 billion to spend and whatever country you"
    print "decide to go, you must live there forever."
    print "Which country will you go to?"

    valid_input = False
    while not valid_input:

        print ""
######
        final_answer = raw_input(">")
######
        print ""

        if "Nigeria" in final_answer:

            print "Wise choice. You've made the best decision in your life and you live happily ever after!"
            print "THE END :)"
            exit(0)

        else:

            print "Poor, poor choice! What's wrong with you???"
            print "If you don't make the right choice, you're going no where"

####################################################################### For the path to Ikoyi

def ikoyi():

    print "High expectation, high results %s. You are dropped off in" % name
    print "Ikoyi, good place to start off and lots of things to do."
    print "What would you like to do? Tour town or go relax in Ikoyi club?"

    valid_input = False
    while not valid_input:

        print ""
######
        to_do = raw_input(">")
######
        print ""

        if "tour" in to_do:

            hawker()
            valid_input = True

        elif "relax" in to_do:

            email()
            valid_input = True

        else:

            print "Do you know how to read? Open your eyes %s" % name

        print ""

##################

def hawker():

    print "During the tour, you are thirsty and want to buy a drink"
    print "from a street hawker. You ask for water and he says it cost N3,000."
    print "What do you do? drive off or buy it?"

    valid_input = False
    while not valid_input:

        print ""
######
        thirst = raw_input(">")
######
        print ""

        if "drive off" in thirst:

            print """You die of thirst"""
            exit(0)

        elif "buy it" in thirst:

            print "You clearly are not a smart %s. Who buys water for N5,000?." % name
            print "You wouldn't last in Yum Yum Yimma."
            exit(0)

        else:

            print "Do you know how to read? Open your eyes %s" % name

        print ""

##################

def email():

    print "You definitely need the relaxation. While doing so, you decide to check"
    print "your email and a Prince in Yum Yum Yimma notifies you that he needs money to"
    print "cover the cost of his mother's funeral. What do you do? Send money or ignore?"

    valid_input = False
    while not valid_input:

        print ""
######
        mother = raw_input(">")
######
        print ""

        if "money" in mother:

            print "You get scammed. You're obviously broke and"
            print "lose your life savings, $63.51 to him."
            exit(0)

        elif "ignore" in mother:

            print "You're heartless. Society doesn't need people like you."
            exit(0)

        else:

            print "Do you know how to read? Open your eyes %s" % name

        print ""

#######################################################################

print "What is your name?"

print ""
######
name = raw_input(">")
######
print ""

print "So let's play this scenario out %s." % name

print ""
start() 
