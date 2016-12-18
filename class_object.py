from sys import exit


class Level_one(object):

    life = 10

    def action_one(self):

        print "You have a life level of 10."
        print "You need to pass through a maze. Where do you go? Left or Right?"
        direction = raw_input(">")

        if (direction == "left"):

            self.life += 2
            print "You just had 2 lives GIVEN to you"
            print self.life
            # exit(0)
            # A method is tied to an instance of a class so run below is a method and not a funciton
            Level_two_a().run()

        elif (direction == "right"):

            self.life -= 2
            print "You just had 2 lives TAKEN from you"
            print self.life
            # exit(0)
            Level_two_b().run()
            # will putint action_one() go back to the begining of the method?

        else:
            print "Do you know how to read? Open your eyes"
            exit(0)


class Level_two_a(object):

    def run(self):
        print "YOU CHOSE LEFT"
        exit(0)


class Level_two_b(object):
    # right
    def run(self):
        print "YOU CHOSE RIGHT"
        exit(0)


class Level_three_a(object):
    pass


class Level_three_a(object):
    pass


class Level_four(object):
    pass


player = Level_one()
player.action_one()
print "complete"
