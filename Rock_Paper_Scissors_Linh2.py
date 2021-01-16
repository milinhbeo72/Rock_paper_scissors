def main():
    player_1 = input("Player 1, enter your choice (R/P/S): ")
    player_2 = input("Player 2, enter your choice (R/P/S): ")
    if player_1 == player_2:
        print("It's a tie!")
    else:
        if player_1 == "P":
            if player_2 == "R":
                print("Player 1 won!")
            else:
                print("Player 2 won!")
        elif player_1 == "R":
            if player_2 == "P":
                print("Player 2 won!")
            else:
                print("Player 1 won!")
        elif player_1 == "S":
            if player_2 == "P":
                print("Player 1 won!")
            else:
                print("Player 2 won!")
main()