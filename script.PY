totalOfCoins = 50

def subtractXcoinsOfTotal (subtractedCoins):
      global totalOfCoins
      totalOfCoins -= subtractedCoins

while totalOfCoins > 0 :
     try:
            subtractedCoins = int(input("Choose a number of coins to subtract (between 1 & 6) "))
            if subtractedCoins < 1 or subtractedCoins > 6:
                 print("Please enter a valid number between 1 and 6.")
            elif subtractedCoins > totalOfCoins:
                 print("You cannot subtract more coins than the total remaining.")
            else:
                   subtractXcoinsOfTotal(subtractedCoins)
                   print(f"There are {totalOfCoins} coins left.")
     except ValueError:
           print("Please enter a valid number.")

if totalOfCoins == 0:
    print("You win, all coins have been collected!")


    