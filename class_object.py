from sys import exit
from random import randint

##############

class Level_one(object):

    life = 10

    def action_one(self):

        print "Introductory Stage"
        print "You have a life level of 10."
        print "Where do you go? Left or Right?"
        direction = raw_input(">")

        if (direction == "left"):

            print "Message from scene. This is the path taking you to the LEFT'"
            Level_two_a().run()

        elif (direction == "right"):

            print "Message from scene. This is the path taking you to the RIGHT"
            Level_two_b().run()

        else:
            print "Do you know how to read? Open your eyes"
            #Put loop here
            exit(0)

########################################################

class Level_two_a(object):

    def two_a (self):

        print "Message from scene. Do something."
        something = raw_input(">")

        if (something == "A"):

            self.life += 2
            print "Message from scene. Do something.2a"
            print self.life
            Level_three_a().run()

        elif (something == "AA"):

            self.life -= 2
            print "Message from scene. Do something.22a"
            print self.life
            Level_three_a().run()

        else:
            print "Do you know how to read? Open your eyes"
            exit(0)
            #Put loop here

##############

class Level_two_b(object):

    def two_b (self):

        print "Message from scene. Do something."
        something = raw_input(">")

        if (something == "B"):

            self.life += 2
            print "Message from scene. Do something.2b"
            print self.life
            Level_three_b().run()

        elif (something == "BB"):

            self.life -= 2
            print "Message from scene. Do something.22b"
            print self.life
            Level_three_b().run()

        else:
            print "Do you know how to read? Open your eyes"
            exit(0)
            #Put loop here

########################################################

class Level_three_a(object):

    def three_a (self):

        print "Message from scene. Do something."
        something = raw_input(">")

        if (something == "A"):

            self.life += 2
            print "Message from scene. Do something.3a"
            print self.life
            Level_four_a().run()

        elif (something == "AA"):

            self.life -= 2
            print "Message from scene. Do something.33b"
            print self.life
            Level_four_a().run()

        else:
            print "Do you know how to read? Open your eyes"
            exit(0)
            #Put loop here

##############

class Level_three_b(object):
    
    def three_b (self):

        print "Message from scene. Do something."
        something = raw_input(">")

        if (something == "B"):

            self.life += 2
            print "Message from scene. Do something.3b"
            print self.life
            Level_four_b().run()

        elif (something == "BB"):

            self.life -= 2
            print "Message from scene. Do something.33b"
            print self.life
            Level_four_b().run()

        else:
            print "Do you know how to read? Open your eyes"
            exit(0)
            #Put loop here

########################################################

class Level_four_a(object):

    def four_a (self):

        print "Message from scene. Do something."
        something = raw_input(">")

        if (something == "A"):

            self.life += 2
            print "Message from scene. Do something.4a"
            print self.life
            Level_five_a().run()

        elif (something == "AA"):

            self.life -= 2
            print "Message from scene. Do something.44a"
            print self.life
            Level_five_a().run()

        else:
            print "Do you know how to read? Open your eyes"
            exit(0)
            #Put loop here


##############

class Level_four_b(object):

    def four_b (self):

        print "Message from scene. Do something."
        something = raw_input(">")

        if (something == "B"):

            self.life += 2
            print "Message from scene. Do something.4b"
            print self.life
            Level_five_b().run()

        elif (something == "BB"):

            self.life -= 2
            print "Message from scene. Do something.44b"
            print self.life
            Level_five_b().run()

        else:
            print "Do you know how to read? Open your eyes"
            exit(0)
            #Put loop here

########################################################

class Level_five_a(object):
        
    def five_a (self):

        print "Message from scene. Do something."
        something = raw_input(">")

        if (something == "A"):

            self.life += 2
            print "Message from scene. Do something.5a"
            print self.life
            Level_six_a().run()

        elif (something == "AA"):

            self.life -= 2
            print "Message from scene. Do something.55a"
            print self.life
            Level_six_a().run()

        else:
            print "Do you know how to read? Open your eyes"
            exit(0)
            #Put loop here

##############

class Level_five_b(object):

    def five_b (self):

        print "Message from scene. Do something."
        something = raw_input(">")

        if (something == "B"):

            self.life += 2
            print "Message from scene. Do something.5b"
            print self.life
            Level_six_b().run()

        elif (something == "BB"):

            self.life -= 2
            print "Message from scene. Do something.55b"
            print self.life
            Level_six_b().run()

        else:
            print "Do you know how to read? Open your eyes"
            exit(0)
            #Put loop here

########################################################

class Level_six_a(object):
    
    def six_a (self):

        print "Message from scene. The end.6a"
        exit(0)

##############

class Level_six_b(object):
    
    def six_b (self):

        print "Message from scene. The end.6b"
        exit(0)

####################################################################################################

first_stage = Level_one()
first_stage.action_one()