import random

def choice_name_mapping(choice):
    choice_names = {1:"Rock",2:"Paper",3:"Scissor"}
    return choice_names[choice]

def get_user_choice():
    choices="""
		    1. Rock
		    2. Paper
		    3. Scissor
	    """
    print(choices)

    user_choice = int(input("\nChoose your option : "))

    while user_choice > 3 or user_choice < 1:
        user_choice = int(input("\nEnter valid input: "))

    choice_name = choice_name_mapping(user_choice)
    print("User choice is: " + choice_name)
    return user_choice, choice_name 

def get_computer_choice(user_choice):
    print("\nNow its computer turn.......")
    computer_choice = random.randint(1, 3)

    if computer_choice == user_choice:
        computer_choice = random.randint(1, 3)

    comp_choice_name = choice_name_mapping(computer_choice)

    print("\nComputer choice is: " + comp_choice_name)
    return computer_choice, comp_choice_name

def compute(user_choice,user_choice_name, computer_choice, computer_choice_name):
    print(user_choice_name + " V/s " + computer_choice_name)

    if((user_choice == 1 and computer_choice == 2) or
          (user_choice == 2 and computer_choice ==1 )):
            print("paper wins => ", end = "")
            result = "Paper"
    elif((user_choice == 1 and computer_choice == 3) or
        (user_choice == 3 and computer_choice == 1)):
        print("Rock wins =>", end = "")
        result = "Rock"
    else:
        print("scissor wins =>", end = "")
        result = "Scissor"
  
    # Printing either user or computer wins
    if result == user_choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
          

def main():
    game_rules="""Winning Rules as follows :
				Rock vs Paper-> Paper wins
				Rock vs Scissor-> Rock wins
				Paper vs Scissor-> Scissor wins.
		"""
    print(game_rules)
    while 1:
        user_choice, user_choice_name = get_user_choice()
        computer_choice, computer_choice_name = get_computer_choice(user_choice)
        compute(user_choice, user_choice_name, computer_choice, computer_choice_name)
        print("Do you want to play again? (Y/N)")
        ans = input()
        # if user input n or N then condition is True
        if ans == 'n' or ans == 'N':
            break
    print("\nThanks for playing")

if __name__ == "__main__":
    main()