totalOfCoins = 50

current_player = 1

def subtractXcoinsOfTotal (subtractedCoins):
      global totalOfCoins
      totalOfCoins -= subtractedCoins

while True:
      try:
            numberOfPlayer = int(input("Enter the total number of players."))
            if numberOfPlayer < 2 or numberOfPlayer > 4:
                  print ("A minimum of 2 players is required, with a maximum limit of 4 players.")
            else:
                  break
      except ValueError:
            print("Enter a valid number.")

while totalOfCoins > 0 :
     try:
            print(f"There is a total of {totalOfCoins} coins.")
            print(f"It's player {current_player} turn.")
            subtractedCoins = int(input("Choose a number of coins to subtract (between 1 & 6) "))
            if subtractedCoins < 1 or subtractedCoins > 6:
                 print("Please enter a valid number between 1 and 6.")
            elif subtractedCoins > totalOfCoins:
                 print("You cannot subtract more coins than the total remaining.")
            else:
                   subtractXcoinsOfTotal(subtractedCoins)
                   print(f"There are {totalOfCoins} coins left.")
            if totalOfCoins == 0:
                   print(f"Player {current_player} win, all coins have been collected.")
                   break
            if current_player < numberOfPlayer:
                 current_player += 1
            else:
                 current_player = 1
     except ValueError:
           print("Enter a valid number.")



    