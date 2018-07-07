from sys import exit
def gold_room():

    print "This roomis full of goal. How much do you take?"

    next=raw_input("> ")
    
    try:
        how_much=int(next)
    except ValueError:
        dead("Man, learn to type number.")
        exit(0)

    if how_much<50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def dead(why):
    print why,"Good job!"
    exit(0)

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "the fat vear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved=False

    while True:
        next=raw_input("> ")
        if next=="take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next=="taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved=True
        elif next=="taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg.")
        elif next=="open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."







bear_room()
