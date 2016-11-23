from sys import exit

class Level_one:

	life = 10

	def action_one(self):

		print "You have a life level of 10."
		print "You need to pass through a maze. Where do you go? Left or Right?"
		direction = raw_input(">")

		if (direction == "left"):

			self.life += 2
			print "You just had 2 lives GIVEN to you"
			print self.life
			#exit(0)
			#Level_two_a()

		elif (direction == "right"):

			self.life -= 2
			print "You just had 2 lives TAKEN from you"
			print self.life
			#exit(0)
			#Level_two_b()
			#will putint action_one() go back to the begining of the method?

		else:
			print "Do you know how to read? Open your eyes"
			exit(0)


player = Level_one()
player.action_one()

class Level_two_a:
	
	print "YOU CHOSE LEFT"
	exit(0)

class Level_two_b:
	#right
	print "YOU CHOSE RIGHT"
	exit(0)

class Level_three_a:
	pass

class Level_three_a:
	pass

class Level_four:
	pass

