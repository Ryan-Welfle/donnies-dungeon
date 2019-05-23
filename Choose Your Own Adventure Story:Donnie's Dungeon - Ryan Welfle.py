#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:43:51 2019
@author: ryanwelfle

Notes about this game...

This was created using Spyder 3.3.2, and thus would best be run via that environment

Total number of questions (not including first question that starts game): 48

Number of questions in "winning" pathway: 20
Pathway to take to win (not including first question that starts game):
    
A, B, yes, a, a, a, no, no, yes, b, b, a, b, b, a, b, b, b, b, a (or) b

Interesting pathways you can take to collect items, play a game or
two, and ultimately meet the wizard (other than the "winning" pathway):

Interesting Path #1 (only takes you up to meeting the wizard): 
10 questions (not including first question that starts game);

a, a, a, a, a, a, yes, a, a, yes

Interesting Path #2 (only takes you up to meeting the wizard): 
10 questions (not including first question that starts game);

b, yes*, a, b, b, b, b, b, a, yes
* = leads to a game that you must win in order to progress on this pathway

Interesting Path #3 (only takes you up to meeting the wizard): 
10 questions (not including first question that starts game);

c, a, b, a, b, b, a, no, b, no

"""

                        #@@@@@@@@@@
import random, sys      #importing "random" and "sys" modules; using random for "randint"; using sys for "sys.exit()"
health = 10             #@@@@@@@@@@
items=[]                #setting up variables that are used for completion of game; "items" is an empty list to be appended with items; "health" is to be changed with augmented operators
print(' ')
print("WELCOME TO DONNIE'S DUNGEON!")
print(' ')
print('To properly play:')
print('Make sure that you answer each question')
print('with "yes", "no", "A", "B", "C", or "go"')
print('as required by each question!')
print(' ')
print('Answering with a non-option will immediately')
print('terminate the game, and you will need to restart it!')                           #@@@@@@@@@@@@@
print(' ')                                                                              #.lower() puts all things in lower case
answer = input("WOULD YOU LIKE TO PLAY DONNIE'S DUNGEON? (yes/no) ").lower().strip()    #.strip() takes empty spaces out of the input
  
                        #@@@@@@@@@@@@@@@
def wizard():           #defining a function; this function serves as a mid-point where four story-lines converge
    print(' ')
    print('You approach the wizard, and he speaks ...')
    print('"Hello, my name is Donnie the Wizard!"')
    print('"Before I can let you leave, I need to see what items you have on you ..."')
    print('What do you do?')
    print(' ')
    print("(A) refuse to let him search you ...")
    print("(B) let him search you ... ")
    print(' ')                                                  #@@@@@@@@@@
    answer = input('Choose wisely! (A/B) ').lower().strip()     #creating the "answer" variable to hold user input to create the new story-path
    if answer == 'no':              #@@@@@@@@@@@@
        sys.exit()                  #using "sys.exit()" to terminate program if invalid entry is made, or "wrong" choice is made, or to end the game if you win
    if answer == 'yes':             
        sys.exit()                  
    if answer == 'b':               #@@@@@@@@@@@@@@@@@@@
        if 'fairy_wand' in items:   #using "in" to check list for a certain variable, where it's (lack of) presence progresses or ends the game
            print(' ')
            print('"You stole my fairy wand!", Donnie says ...')
            print('"You must be punished for this!"')
            print('He throws some magic dust as you ... and you disappear ...')
            print(' ')
            print('GAME OVER')
            sys.exit()                  #@@@@@@@@@@@@@@@@@@@
        if 'fairy_wand' not in items:   #using "not in" to check a list for a certain variable, to either progress or end the game
            print(' ')
            print('"Good, you have not stolen my fairy wand!", Donnie says ...')
            print('"Let me see how much damage you have taken ..."')
            print('What do you do?')
            print(' ')
            print("(A) let him check your damage ...")
            print("(B) tell him he can check for more items ... ")
            print(' ')
            answer = input('Choose wisely! (A/B) ').lower().strip()
            if answer == 'no':
                sys.exit()
            if answer == 'yes':
                sys.exit()                  #@@@@@@@@@@@@@@
            if answer == 'a':               #using "if statements" to branch the story into other narratives, using "equals to" comparison operator
                if health == 8:
                    print(' ')
                    print('"You have taken a respectful amount of damage", Donnie says ...')  #@@@@@@@@@@@@@@@
                    print('"Your health is at ' + str(health) + '/10 "')                        #concatenating strings, and displaying the "health" variable as a string with "str()"
                    print('"Do you know why that is a respectable amount?"')
                    print(' ')
                    print("(A) yes ...")
                    print("(B) no ... ")
                    print(' ')
                    answer = input('What is your answer? (A/B) ').lower().strip()
                    if answer == 'no':
                        sys.exit()
                    if answer == 'yes':
                        sys.exit()
                    if answer == 'b':
                        print(' ')
                        print('"I respect your honesty", Donnie says ...')
                        print('"By the way, do you have my dagger?"')
                        print(' ')
                        print("(A) yes ...")
                        print("(B) no ... ")
                        print(' ')
                        answer = input('What is your answer? (A/B) ').lower().strip()
                        if answer == 'no':
                            sys.exit()
                        if answer == 'yes':
                            sys.exit()
                        if answer == 'b':
                            print(' ')
                            print('"I respect your honesty", Donnie says ...')
                            if 'gemstone' in items:
                                print('"... and I see you have my gemstone!"')
                                print('"... may I have it back?"')
                                print(' ')
                                print("(A) yes ...")
                                print("(B) no ... ")
                                print(' ')
                                answer = input('What is your answer? (A/B) ').lower().strip()
                                if answer == 'no':
                                    sys.exit()
                                if answer == 'yes':
                                    sys.exit()
                                if answer == 'a':                   #@@@@@@@@@@@@@@@@@@@
                                    items.remove('gemstone')        #removing the "gemstone" variable from the "items" list-value variable with "items.remove()"
                                    print(' ')
                                    print('"Thank you!"')
                                    print('"Do you believe you are free to go now?"')
                                    print(' ')
                                    print("(A) yes ...")
                                    print("(B) no ... ")
                                    print(' ')
                                    answer = input('What is your answer? (A/B) ').lower().strip()
                                    if answer == 'no':
                                        sys.exit()
                                    if answer == 'yes':
                                        sys.exit()
                                    if answer == 'b':
                                        print(' ')
                                        print('"I respect your patience", Donnie says ...')
                                        if 'crystal' in items:
                                            print('"But you have not given me my crystal!", Donnie says ...')
                                            print('"You must be punished for this!"')
                                            print('He throws some magic dust at you ... and you disappear ...')
                                            print(' ')
                                            print('GAME OVER')
                                            sys.exit()              #@@@@@@@@@@@@@@@
                                        else:                       #using "else" statement to create an action if "crystal" variable is not in "items"
                                            print('"By the way, may I ask how many items you have?"')
                                            print(' ')
                                            print("(A) yes ...")
                                            print("(B) no ... ")
                                            print(' ')
                                            answer = input('What is your answer? (A/B) ').lower().strip()
                                            if answer == 'no':
                                                sys.exit()
                                            if answer == 'yes':
                                                sys.exit()
                                            if answer =='b':
                                                print(' ')
                                                print('"Smart answer! You already know I know the answer ..."') #@@@@@@@@@@@@@@@@
                                                print('"You have ' + str(len(items)) + ' items ..."')           #calculating the length of the "items" list with "len()", and displaying it as a string with "str()"
                                                print('"Do you believe this is the right amount to have?"')
                                                print(' ')
                                                print("(A) yes ...")
                                                print("(B) no ... ")
                                                print(' ')
                                                answer = input('What is your answer? (A/B) ').lower().strip()
                                                if answer == 'no':
                                                    sys.exit()
                                                if answer == 'yes':
                                                    sys.exit()
                                                if answer == 'b':
                                                    print(' ')
                                                    print('"We shall see"')                     #@@@@@@@@@@@@@@
                                                    if ('sword' and 'envelope') in items:       #using "and" Boolean operator to test if True that both "sword" and "envelope" variables are in "items" list
                                                        print('"But you have my sword and envelope!", Donnie says ...')
                                                        print('"You must be punished for this!"')
                                                        print('He throws some magic dust at you ... and you disappear ...')
                                                        print(' ')
                                                        print('GAME OVER')
                                                        sys.exit()
                                                    else:
                                                        print('"You do not have my sword or envelope ..."')
                                                        print('"Do you think you should have those things ...?"')
                                                        print(' ')
                                                        print("(A) yes ...")
                                                        print("(B) no ... ")
                                                        print(' ')
                                                        answer = input('What is your answer? (A/B) ').lower().strip()
                                                        if answer == 'no':
                                                            sys.exit()
                                                        if answer == 'yes':
                                                            sys.exit()
                                                        if answer == 'b':
                                                            print(' ')
                                                            print('"Correct you are ..."')
                                                            print('"Last question ... do you have all of the three items from the first question of the game ...?"')
                                                            print(' ')
                                                            print("(A) yes ...")
                                                            print("(B) no ... ")
                                                            print(' ')
                                                            answer = input('What is your answer? (A/B) ').lower().strip()
                                                            if answer == 'no':
                                                                sys.exit()
                                                            if answer == 'yes':
                                                                sys.exit()
                                                            if answer == 'b':
                                                                if ('hankerchief' and 'wood_block' and 'nail') in items:
                                                                    print(' ')
                                                                    print('"You actually DO have those things ..."') 
                                                                    print('"... you are free to go ...", Donnie says ...')
                                                                    print(' ')
                                                                    print('YOU WIN!')
                                                                    sys.exit()     
                                                                else:
                                                                    print(' ')
                                                                    print('"You are correct about that ...", Donnie says ...')
                                                                    print('"You must be punished for that!"')
                                                                    print('He throws some magic dust at you ... and you disappear ...')
                                                                    print(' ')
                                                                    print('GAME OVER')
                                                                    sys.exit()
                                                            if answer == 'a':
                                                                if ('hankerchief' and 'wood_block' and 'nail') in items:
                                                                    print(' ')
                                                                    print('"Excellent! You are free to go ...", Donnie says ...')
                                                                    print(' ')
                                                                    print('YOU WIN!')
                                                                    sys.exit()     
                                                                else:
                                                                    print(' ')
                                                                    print('"You do not!", Donnie says ...')
                                                                    print('"You must be punished for this!"')
                                                                    print('He throws some magic dust at you ... and you disappear ...')
                                                                    print(' ')
                                                                    print('GAME OVER')
                                                                    sys.exit()
                                                        if answer == 'a':
                                                            print(' ')
                                                            print('"You should not! Those are my personal things!", Donnie says ...')
                                                            print('"You must be punished for this!"')
                                                            print('He throws some magic dust at you ... and you disappear ...')
                                                            print(' ')
                                                            print('GAME OVER')
                                                            sys.exit()
                                                if answer == 'a':
                                                    print(' ')
                                                    print('"WRONG!", Donnie says ...')
                                                    print('"You must be punished for this!"')
                                                    print('He throws some magic dust at you ... and you disappear ...')
                                                    print(' ')
                                                    print('GAME OVER')
                                                    sys.exit()
                                            if answer == 'a':
                                                print(' ')
                                                print('"You underestimate me! You should know I already know the answer!", Donnie says ...')
                                                print('"You must be punished for this!"')
                                                print('He throws some magic dust at you ... and you disappear ...')
                                                print(' ')
                                                print('GAME OVER')
                                                sys.exit()    
                                    if answer == 'a':
                                        print(' ')
                                        print('"Not patient enough!", Donnie says ...')
                                        print('"You must be punished for this!"')
                                        print('He throws some magic dust at you ... and you disappear ...')
                                        print(' ')
                                        print('GAME OVER')
                                        sys.exit()
                                if answer == 'b':
                                    print('"This angers me ...", Donnie says ...')
                                    print('"You must be punished for this!"')
                                    print('He throws some magic dust at you ... and you disappear ...')
                                    print(' ')
                                    print('GAME OVER')
                                    sys.exit()
                            else:
                                print('"But you do not have my gemstone!", Donnie says ...')
                                print('"You must be punished for this!"')
                                print('He throws some magic dust at you ... and you disappear ...')
                                print(' ')
                                print('GAME OVER')
                                sys.exit()
                        if answer == 'a':
                            print(' ')
                            print('"You lie! I do not own a dagger!", Donnie says ...')
                            print('"You must be punished for this!"')
                            print('He throws some magic dust at you ... and you disappear ...')
                            print(' ')
                            print('GAME OVER')
                            sys.exit()
                    if answer == 'a':
                        print(' ')
                        print('"You lie! It is just an arbitrary number!", Donnie says ...')
                        print('"You must be punished for this!"')
                        print('He throws some magic dust at you ... and you disappear ...')
                        print(' ')
                        print('GAME OVER')
                        sys.exit()        
                else:
                    print(' ')
                    print('"You have taken a disrespectful amount of damage", Donnie says ...')
                    print('"Your health is at ' + str(health) + '/10 "')
                    print('"You must be punished for this!"')
                    print('He throws some magic dust at you ... and you disappear ...')
                    print(' ')
                    print('GAME OVER')
                    sys.exit()
            if answer == 'b':
                print(' ')
                print('"You disobey me?", Donnie says ...')
                print('"You must be punished for this!"')
                print('He throws some magic dust at you ... and you disappear ...')
                print(' ')
                print('GAME OVER')
                sys.exit()     
    if answer == 'a':
        print(' ')
        print('"Very well then ...", Donnie says ...')
        print('He throws some magic dust as you ... and you disappear ...')
        print(' ')
        print('GAME OVER')
        sys.exit()
                            #@@@@@@@@@@@@@@@@@@@@
if answer == "yes":         #the game actually starts right here!
    print(' ')
    print('You wake up in a cold, dark and ancient dungeon, locked in a cell.')
    print('On the stone floor, you can make our three objects...')
    print(' ')
    print('(A) a nail ...')
    print('(B) a block of wood ...')
    print('(C) a hankerchief ...')
    answer = input("Which one of those items do you choose to pick up? (A/B/C) ").lower().strip()
    if answer == 'a':                   #@@@@@@@@@@@@@@@@
        health -= 1                     #using augmented operator to subtract 1, from the global health variable created above; this variable comes into play later in the game
        items.append('nail')            #adding the variable/string "nail" to the "items" list/variable using "items.append()"
        print(' ')
        print('Ouch! You pricked yourself with the nail, and yelp with pain!')
        print(' ')
        print('Your health is now at ' + str(health) + '/10.')
        print(' ')
        print('You hear a loud and scary voice from outside the cell in response:')
        print("'Hey! Why don't you pipe down in there!'")
        print(' ')
        print('What do you do?')
        print(' ')
        print('(A) yell back, "make me!" ...')
        print('(B) feign being in pain ...')
        print('(C) continue to examine your cell ...')
        answer = input("Think fast! (A/B/C) ").lower().strip()
        if answer == 'c':
            print(' ')
            print('You turn away from the door to look on the ground for things ...')
            print('Unfortunately, the door gets kicked down the the person being the scary voice ...')
            print(' ... the dungeon-warden ...!')
            print('He plunges his sword right into you ...')
            print(' ')
            print('GAME OVER')
            sys.exit()
        if answer == 'b':
            print(' ')
            print('The person behind the voice turns out to be the dungeon-warden.')
            print("The dungeon-warden kicks down the door.")
            print('You are on the ground pretending to have a hurt knee.')
            print('The dungeon-warden raises his sword to slash at you')
            print(' ')
            answer = input('Do you move out of the way? (yes/no) ').lower().strip()
            if answer == 'a':
                sys.exit()
            if answer == 'yes':
                print(' ')
                print('You roll out of the way.')
                print('The dungeon-warden misses and gets his sword stuck in the ground.')
                print('What do you do?')
                print(' ')
                print('(A) kick him ...')
                print('(B) grab a shiny thing you see on the ground ...')
                print(' ')
                answer = input("Think fast! (A/B) ").lower().strip()
                if answer == 'no':
                    sys.exit()
                if answer == 'a':
                    print(' ')
                    print('You kick him hard, and he falls head-first into the ground - getting knocked out!')
                    print('Now what?')
                    print(' ')
                    print('(A) grab that hankerchief you saw before ...')
                    print('(B) get out of your cell before he wakes up ...')
                    print(' ')
                    answer = input("Choose wisely! (A/B) ").lower().strip()
                    if answer == 'no':
                        sys.exit()
                    if answer == 'b':
                        print(' ')
                        print('You leave the cell, post-haste!')
                        print('Unfortunately, another dungeon-warden is around the corner!')
                        print('He plunges his sword right into you ...')
                        print(' ')
                        print('GAME OVER')
                        sys.exit()
                    if answer == 'a':
                        items.append('hankerchief')
                        items.append('gemstone')
                        print(' ')
                        print('You pick up the hankerchief ...')
                        print('You find a gemstone!')
                        print('Now what?')
                        print(' ')
                        print('(A) pick up the block of wood in the ground ...')
                        print('(B) wait for the dungeon-warden to wake up ...')
                        print(' ')
                        answer = input("Choose wisely! (A/B) ").lower().strip()
                        if answer == 'no':
                            sys.exit()
                        if answer == 'a':
                            health -= 1
                            items.append('wood_block')
                            print(' ')
                            print('You pick up the block of wood ...')
                            print('Ouch! It gives you a splinter!')
                            print('Your health is now at ' + str(health) + '/10.')
                            print('You see a button underneath ...')
                            print(' ')
                            answer = input('Do you press it? (yes/no) ').lower().strip()
                            if answer == 'a':
                                sys.exit()
                            if answer == 'b':
                                sys.exit()
                            if answer == 'no':
                                print(' ')
                                print('You forget about the button, for the time being ...')
                                print("You see the dungeon-warden's sword lying on the ground beside him ...")
                                print(' ')
                                answer = input('Do you pick it up? (yes/no) ').lower().strip()
                                if answer == 'a':
                                    sys.exit()
                                if answer == 'b':
                                    sys.exit()
                                if answer == 'no':
                                    print(' ')
                                    print('The guard is still out cold ...')
                                    print(' ')
                                    answer = input('Do you leave your cell? (yes/no) ').lower().strip()
                                    if answer == 'a':
                                        sys.exit()
                                    if answer == 'b':
                                        sys.exit()
                                    if answer == 'yes':
                                        print(' ')
                                        print('You exit the cell ...')
                                        print("It's very dark in the hallways, but you make out two things ...")
                                        print('(A) to your left is a glowing orb ...')
                                        print('(B) to your right is some entity that looks like a wizard ...')
                                        print(' ')
                                        answer = input('What do you go towards? (A/B) ').lower().strip()
                                        if answer == 'yes':
                                            sys.exit()
                                        if answer == 'no':
                                            sys.exit()
                                        if answer == 'b':
                                            wizard()
                                        if answer == 'a':
                                            print(' ')
                                            print('You slowly make your way towards the orb ...')
                                            print("When you get in front of it, you touch it ...")
                                            print('... unfortunately, it electrocutes you beyond belief ...')
                                            print(' ')
                                            print('GAME OVER')
                                            sys.exit()
                                    if answer == 'no':
                                        print(' ')
                                        print('You wait for the guard to wake up, for some reason ... ')
                                        print("He eventually, he wakes up and plunges his sword into you ...")
                                        print(' ')
                                        print('GAME OVER')
                                        sys.exit()
                                if answer == 'yes':
                                    print(' ')
                                    print('You pick up the sword ...')
                                    print("But unfortunately, something literally shocked happens!")
                                    print('The sword is somehow electrified, and it electrocutes you ...')
                                    print(' ')
                                    print('GAME OVER')
                                    sys.exit()
                            if answer == 'yes':
                                print(' ')
                                print('You try and press the button.')
                                print("Unfortunately, it seems to be jammed!")
                                print('The dungeon-warden wakes up, and is furious!')
                                print('He plunges his sword right into you ...')
                                print(' ')
                                print('GAME OVER')
                                sys.exit()
                        if answer == 'b':
                            print(' ')
                            print('You wait about an hour for him to wake.')
                            print("Unfortunately, when he wakes up he's furious!")
                            print('He plunges his sword right into you ...')
                            print(' ')
                            print('GAME OVER')
                            sys.exit()
                if answer == 'b':
                    print(' ')
                    print('You reach for the shiny thing.')
                    print('However, the dungeon-warden already got his sword unstuck!')
                    print('He plunges his sword right into you ...')
                    print(' ')
                    print('GAME OVER')
                    sys.exit()
            if answer == 'no':
                print(' ')
                print('As expected, the sword plunges right through you ...')
                print('GAME OVER')
                sys.exit()
        if answer == 'a':
            print(' ')
            print('"MAKE ME!", you scream back to the voice.')
            print('The loud sound of increasingly fast feet boom throughout the dungeon.')
            print('"ALRIGHT! YOU ASKED FOR IT!", the scary voice screamed back.')
            print(' ')
            print('What do you do?')
            print('(A) try to apologize ...')
            print('(B) try to unlock the cell door with the nail ...')
            answer = input("Think fast! (A/B) ").lower().strip()
            if answer == 'b':
                print(' ')
                print('You try to use the nail to unlock the door  ...')
                print('However, it is no use ...')
                print('The cell door swings open ... and knocks you clean out ...')
                print('GAME OVER')
                sys.exit()
            if answer == 'a':
                print(' ')
                print('You yell "Sorry!" to the angry presence, yet the footsteps quicken in pace.')
                print('Suddenly the cell door flies open, hitting you and knocking you to the ground')
                print('The giant dungeon-warden stands before you: "TO THE GUILLOTINE WITH YOU!", he yells.')
                print('What do you do now?')
                print(' ')
                print('(A) use the nail ...')
                print('(B) grab something else from the ground ...')
                print(' ')
                answer = input('Choose wisely! (A/B) ').lower().strip()
                if answer == 'b':
                    print(' ')
                    print('You try to pick something else up quickly ...')
                    print('However, it is no use ...')
                    print('The dungeon-warden drags you to the guillotine ...')
                    print('GAME OVER')
                    sys.exit()
                if answer == 'a':
                    print(' ')
                    print("You poke the dungeon-warden's finger with the nail.")
                    print("Surprisingly, he falls to the ground - now you can escape!")
                    print("You exit the cell, which way do you go?")
                    print(' ')
                    print('(A) left ...')
                    print('(B) right ...')
                    print(' ')
                    answer = input('Choose wisely! (A/B) ').lower().strip()
                    if answer == 'b':
                        print(' ')
                        print('You turn right and step a secret button on the floor ...')
                        print('The floor opens from under your feet ...')
                        print('You immediately fall into the pit ... to never return ...')
                        print('GAME OVER')
                        sys.exit()
                    if answer == 'a':
                        print(' ')
                        print("It's pretty dark down this hall, so your vision alone cannot get you through.")
                        print("How do you choose to navigate this hallway?")
                        print(' ')
                        print('(A) crawl on the ground ...')
                        print('(B) feel your way through along the walls ...')
                        print(' ')
                        answer = input('Choose wisely! (A/B) ').lower().strip()
                        if answer == 'b':
                            print(' ')
                            print('You start moving along the walls for guidance ...')
                            print('Unfortunately, another dungeon-warden walks by and sees you ...')
                            print('He promptly plunges his sword into you ...')
                            print('GAME OVER')
                            sys.exit()
                        if answer == 'a':
                            print(' ')
                            print("You crawl down the hallway on your hands and knees.")
                            print("You feel something on the ground under your hand")
                            print(' ')
                            answer = input('Do you pick it up? (yes/no) ').lower().strip()
                            if answer == 'no':
                                print(' ')
                                print('You ignore the object ..')
                                print('Unfortunately, another dungeon-warden walking by steps on you and sees you ...')
                                print('He promptly plunges his sword into you ...')
                                print('GAME OVER')
                                sys.exit()
                            if answer == 'yes':
                                items.append('crystal')
                                print(' ')
                                print("It was a crystal! You put it in your pocket.")
                                print("You turn a corner, and see a soft light at the end of another hallway ...")
                                print('What do you do?')
                                print(' ')
                                print('(A) go towards it, obviously ...')
                                print('(B) go far away from it ...')
                                print(' ')
                                answer = input('Choose wisely! (A/B) ').lower().strip()
                                if answer == 'b':
                                    print(' ')
                                    print('You start running away from the light ...')
                                    print('Unfortunately, you bump into another dungeon-warden ...')
                                    print('He promptly plunges his sword into you ...')
                                    print('GAME OVER')
                                    sys.exit()
                                if answer == 'a':
                                    health -= 2
                                    print(' ')
                                    print("You crawl furiously towards to light ...")
                                    print("Once you get within a meter of it spontaneously explodes!")
                                    print('You get injured, and your health is now at ' + str(health) + '/10.')
                                    print('Now what do you do?')
                                    print(' ')
                                    print('(A) continue to escape the dungeon ...')
                                    print('(B) lie down for a bit to recuperate ...')
                                    print(' ')
                                    answer = input('Choose wisely! (A/B) ').lower().strip()
                                    if answer == 'b':
                                        print(' ')
                                        print('You sit down ...')
                                        print('Unfortunately, you sit on a secret button protruding from the floor')
                                        print('The floor opens up beneath you ... you fall and never return ...')
                                        print('GAME OVER')
                                        sys.exit()
                                    if answer == 'a':
                                        print(' ')
                                        print('You continue on with a stronger will than ever.')
                                        print('The hallways begin to get progressively more dark.')
                                        print('A see another person about 20 yard away, that looks like ... a wizard ...')
                                        print(' ')
                                        answer = input('Do you approach the wizard? (yes/no) ').lower().strip()
                                        if answer == 'yes':     #@@@@@@@@@@@@@@@@@@@@@
                                            wizard()            #calling the wizard() function, which defines the second half of the story, which only four particular story-lines get to
    elif answer == 'b':
        items.append('wood_block')
        print(' ')
        print('You pick up the block of wood, which uncovers what looks like a button on the floor ...')
        answer = input('Do you press it? (yes/no) ').lower().strip()
        if answer == 'no':
            print(' ')
            print('You leave the button be ...')
            print('Just then, the door gets kicked down by a tall, burly, heavily armoured man!')
            print("Oh no! That's the dungeon-warden!")
            print('"EXECUTION DAY!", he screams - as he plunges his sword into you ...')
            print(' ')
            print('GAME OVER')
            sys.exit()
        if answer == 'yes':
            print(' ')
            print('Upon pressing the button, the floor opens up from underneath you!')
            print('You start to fall into a dark pit at great speed, grabbing at the walls of the pit to slow you fall.')
            chances = 3
            print('You have ' + str(chances) + ' chances to cling to the walls.')
            answer = input('Type "go" to try and grab the walls: ').lower().strip()
            if answer != 'go':
                    print(' ')
                    print('You could not grab a hold, and so you fall forever ...')
                    print('GAME OVER')
                    sys.exit()                              #@@@@@@@@@@@@@@@@@@@
            while (answer == 'go') and (chances != 0):      #creating a short game with a "while loop" triggered by the user input "go", and the variable "chances" not being equal to "0"
                walls = (random.randint(1,3))               #using "random.randint()" to assign the variable "walls" with a random integer between 1-3
                if chances == 1:
                    print(' ')
                    print('You could not grab a hold, and so you fall forever ...')
                    print('GAME OVER')
                    sys.exit()
                elif walls == 1:            #@@@@@@@@@@@@@
                    break                   #using "break" to get of the "while loop" if the "walls" variable is equal to 1
                elif walls != 1:            #using "elif statement" as another flow control statement to decide what happens in the "while loop"
                    chances -= 1
                    health -= 1
                    print(' ')
                    print("You couldn't get a hold!")
                    print('Your health is now at ' + str(health) + '/10.')
                    print('You have ' + str(chances) + ' chances to cling to the walls.')
                    answer = input('Type "go" to try and grab the walls: ').lower().strip #@@@@@@@@@@@
                    continue                                                              #using "continue" the restart the "while loop" at its beginning
                else:
                    print(' ')
                    print('You could not grab a hold, and so you fall forever ...')
                    print('GAME OVER')
                    sys.exit()
            while answer != 'go':
                print(' ')
                print('You could not grab a hold, and so you fall forever ...')
                print('GAME OVER')
                sys.exit()
            print(' ')
            print('You grabbed a hold!')
            print('You hang in the dark pit for a short while ...')
            print('Suddenly, a little fairy flies towards you ...')
            print('What do you do?')
            print(' ')
            print('(A) ask the fairy for help ...')
            print('(B) tell the fairy to go away ...')
            print(' ')
            answer = input('Choose wisely! (A/B) ').lower().strip()
            if answer == 'a':
                print(' ')
                print('The fairy smiles ...')
                print('The fairy says they can help you, but you must answer three questions correctly!')
                print('They ask you: "what is my favourite colour?')
                print(' ')
                print('(A) blue ...')
                print('(B) red ...')
                print(' ')
                answer = input('Choose wisely! (A/B) ').lower().strip()
                if answer == 'b':
                    print(' ')
                    print('"CORRECT", the fairy says ...')
                    print('They then ask you: "what is my favourite season?')
                    print(' ')
                    print('(A) autumn ...')
                    print('(B) spring ...')
                    print(' ')
                    answer = input('Choose wisely! (A/B) ').lower().strip()
                    if answer == 'b':
                        print(' ')
                        print('"CORRECT", the fairy says ...')
                        print('They then ask you their last question:') 
                        print('"... what is my name?"')
                        print(' ')
                        print('(A) how could I possibly guess that ...')
                        print('(B) Fairy McFairykins ...')
                        print(' ')
                        answer = input('Choose wisely! (A/B) ').lower().strip()
                        if answer == 'b':
                            items.append('fairy_wand')
                            print(' ')
                            print('"WOW - HOW DID YOU KNOW?!", the fairy says.')
                            print('As a prize, you get my fairy wand!')
                            print('The fairy puts the wand in your pocket, and flies away ...')
                            print("You're still stuck though ... what do you do?")
                            print(' ')
                            print('(A) see if the wand can help you ...')
                            print('(B) try to call the fairy back ...')
                            print(' ')
                            answer = input('Choose wisely! (A/B) ').lower().strip()
                            if answer == 'b':
                                print(' ')
                                print('You yell at the fairy to come back ...')
                                print('The fairy turns around angrily ...') 
                                print('"I GIVE YOU MY WAND, AND THEN YOU YELL AT ME?!", the fairy says.')
                                print('"WHY SHOULD I HELP YOU AGAIN?!"')
                                print(' ')
                                print('(A) because you said that you would (?) ...')
                                print('(B) uhhh ...')
                                print(' ')
                                answer = input('Choose wisely! (A/B) ').lower().strip()
                                if answer == 'b':
                                    print(' ')
                                    print('The fairy then remembers something ...')
                                    print('"OH RIGHT, I SAID I WOULD HELP YOU", the fairy says.')
                                    print('They snap their fingers, and you find youself in a dark hallway')
                                    print('Now what?')
                                    print(' ')
                                    print('(A) run in a random direction ...')
                                    print('(B) try to call for the fairy again ...')
                                    print(' ')
                                    answer = input('Choose wisely! (A/B) ').lower().strip()
                                    if answer == 'a':
                                        health -= 2
                                        print(' ')
                                        print('You run in a random direction, and bump your head into a wall.')
                                        print('Your health is now at ' + str(health) + '/10.')
                                        print('In your dizziness, you see a figure in the distance that looks like a wizard ...')
                                        print(' ')
                                        answer = input('Do you approach the wizard? (yes/no) ').lower().strip()
                                        if answer == 'yes':
                                            wizard()
                                        if answer == 'no':
                                            print(' ')
                                            print('You take a few steps back from the wizard ...')
                                            print("Just then, you bump into something hard ... it's the dungeon-warden!")
                                            print('He plunges his sword into you')
                                            print("It's the dungeon-warden! He pulls out his sword and plunges it into you ...")
                                            print(' ')
                                            print('GAME OVER')
                                            sys.exit()
                                    if answer == 'b':
                                        print(' ')
                                        print('You call for the fairy ...')
                                        print('Just then, you hear running footsteps coming in your direction!')
                                        print('"THE PRISONER IS TRYING TO ESCAPE!"')
                                        print("It's the dungeon-warden! He pulls out his sword and plunges it into you ...")
                                        print(' ')
                                        print('GAME OVER')
                                        sys.exit()
                                if answer == 'a':
                                    print(' ')
                                    print('"BEING SMART WITH ME, EH?!", the fairy yells ...')
                                    print('The fairy take their wand back, waves it, and you spontaneously combust!')
                                    print(' ')
                                    print('GAME OVER')
                                    sys.exit()
                                    
                            if answer == 'a':
                                print(' ')
                                print('You wave the wand around ...')
                                print('The wand glows, and unfortunately you spontaneously combust!')
                                print(' ')
                                print('GAME OVER')
                                sys.exit()
                        if answer == 'a':
                            print(' ')
                            print('"NOT EVEN A GUESS?! YOU LOSE!", the fairy yells ...')
                            print('The fairy waves its wand at you, and you spontaneously combust!')
                            print(' ')
                            print('GAME OVER')
                            sys.exit()
                    if answer == 'a':
                        print(' ')
                        print('"WRONG", the fairy yells ...')
                        print('The fairy waves its wand at you, and you spontaneously combust!')
                        print(' ')
                        print('GAME OVER')
                        sys.exit()
                if answer == 'a':
                    print(' ')
                    print('"WRONG", the fairy yells ...')
                    print('The fairy waves its wand at you, and you spontaneously combust!')
                    print(' ')
                    print('GAME OVER')
                    sys.exit()
            if answer == 'b':
                print(' ')
                print('The fairy gets very upset by this ...')
                print('The fairy waves its wand at you, and you spontaneously combust!')
                print(' ')
                print('GAME OVER')
                sys.exit()
    elif answer == 'c':
        print(' ')
        print('You pick up the musty hankerchief, and you find that underneath \
              is a blue gemstone!')
        items.append('gemstone')
        items.append('hankerchief')
        print(' ')
        print('All of a sudden, you hear echoing footsteps heading towards your cell. \
              What do you do?')
        print(' ')
        print('(A) hide in a dark corner of the cell ...')
        print('(B) stay right where you are ...')
        print(' ')
        answer = input("You don't have much time! (A/B) ").lower().strip()
        if answer == 'a':
            print(' ')
            print('You hide in the darkest corner of the cell.')
            print("The cell door swings open! It's the dungeon-warden!")
            print('What do you do?')
            print(' ')
            print('(A) throw the gemstone at him ...')
            print('(B) throw the hankerchief at him ...')
            print(' ')
            answer = input("Choose wisely! (A/B) ").lower().strip()
            if answer == 'b':
                print(' ')
                print('You throw the hankerchief as hard as you can.')
                print("Surprisingly, it lands flat on his face ... covering his eyes!")
                print('He starts thrashing about in disarray ...')
                print('What do you do?')
                print(' ')
                print('(A) try and get his sword ...')
                print('(B) try and sneak past him ...')
                print(' ')
                answer = input("Choose wisely! (A/B) ").lower().strip()
                if answer == 'a':
                    items.append('sword')
                    print(' ')
                    print('You carefully approach the dungeon-warden ...')
                    print("To your own disbelief, you grab it right from his hands with no problem!")
                    print('The hankerchief falls from his face ...')
                    print('What do you do?')
                    print(' ')
                    print('(A) try and slash him with the sword ...')
                    print('(B) try and pick up the hankerchief ...')
                    print(' ')
                    answer = input("Choose wisely! (A/B) ").lower().strip()
                    if answer == 'b':
                        print(' ')
                        print('Just ask you go to pick-up the hankerchief, the dungeon-warden swings at you ...')
                        print("He missed you as you grab the hankerchief, and he loses his balance!")
                        print('He falls down, and hits his head hard on the ground - enough to knock him out ...')
                        print('What do you do now?')
                        print(' ')
                        print('(A) leave the cell, obviously ...')
                        print('(B) see what the dungeon-warden has in his pockets ...')
                        print(' ')
                        answer = input("Choose wisely! (A/B) ").lower().strip()
                        if answer == 'b':
                            print(' ')
                            print('You reach into his pockets and find two interesting items ...')
                            print(' ')
                            print('(A) an envelope ...')
                            print('(B) a box of matches ...')
                            print(' ')
                            answer = input("Which one do you choose? (A/B) ").lower().strip()
                            if answer == 'a':
                                print(' ')
                                print('Huh ... there seems to be something inside ...')
                                print(' ')
                                answer = input("Do you open it? (yes/no) ").lower().strip()
                                if answer == 'a':
                                    sys.exit()
                                if answer == 'b':
                                    sys.exit()
                                if answer == 'no':
                                    items.append('envelope')
                                    print(' ')
                                    print('You decide to keep the envelope on your person, and open it later ...')
                                    print('Outside the cell you are faced with a dark hallway ...')
                                    print(' ')
                                    print('(A) to the left is a faint light ...')
                                    print('(B) to the right is a mysterious figure ...')
                                    print(' ')
                                    answer = input("Which way do you go? (A/B) ").lower().strip()
                                    if answer == 'yes':
                                        sys.exit()
                                    if answer == 'no':
                                        sys.exit()
                                    if answer == 'b':
                                        print(' ')
                                        print('You walk cautiously towards figure, that sort of looks like a wizard ...')
                                        print('Just then you trip and fall over something ...')
                                        print(' ')
                                        answer = input("Do you investigate to see what you tripped over? (yes/no) ").lower().strip()
                                        if answer == 'a':
                                            sys.exit()
                                        if answer == 'b':
                                            sys.exit()
                                        if answer == 'no':
                                            wizard()
                                        if answer == 'yes':
                                            print(' ')
                                            print("It feels like a button protruding from the ground ...")
                                            print('You press the button, to which it opens up the floor from underneath you!')
                                            print('You fall immediately ... never to return ...')
                                            print(' ')
                                            print('GAME OVER')
                                            sys.exit()
                                    if answer == 'a':
                                        print(' ')
                                        print("You walk towards the faint light, and it grows in brightness ...")
                                        print('As you get right up to it ... it explodes in your face ...')
                                        print(' ')
                                        print('GAME OVER')
                                        sys.exit()
                                if answer == 'yes':
                                    print(' ')
                                    print("You rip open the envelope ...")
                                    print('A poisonous gas fills the air ... you immediately lose consciousness')
                                    print(' ')
                                    print('GAME OVER')
                                    sys.exit()
                            if answer == 'b':
                                print(' ')
                                print("You grab the box of matches, and slide it open ...")
                                print('For some truly unfortunate reason it explodes right in your face ...')
                                print(' ')
                                print('GAME OVER')
                                sys.exit()
                        if answer == 'a':
                            print(' ')
                            print("You run with glee out of your cell.")
                            print('Unfortunately, you trip and fall - and the sword plunges right into you ...')
                            print(' ')
                            print('GAME OVER')
                            sys.exit()
                    if answer == 'a':
                        print(' ')
                        print('You swing the sword at him, and it completely shatters ...')
                        print('The dungeon-warden elbows you right in the head, knocking you right out ...')
                        print(' ')
                        print('GAME OVER')
                        sys.exit()
                if answer == 'b':
                    print(' ')
                    print('You do your best to stealthily sneak by him ...')
                    print('Unfortunately, in his thrashing about he plunges his sword directly into you ...')
                    print(' ')
                    print('GAME OVER')
                    sys.exit()
            if answer == 'a':
                print(' ')
                print("You throw the gemstone at his head ...")
                print('This gives away your hiding place! He throws his sword at you!')
                print('The sword plunges right into you ...')
                print(' ')
                print('GAME OVER')
                sys.exit()
            if answer == 'b':
                print(' ')
                print("The cell door kicks down! It's the dungeon-warden!")
                print('"EXECUTION DAY!", he yells')
                print('He then promptly plunges his sword into you ...')
                print(' ')
                print('GAME OVER')
                sys.exit()
else:
    print('Maybe another time!')