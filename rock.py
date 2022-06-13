# import random module

import random
 
# Print multiline instruction
# performstring concatenation of string

print("Winning Rules of the Rock paper scissor game as follows: \n"

                                +"Rock vs paper->paper wins \n"

                                + "Rock vs scissor->Rock wins \n"

                                +"paper vs scissor->scissor wins \n")
 

while True:

    print("Enter choice \n R for Rock, \n P for paper, and \n S for scissors \n")

     

    # take the input from user

    choice = int(input("User turn: "))
 

    # OR is the short-circuit operator

    # if any one of the condition is true

    # then it return True value

     

    # looping until user enter invalid input

    while choice > S or choice < R:

        choice = int(input("enter valid input: "))

         
 

    # initialize value of choice_name variable

    # corresponding to the choice value

    if choice == R:

        choice_name = 'Rock'

    elif choice == P:

        choice_name = 'paper'

    else:

        choice_name = 'scissor'

         

    # print user choice 

    print("user choice is: " + choice_name)

    print("\nNow its computer turn.......")
 

    # Computer chooses randomly any number 

    # among R , P and S. Using randint method

    # of random module

    comp_choice = random.randint(R, S)

     

    # looping until comp_choice value 

    # is equal to the choice value

    while comp_choice == choice:

        comp_choice = random.randint(R, S)
 

    # initialize value of comp_choice_name 

    # variable corresponding to the choice value

    if comp_choice == R:

        comp_choice_name = 'Rock'

    elif comp_choice == P:

        comp_choice_name = 'paper'

    else:

        comp_choice_name = 'scissor'

         

    print("Computer choice is: " + comp_choice_name)
 

    print(choice_name + " V/s " + comp_choice_name)

    #we need to check of a draw

    if choice == comp_choice:

        print("Draw=> ", end = "")

        result = Draw

       

    # condition for winning

        if((choice == R and comp_choice == P) or

          (choice == R and comp_choice ==P )):

            print("paper wins => ", end = "")

            result = "paper"
 

        elif((choice == R and comp_choice == S) or

            (choice == S and comp_choice == R)):

            print("Rock wins =>", end = "")

            result = "Rock"

        else:

            print("scissor wins =>", end = "")

            result = "scissor"
 

    # Printing either user or computer wins or draw

    if result == Draw:

        print("<== Its a tie ==>")

    if result == choice_name:

        print("<== User wins ==>")

    else:

        print("<== Computer wins ==>")

         

    print("Do you want to play again? (Y/N)")

    ans = input().lower
 
 

    # if user input n or N then condition is True

    if ans == 'n':

        break

     
# after coming out of the while loop
# we print thanks for playing

print("\nThanks for playing")
 
