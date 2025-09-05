import random
user_choice= int(input("Enter your choice(0 rock, 1 paper, 2 scissors):"))
computer_choice= random.randint(0,2)
sign=['rock','paper','scissors']
print("Computer chose ",sign[computer_choice])
if user_choice == computer_choice:
    print("Draw")
if user_choice==2 and computer_choice==0:
    print("You lose")
elif user_choice==0 and computer_choice==2:
    print("You win")
elif user_choice < computer_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win")