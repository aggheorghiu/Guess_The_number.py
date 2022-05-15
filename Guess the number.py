import simplegui
import random
import math


# helper function to start and restart the game
def new_game():
    global secret_number
    secret_number = random.randrange(0,1000)
    secret_number = random.randrange(0,100)
    
    global num_range    
    num_range = random.randrange(0,100)

    global count
    if range100:
        count=7
    else:
        count=10
    print "New Game" 
    
        
                   

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    print
    new_game()
    global num_range    
    num_range = random.randrange(0,100)
    print "range is now 0-99"       
    
    global count
    count = 7
        

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print
    new_game()
    global num_range
    num_range = random.randrange(0,1000)
    print "range is now 0-999"  
    
    global count
    count = 10
        
    
    
def input_guess(guess):
    # main game logic goes here	
    pGuess = int(guess)
    print "Guess was ", pGuess
    
    global count
    if pGuess<num_range:
        count -= 1               
        print "Remaining guesses: " + str((count))
        print "HIGHER"
        print "Keep trying"
        print
    elif pGuess>num_range:
        count -= 1       
        print "Remaining guesses: " + str((count))
        print "LOWER"
        print "Keep trying"
        print
    else:
        print "CORRECT!" 
        print "!!!"
        print "!!!"
        print "!!!"
        print "!!!"
        new_game()

    if count==0:
        print
        print
        print
        new_game()
        print "You lose"   


            
        

               


    
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)
inp = frame.add_input('input_guess', input_guess, 50)


# register event handlers for control elements and start frame
button1 = frame.add_button('Rabge is [0, 100)', range100)
button2 = frame.add_button('Range is [0, 1000)', range1000)

new_game()

frame.start()