total_of_coins = 50

current_player = 1


def subtract_x_coins_of_total(subtracted_coins):
    global total_of_coins
    total_of_coins -= subtracted_coins


while True:
    try:
        number_of_player = int(input("Enter the total number of players. "))
        if number_of_player < 2 or number_of_player > 4:
            print(
                "A minimum of 2 players is required, with a maximum limit of 4 players. "
            )
        else:
            break
    except ValueError:
        print("Enter a valid number.")

while total_of_coins > 0:
    try:
        print(f"There is a total of {total_of_coins} coins.")
        print(f"It's player {current_player} turn.")
        while True:
            try:
                subtracted_coins = int(
                    input("Choose a number of coins to subtract (between 1 & 6) ")
                )
                if subtracted_coins < 1 or subtracted_coins > 6:
                    print("Please enter a valid number between 1 and 6.")
                elif subtracted_coins > total_of_coins:
                    print("You cannot subtract more coins than the total remaining.")
                else:
                    break
            except ValueError:
                print("Enter a valid number.")
        subtract_x_coins_of_total(subtracted_coins)
        print(f"There are {total_of_coins} coins left.")
        if total_of_coins == 0:
            print(f"Player {current_player} win, all coins have been collected.")
            break
        if current_player < number_of_player:
            current_player += 1
        else:
            current_player = 1
    except ValueError:
        print("Enter a valid number.")
