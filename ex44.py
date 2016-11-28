print ""
print "1"
print ""

# Implicit Inheritance

class Manchester(object):
	def striker(self):
		print "We score the goals"

class Arsenal(Manchester):
	pass

rooney = Manchester()
giroud = Arsenal()

rooney.striker()
giroud.striker()

print ""
print "2"
print ""

# Override Explicitly 

class Manchester(object):
	def striker(self):
		print "We score the goals"

class Arsenal(Manchester):
	def striker(self):
		print "A lot of them"

rooney = Manchester()
giroud = Arsenal()

rooney.striker()
giroud.striker()

print ""
print "3"
print ""

# Alter before or after

class Manchester(object):
	def striker(self):
		print "We score the goals"

class Arsenal(Manchester):
	def striker(self):
		print "A lot of them"
		super(Arsenal, self).striker()
		print "GGGGGOOOOOAAAAALLLLLL"

rooney = Manchester()
giroud = Arsenal()

rooney.striker()
giroud.striker()
