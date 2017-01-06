# -*- coding: utf-8 -*-
# See https://stackoverflow.com/questions/10589620/syntaxerror-non-ascii-character-xa3-in-file-when-function-returns-%C2%A3 for details

from sys import exit
from random import randint

##################

#Need for sustainable agriculture

def need_for_sustainable_ag():

    print "The need for sustainable agriculture worldwide has become especially pressing given growing"
    print "concerns about agriculture's role in contributing to pollution and climate change."
    print "In addition, the world's population is projected to rise significantly by 2050"
    print "The world population will be ______ billion in 2050 (round to nearest whole number)."

    valid_input = False
    while not valid_input:

        print ""
######
        world_population = raw_input(">")
        ### world_population = float(world_population) --- WOULD NOT CONVERT STRING TO FLOAT IT RESPONSE GIVE ELSE

######
        print ""

        if "10" in world_population:
        ### if 9.5 < world_population and world_population <= 10

            print "10 billion is correct but to be precise, about 9.7"
            print "With this projected amount, there will be increasing pressure to intensify"
            print "agricultural production in many regions across the world given that most of the" 
            print "world’s arable land (land suitable for growing crops) is already being farmed"

            monoculture()
            valid_input = True
            ### return 1 #adding 1 to grade -- remove both about (nick6)


        elif world_population > 10 and world_population < 10:

            print "BZZZZZZZZZZZZZZ!!! wrong, 10 billion is the answer, but to be precise, about 9.7"
            print "With this projected amount, there will be increasing pressure to intensify"
            print "agricultural production in many regions across the world given that most of the" 
            print "world’s arable land (land suitable for growing crops) is already being farmed"

            monoculture()
            valid_input = True
            ### return 0 -- remove both about (nick6)
 #THIS DOES NOT WORK

        else:

            print "Population is in NUMBERS %s!!!. This isn't rocket science. Try again" %name
            ### need_for_sustainable_ag()


        print ""

##################

# Reliance on monoculture

def monoculture():

    print "A number of prominent scientists and others involved in the agricultural sector have expressed"
    print "doubts about the sustainability of current agricultural production systems, particularly in" 
    print "the face of climate change and continued population growth. One of the primary impediments to"
    print "developing more sustainable systems of agriculture is reliance on ____________."
    print ""
    print "*** one word answer ***"
    print ""
    print "A - Monoculture (planting of only one crop on a field)"
    print "B - Polyculture (planting of many crops on a field)"
    print "C - Silviculture (planting of trees on a field)"

    valid_input = False
    while not valid_input:

        print ""
######
        reliance_on = raw_input(">")
        ### reliance_on = reliance_on.lower() --- Since monoculture first letter is capital, allows for small letter input without providing error
######
        print ""

        if "monoculture" in reliance_on:

            print "Correct. Monoculture production has increased world-wide as the size of" 
            print "farms and incentives for commodity crop production have increased."

            staple_crops()
            valid_input = True
            ### return 1 -- remove both about (nick6)

        elif "polyculture" in reliance_on:

            print "No. This is good for sustainable agriculture. Try again."
            ### return 0

        elif "silviculture" in reliance_on:

            print "No. This is good for sustainable agriculture. Try again."
            ### return 0

        else:

            print "%s please open your eyes and read the question carefully." %name
            ### return 0 IS THIS NECESSARY

        print ""

##################

# Major staple crops

def staple_crops():

    print "In many countries around the world, crop production and consumption involve only a few major crop species."
    print "For example, 3 food grain crops are major staples in 97, 91 and 74 percent of countries around the world."
    print ""
    print "Pick 3 crops below you think are the major staples."
    print "Wheat, rice, oat and soybeans."

    valid_input = False
    while not valid_input:

        print ""
######
        grains = raw_input(">")
######
        print ""

        if "wheat" and "rice" and "soybean" and "soybeans" in grains:

            print "Correct, wheat, rice and soybeans are major staple crops in" 
            print "97, 91 and 74 percent of countries around the world respectively."
            print "This level of homogeneity in our agricultural food systems is due, in part, to" 
            print "pressures from political and economic forces and economies of scale."

            exit(0)
            #interseeding()
            valid_input = True
            ### return 1 

        elif "oat" and "oats" in grains:

            print "BZZZZZZZZZZZZZZ!!! One of the staples is wrong. Try again."
            ### return 0 -- remove both about (nick6) 
 #THIS DOES NOT WORK

        else:

            print "%s please open your eyes and read the question carefully." %name
            ### return 0 IS THIS NECESSARY

        print ""

##################

#Introduction

#def interseeding():

    #print "Continuous use of monoculture is associated with increased risk of crop disease,"
    #print "herbicide resistance, reductions in soil quality, and a variety of other"
    #print "agricultural and environmental problems. Hence, increasing interest in understanding"
    #print "crop diversity and the effects on sustainable agriculture."
    #print ""
    #print "My project examined several strategies for both managing the hayfield plant community prior"
    #print "to planting the crop mixture and the timing and approach to seeding the mixture."
    #print ""
    #print "The rational and hypotheses were formed based of 3 managemenst practices."
    #print "Interseeding"
    #print "Mowing"
    #print "Tillage"

    #valid_input = False
    #while not valid_input:

        #print ""
######
        #abc = raw_input(">")
######
        #print ""

        #if "abc" in abc:

            #print "abc"
            #print "abc"
            #exit(0)

        #elif "abc" in abc:

            #print "abc"
            #print "abc"
            #exit(0)

        #elif "abc" in abc:

            #abc()
            #valid_input = True

        #else:

            #print "abc"

        #print ""

##################

#Introduction

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################

#Introduction

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################

#Introduction

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################

#Introduction

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#########################################################################################

##################
#Rational and Hypothesis

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Rational and Hypothesis

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Rational and Hypothesis

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Rational and Hypothesis

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Rational and Hypothesis

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Rational and Hypothesis

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Rational and Hypothesis

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#########################################################################################

##################
#Materials and methods

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Materials and methods

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Materials and methods

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#########################################################################################

##################
#Results

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Results

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Results

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Results

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Results

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Results

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Results

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Results

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Results

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Results

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Results

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#########################################################################################

##################
#Conclusion

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Conclusion

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Conclusion

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Conclusion

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Conclusion

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Conclusion

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Conclusion

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################
#Conclusion

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

#########################################################################################
#########################################################################################

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = int(raw_input(">"))
######
        print ""

        if abc >= 0 and abc < 0:

            abc()
            valid_input = True

        elif abc >= 0 and abc < 0:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

##################

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""

        if "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

#################

def abc():

    print "abc"
    print "abc"

    valid_input = False
    while not valid_input:

        print ""
######
        abc = raw_input(">")
######
        print ""
        
        #code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        #guess = raw_input("[keypad]> ")
        #guesses = 0

        #while guess != code and guesses < 10:
            #print "BZZZZEDDD!"
            #guesses += 1
            #guess = raw_input("[keypad]> ")

        if "abc" in abc:
        #if guess == code:
            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            print "abc"
            print "abc"
            exit(0)

        elif "abc" in abc:

            abc()
            valid_input = True

        else:

            print "abc"

        print ""

###################

#Introduction


print "Welcome to my Master's thesis question and answer script."
print "My Thesis is called:" 
print "Effects Of Mowing And Soil Disturbance On The No-Till Establishment And Productivity Of A Diverse Forage Crop Cocktail In Hayfields."
print "My thesis in a sentence summary is about,"
print "exploring ways to enhance ecosystem services organically, using diverse forage crop cocktails in hayfields."
print "This might still sound confusing, so let's get started so you know more about my Thesis"
print "exploring ways to enhance ecosystem services organically, using diverse forage crop cocktails in hayfields."
print ""
print "First of all, what is your name?"

print ""
######
name = raw_input(">")
######
print ""

print "Great, let's get started %s." %name

print ""

grade = 0 #make starting grade 0
num_questions = 3 #number of questions - remember to update this when I add more questions
grade += need_for_sustainable_ag() 
grade += monoculture()
grade += staple_crops()

#mixing strings with numbers. use str function to convert number into string
print "Score: " + str(round(float(grade)/num_questions * 100, 2)) + '%'