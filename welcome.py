print "\n \n Hi Hannah. Welcome to my place once again. Your presence is sincerely an honor"

print "\n I have a couple of questions I would like to ask you. This is in preparation of some Nigerian culture you are about to learn. Are you ready? yes or no"

answer = raw_input('>')



if answer == "yes":
	print "\n Great, I trust you are always ready Madam Hannah. Pronounce like a Nigerian the word eba and what do you think it is derived from?"
	print "\n Cassava or Yam"

	from_what = raw_input('>')



	if from_what == "cassava":
		print "\n Great, sounds like someone was listening last time"
	else:
		print "\n Damn, that hurts. I thought you were listening, it's cassava."

	print "\n Okay, how do you think you eat eba with okra soup?"
	print "\n With a fork, spoon or bare hands?"



	eaten_with_what = raw_input('>')

	if eaten_with_what == "bare hands":
		print "\n Wonderful, so get ready to eat like a Nigerian queen"
	else:
		print "\n No my dear, we do not eat this wonderful delicacy with such equipments. We use our bare hands"

	print "\n Annnnd btw, I love the smile on your face right now. You look God damn pretty when you smile like that. Who do you look like, mom or dad?"



	who = raw_input('?')

	if who == "mom":
		print "\n You're lucky you got them from mama, people would kill to have the beauty you possess"
	elif who == "dad":
		print "\n Damnnnn you dad must be a model or something. Lucky you"

	print "\n Well, that's all I have to put you through right now"
	print "\n My goals for after your meal are: talk about your blog, tell you more about my culture and convince you to hang with me tomorrow"


elif answer == "no":
	print "\n That's uncharacteristic of you. I doubt this is the Hannah Brantley I know"