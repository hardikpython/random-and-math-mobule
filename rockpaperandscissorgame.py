import random
while True:
    user_action=input("Enter a choice(rock,paper and scissors)")
    possible_actions=["rock","paper","scissors"]
    computer_action=random.choice(possible_actions)
    print(f"/nYou chose{user_action}),computer chose{computer_action}./n")
    if user_action== computer_action:
        print(f"Both players selected{user_action}.It's a tie")
    elif user_action=="rock":
        if computer_action=="scissors":
            print("Rock smashes scissors! You win")
        else:
            print("paper covers rock! you lose.")
    elif user_action=="paper":
        if computer_action=="rock":
            print("paper covers rock!you win!")
        else:
            print("scissors cuts paper! you lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors cuts paper! you win!")
        else:
            print("Rock smashes scissors! you lose.")
            play_again= input("play again/(y/n):'")
            if play_again!="y":
                break

          