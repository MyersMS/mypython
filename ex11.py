def person_stats():
	print "How old are you?",
	age = raw_input()
	print "How tall are you?",
	height = raw_input()
	print "How much do you weigh?",
	weight = raw_input()
	return age, height, weight

def print_person(a, h, w):
	print "So, you're %s old, %r tall and %r heavy" % (a, h, w)

person_age, height, weight = person_stats()
print_person(person_age, height, weight)