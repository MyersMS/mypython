from sys import exit

##################

def start():

	print "You just arrived in Lagos Nigeria and asked to be dropped off" 
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
	print "This is the rough part of Lagos %s, and you definitly need to stay safe," 
	print "what do you pick for protection? juju, a gun or wisdom?" % name

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

			print "Have you ever used a gun before? You accidentally shoot yourself"
			print "because you don't know how to use one. You're eaten alive by fire ants"
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
	print "Pick it up, ignore it or kill the driver and steal the bus?"

	valid_input = False
	while not valid_input:

		print ""
######
		bus = raw_input(">")
######
		print ""

		if "pick it up" in bus:

			print "Bad idea to pick up items you don't own here."
			print "You turn into yam and you are used to make yam porridge"
			print "to feed your neighbours dog."
			exit(0)

		elif "ignore" in bus:

			print "You get kidnapped and because friends and family don't like you," 
			print "you get sold for $0 to a cannibal who slowly cuts you to pieces" 
			print "and eats you for breakfast every day."
			exit(0)

		elif "steal" in bus:

			print """to be continued"""
			exit(0) ####remove exit and define function from here

		else:

	 		print "Do you know how to read? Open your eyes %s" % name

		print ""

####################################################################### For the path to Ikoyi

def ikoyi():

	print "High expectation, high results %s. You are dropped off in"
	print "Ikoyi, good place to start off and lots of things to do." 
	print "What would you like to do? Tour town or go relax in ikoyi club?" % name

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

			print "You clearly are not a smart %r. Who buys water for N5,000?."
			print "You wouldn't last in Lagos." % name
			exit(0)

		else:

			print "Do you know how to read? Open your eyes %s" % name

		print ""

##################

def email():

	print "You definitly need the relaxation. While doing so, you decide to check"
	print "your email and a Prince in Nigeria notifies you that he needs money to"
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