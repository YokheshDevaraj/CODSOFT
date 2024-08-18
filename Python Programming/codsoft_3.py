import random

def computers_choice():
    return random.choice(['rock','paper','scissors'])

def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return 'tie'
    elif (user_choice=='rock' and computer_choice=='scissors') or (user_choice=='scissors' and computer_choice=='paper') or (user_choice=='paper' and computer_choice=='rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice,computer_choice,result):
    print(f"Your choice:{user_choice}")
    print(f"Computer's choice:{computer_choice}")
    
    if result=='tie':
        print("It's a tie")
    elif result=='user':
        print("You win")
    else:
        print("You lose")

def play_game():
    your_score=0
    computer_score=0
    
    while True:
        print("Rock,Paper,Scissors")
        user_choice=input("Choose rock,paper or scissors:").lower()
        
        if user_choice not in ['rock','paper','scissors']:
            print("Invalid choice")
            continue
        
        computer_choice=computers_choice()
        result=determine_winner(user_choice,computer_choice)
        
        display_result(user_choice,computer_choice,result)
        
        if result=='user':
            your_score+=1
        elif result=='computer':
            computer_score+=1
        
        print(f"Score-You:{your_score} | Computer:{computer_score}")
        
        play_again=input("Do you want to play again? (yes/no):").lower()
        if play_again!='yes':
            break


play_game()
