
# =============Created by Mahim Chowdhury=================#
# Please try it on a python IDE #

from random import *

def computer():
    turn_list = [1, 2, 3, 4, 5, 6]
    computer_turn = choice(turn_list)
    return computer_turn


#######
def add(list):
    sum = 0
    for e in list:
        sum = e + sum
    return sum


#######
def user_batting():
    print("You are batting now:")
    wickets = 0
    run_list = []
    turn_list = [1, 2, 3, 4, 5, 6]
    while True:
        user_run = input("Your turn:")
        try:
            user_run = int(user_run)
        except:
            user_run = str(user_run)
        computer_run = computer()
        if user_run == computer_run:
            print("Computer's turn:", computer_run)
            print("Out")
            wickets = wickets + 1
            print("Scoreline:", add(run_list), "/", wickets)
            if wickets == 10:
                break
        elif user_run == "score" or user_run == "s":
            print(add(run_list), "/", wickets)
        elif user_run not in turn_list:
            print("invalid")
        else:
            print("Computer's turn:", computer_run)
            run_list.append(user_run)
    return [add(run_list), wickets]


#######
def user_chasing(target):
    print("You are now chasing the target:")
    wickets = 0
    run_list = []
    turn_list = [1, 2, 3, 4, 5, 6]
    while True:
        user_run = input("Your turn:")
        try:
            user_run = int(user_run)
        except:
            user_run = str(user_run)
        computer_run = computer()
        if user_run == computer_run:
            print("Computer's turn:", computer_run)
            print("Out")
            wickets = wickets + 1
            print("Scoreline:", add(run_list), "/", wickets)
            if wickets == 10:
                break
        elif user_run == "score" or user_run == "s":
            print(add(run_list), "/", wickets)
        elif user_run not in turn_list:
            print("invalid")
        else:
            print("Computer's turn:", computer_run)
            run_list.append(user_run)
            if add(run_list) >= target:
                # return_list = [add(run_list),()]
                return [add(run_list), wickets]

    return [add(run_list), wickets]


#######
def computer_chasing(target):
    print("Computer is now chasing your total:")
    wickets = 0
    run_list = []
    turn_list = [1, 2, 3, 4, 5, 6]
    while True:
        user_run = input("Your turn:")

        try:
            user_run = int(user_run)
        except:

            user_run = str(user_run)
        computer_run = computer()
        if computer_run == user_run:
            print("Computer's turn:", computer_run)
            print("Out")
            wickets = wickets + 1
            print("Scoreline:", add(run_list), "/", wickets)
            if wickets == 10:
                break
        elif user_run == "score" or user_run == "s":
            print(add(run_list), "/", wickets)
        elif user_run not in turn_list:
            print("invalid")
        else:
            print("Computer's turn:", computer_run)
            run_list.append(computer_run)
            if add(run_list) >= target:
                return [add(run_list), wickets]

    return [add(run_list), wickets]


#######
def computer_batting():
    print("Computer is batting now:")
    wickets = 0
    run_list = []
    turn_list = [1, 2, 3, 4, 5, 6]
    while True:
        user_run = input("Your turn:")

        try:
            user_run = int(user_run)
        except:

            user_run = str(user_run)
        computer_run = computer()
        if computer_run == user_run:
            print("Computer's turn:", computer_run)
            print("Out")
            wickets = wickets + 1
            print("Scoreline:", add(run_list), "/", wickets)
            if wickets == 10:
                break
        # elif user_run == None:
        # continue
        elif user_run == "score" or user_run == "s":
            print(add(run_list), "/", wickets)
        elif user_run not in turn_list:
            print("invalid")
        else:
            print("Computer's turn:", computer_run)
            run_list.append(computer_run)
    return [add(run_list), wickets]


#######
def toss():
    while True:
        valid_toss_list = ["heads", "head", "h", "H", "Heads", "Head", "tails", "tail", "t", "T", "Tails", "Tail"]
        heads_list = valid_toss_list[0:5]
        tails_list = valid_toss_list[5:len(valid_toss_list)]
        user_call = input("Please enter your call:")
        if user_call in heads_list:
            user_tossed = "Heads"
        elif user_call in tails_list:
            user_tossed = "Tails"
        else:
            print("Invalid call.\nPlease toss again.")
            continue
        toss_list = ["Heads", "Tails"]
        fate = choice(toss_list)
        if user_tossed == fate:
            return "won"
        else:
            return "lost"


#######
def bat_or_bowl():
    act_list = ["bat", "bowl"]
    act = choice(act_list)
    return act


#######
def maingame():
    while True:
        Toss = toss()
        if Toss == "won":
            print("You", Toss, "the toss!")
            user_choice = input("What would you like to do first?\nYour choice:")
            if user_choice == "bat" or user_choice == "b":
                user_run_wickets = user_batting()
                user_score = user_run_wickets[0]
                user_wickets = user_run_wickets[1]
                target_score = user_score + 1
                print("Your score:", user_score, "/", user_wickets)
                print("Computer target:", target_score)
                computer_run_wickets = computer_chasing(target_score)
                computer_score = computer_run_wickets[0]
                computer_wickets = computer_run_wickets[1]
                run_margin = user_score - computer_score
                wickets_margin = 10 - computer_wickets
                if user_score > computer_score:
                    print("Computer score:", computer_score, "/", computer_wickets)
                    print("CONGRATS! You won the match by", run_margin, "runs!")
                    break
                elif user_score == computer_score:
                    print("Computer score:", computer_score, "/", computer_wickets)
                    print("It's a Draw!")
                    break
                elif target_score <= computer_score:
                    print("Computer score:", computer_score, "/", computer_wickets)
                    print("Oops! You lost by", wickets_margin, "wickets!")
                    break
            elif user_choice == "bowl" or user_choice == "bl":
                computer_run_wickets = computer_batting()
                computer_score = computer_run_wickets[0]
                computer_wickets = computer_run_wickets[1]
                target_score = computer_score + 1
                print("Computer score:", computer_score, "/", computer_wickets)
                print("Your target:", target_score)
                user_run_wickets = user_chasing(target_score)
                user_score = user_run_wickets[0]
                user_wickets = user_run_wickets[1]
                run_margin = computer_score - user_score
                wickets_margin = 10 - user_wickets
                if user_score >= target_score:
                    print("Your score:", user_score, "/", user_wickets)
                    print("CONGRATS! You won the match by", wickets_margin, "wickets!")
                    break
                elif user_score == computer_score:
                    print("Your score:", user_score, "/", user_wickets)
                    print("It's a Draw!")
                    break
                elif computer_score > user_score:
                    print("Your score:", user_score, "/", user_wickets)
                    print("Oops! You lost by", run_margin, "runs!")
                    break
            else:
                print("Invalid choice.\nPlease toss again.")
        elif Toss == "lost":
            print("You", Toss, "the toss!")
            computer_choice = bat_or_bowl()
            print("Computer choose to", computer_choice)
            if computer_choice == "bat":
                computer_run_wickets = computer_batting()
                computer_score = computer_run_wickets[0]
                computer_wickets = computer_run_wickets[1]
                target_score = computer_score + 1
                print("Computer score:", computer_score, "/", computer_wickets)
                print("Your target:", target_score)
                user_run_wickets = user_chasing(target_score)
                user_score = user_run_wickets[0]
                user_wickets = user_run_wickets[1]
                run_margin = computer_score - user_score
                wickets_margin = 10 - user_wickets
                if user_score >= target_score:
                    print("Your score:", user_score, "/", user_wickets)
                    print("CONGRATS! You won the match by", wickets_margin, "wickets!")

                    break
                elif user_score == computer_score:
                    print("Your score:", user_score, "/", user_wickets)
                    print("It's a Draw!")
                    break
                elif computer_score > user_score:
                    print("Your score:", user_score, "/", user_wickets)
                    print("Oops! You lost by", run_margin, "runs!")
                    break
            if computer_choice == "bowl":
                user_run_wickets = user_batting()
                user_score = user_run_wickets[0]
                user_wickets = user_run_wickets[1]
                target_score = user_score + 1
                print("Your score:", user_score, "/", user_wickets)
                print("Computer target:", target_score)
                computer_run_wickets = computer_chasing(target_score)
                computer_score = computer_run_wickets[0]
                computer_wickets = computer_run_wickets[1]
                run_margin = user_score - computer_score
                wickets_margin = 10 - computer_wickets
                if user_score > computer_score:
                    print("Computer score:", computer_score, "/", computer_wickets)
                    print("CONGRATS! You won the match by", run_margin, "runs!")
                    break
                elif user_score == computer_score:
                    print("Computer score:", computer_score, "/", computer_wickets)
                    print("It's a Draw")
                    break
                elif target_score <= computer_score:
                    print("Computer score:", computer_score, "/", computer_wickets)
                    print("Oops! You lost by", wickets_margin, "wickets!")
                    break


#######

#######
def run_game():
    print("Welcome to my cricket game:)")
    maingame()
    while True:
        y_or_n = input("\nWould you like to try again?\nYour command(y/any):")
        if y_or_n == "y" or y_or_n == "yes":
            maingame()
        else:
            break
    print("\nThanks for playing:)")


#######


run_game()
