from sys import exit

############################

print "What is your name?"
print ""
name = raw_input(">")
print ""
print "So let's play this scenario out %r." % name
print ""
print """You just arrived in Lagos Nigeria and were asked to be dropped off 
         based on a number you choose between 0 to 10, which do you pick?"""
print ""

############################

# This is where the location is chosed based off the number you pick
drop_off = raw_input(">") ### either raw input or int(function)

print ""

####################################################################### For the path to Ajegunle
if drop_off == (0,5):

	print """Low expectation, low results. You are dropped off in Ajegunle
	         This is the rough part of Lagos %r, and you definitly need to stay
	         safe, what do you pick for protection? juju, a gun or wisdom?""" % name

print ""

############################

protection = raw_input(">")

print ""

if "juju" in protection:

	print """Very smart idea to pick something you don't know how to use. You light yourself
	       on fire and burn to ashes"""
exit(0)

elif "gun" in protection:

	print """Have you ever used a gun before? You accidentally shoot yourself because 
		       you don't know how to use one. You're eaten alive by fire ants"""
exit(0)

elif "wisdom" in protection:

	print """Good choice, you would need to be street smart to survive around here.
			         Let's see how you use this wisdom."""

else:
		#loop

	print """ So you get stuck at 2am in a very sketchy place and you have no money.
		       The only was back is a bus that would cost N500, it's your lucky day and 
		       you see a N500 note crumbled below you. What do you do? Pick it up, ignore it
		       or kill the driver and steal the bus? """

print ""

############################

bus = raw_input(">")

print ""

if "pick it up" in bus:

print """Bad idea to pick up items you don't own here. You turn into yam and you are used
		to make yam porridge for your neighbours dog"""
exit(0)

elif "ignore" in bus:

print """ You get kidnapped and because friends and family don't like you, you get sold for
	        $0 to a canibal who slowly cuts you to pieces and eats you for breakfast every day"""
exit(0)

elif "steal" in bus:

print """ to be continued """

else:
	 	#loop

####################################################################### For the path to Ikoyi

elif drop_off >= 5 or <= 10:

print """High expectation, high results. You are dropped off in Ikoyi, good place
			to start off and lots of things to do""" % name

print """ What would you like to do? tour town or go relax in ikoyi club? """

to_do = raw_input(">")

print ""

if "tour" in to_do:

print """ During the tour, you are thirsty and want to buy a drink from a street hawker.
			 You ask for water and he says it cost N3,000. What do you do? drive off or buy it?"""

hawker == raw_input(">")

if "drive off" in hawker:

print """ You die of thirst"""
exit(0)

elif "buy it" in hawker:

print """ You clearly are not a smart %r. Who buys water for N3,000?. You wouldnt last
	      in Lagos """ % name
exit(0)

else:
		#loop

print ""

############################

elif "relax" in to_do:

print """You definitly need the relaxation. While doing so, you decide to check your email
	    and a Prince in Nigeria notifies you that he needs money to cover the cost of his
	    mother's funeral. What do you do? send money or ignore"""

email = raw_input(">")

if "money" in email:
	
print """You get scammed. You're obviously broke and lose your life savings, $6,432.51
		to him"""
exit(0)

elif "ignore" in email:

print """ You're heartless. Society doesn't need people like you."""
exit(0)

else:
	#loop

print ""




















