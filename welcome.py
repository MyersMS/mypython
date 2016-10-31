print "\n \n Hi Momo. Welcome. Your presence is sincerely an honor"

print "\n I have a couple of questions I would like to ask you. Are you ready? yes or no"

answer = raw_input('>')



if answer == "yes":
	print "\n Great, I trust you are always ready. Very random but pronounce like a Nigerian, the word eba and what do you think it is derived from?"
	print "\n Cassava or Yam"

	from_what = raw_input('>')



	if from_what == "cassava":
		print "\n Great, suprised you got that"
	else:
		print "\n Not surprised but it's cassava, now you know and take note of that"

	print "\n Okay, how do you think you eat eba with okra soup?"
	print "\n With a fork, spoon or bare hands?"



	eaten_with_what = raw_input('>')

	if eaten_with_what == "bare hands":
		print "\n Wonderful, so eat like that in Argentina"
	else:
		print "\n Not surprised sir, we do not eat this wonderful delicacy with such equipments. We use our bare hands"

	print "\n Okay we're done with the random questions but I just got a slack from 6 about learning some stuff. Which should I explore first? unix or git"



	who = raw_input('?')

	if who == "unix":
		print "\n hmmmm, i'm curious to explore that"
	elif who == "dad":
		print "\n Well, you did introduce me to it but i never really got a hang of it"

	print "\n Well, that's all I have to put you through right now"
	print "\n Let's chat about the slack 6 sent me"


elif answer == "no":
	print "\n That's uncharacteristic of you. I doubt this is the momo I know"