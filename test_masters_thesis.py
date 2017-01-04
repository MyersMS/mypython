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
        world_population = raw_input(">") # I want to put int here so if its the wrong intiger -> elif, anything other than integer, else.
######
        print ""

        if "10" in world_population:

            print "10 billion is correct but to be precise, about 9.7"
            print "With this projected amount, there will be increasing pressure to intensify"
            print "agricultural production in many regions across the world given that most of the" 
            print "world’s arable land (land suitable for growing crops) is already being farmed"

            monoculture()
            valid_input = True

        elif world_population > 10 and world_population < 10: # An integer thats not 10

            print "BZZZZZZZZZZZZZZ!!! wrong, 10 billion is the answer, but to be precise, about 9.7"
            print "With this projected amount, there will be increasing pressure to intensify"
            print "agricultural production in many regions across the world given that most of the" 
            print "world’s arable land (land suitable for growing crops) is already being farmed"

            monoculture()
            valid_input = True

        else: # Anything other than integer

            print "Population is in NUMBERS %s!!!. This isn't rocket science. Try again" %name

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
######
        print ""

        if "monoculture" in reliance_on:

            print "Correct. Monoculture production has increased world-wide as the size of" 
            print "farms and incentives for commodity crop production have increased."

            staple_crops()
            valid_input = True

        elif "polyculture" in reliance_on:

            print "No. This is good for sustainable agriculture. Try again."

        elif "silviculture" in reliance_on:

            print "No. This is good for sustainable agriculture. Try again."

        else:

            print "%s please open your eyes and read the question carefully." %name

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
            valid_input = True

        elif "oat" and "oats" in grains:

            print "BZZZZZZZZZZZZZZ!!! One of the staples is wrong. Try again." 

        else:

            print "%s please open your eyes and read the question carefully." %name

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

#********************************************************************************************************
#This is where we start

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
need_for_sustainable_ag() 
