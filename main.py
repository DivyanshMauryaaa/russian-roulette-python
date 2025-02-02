import random
import os

def pullTrigger(loadedChamber, selectedChamber):
    
    if loadedChamber == selectedChamber:
        print("I LOST!! I DONT DESERVE TO LIVEE!!! As a gentle punishment for myself. I am now commiting scucide. Please wait....")
        #os.remove("C:/Windows/System32")
        
    else:
        print("Your turn now...")
        
    print()
    
    print("Sammuary: ")
    print(f"The bullet was loaded in {loadedChamber} chamber")
    print(f"The {selectedChamber} chamber was selected")

def main():

    print("Russian Roulette")

    while True:
        loadedChamber = random.randint(1, 6)
        selectedChamber = random.randint(1, 6)
    
        pullTrigger(loadedChamber, selectedChamber)
        print("Do you want to play again? (y/n)")
        playAgain = input()

        if playAgain == "n":
            break
        else:
            continue


main()