# You can use this workspace to write and submit your adventure game project.

import time

import random

animals = ["cat", "bunny", "pet komodo dragon", "prize-winning chinchilla"]


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You wake up in the middle of night in your bed.")
    print_pause("The room is pitch-black.")
    print_pause("You have an unsettling feeling in the pit of your stomach.")
    print_pause("You hear scratching and thrashing at your window.")
    print_pause("You reach for your flashlight.")
    print_pause("But it is out of batteries!")


def choice(items):
    print_pause("Enter 1 to get up and investigate.")
    print_pause("Enter 2 to hide under the covers.")
    choice = input("What would you like to do?\n"
                   "(please enter 1 or 2)")
    if choice == "1":
        investigate(items)
    elif choice == "2":
        go_to_sleep(items)
    else:
        print_pause("That's not possible right now.")


def investigate(items):
    if "batteries" in items:
        print_pause("You turn on your flashlight")
        print_pause("Cautiously, you approach the window.")
        print_pause("You push the window open and shine your light out.")
        print_pause("AHHH!!!")
        print_pause("Wait, it's just your " + random.choice(animals) + ".")
        print_pause("The pesky creature must've snuck out!")
        print_pause("You open the window and pull in your pet.")
        print_pause("CONGRATULATIONS!!")
        print_pause("You've solved the mystery and can go back to sleep!")
        play_again()
    else:
        print_pause("You muster up all your courage and stand up.")
        print_pause("It's too dark outside to see what's at the window.")
        print_pause("You should really find those batteries.")
        search_nightstand(items)


def search_nightstand(items):
    print_pause("Enter 1 to take your chances at the dark window.")
    print_pause("Enter 2 to check your nightstand for batteries.")
    find_batteries = input("What would you like to do?\n"
                           "(please enter 1 or 2)")
    if find_batteries == "1":
        print_pause("That's right! You're not scared of the dark!")
        print_pause("You take a step toward the window.")
        print_pause("But then you stumble and trip back into bed.")
        print_pause("That was enough excitement for one night.")
        print_pause("GAME OVER!")
        play_again()

    elif find_batteries == "2":
        print_pause("You shuffle around in your nightstand.")
        print_pause("You found the batteries!")
        items.append("batteries")
        print_pause("You sit down and put the batteries in your flashlight.")
        print_pause("Are you ready to get up now?")
        choice(items)
    else:
        print_pause("That's not possible right now.")
        choice(items)


def go_to_sleep(items):
    print_pause("You momentarily drift back off.")
    print_pause("Until...")
    print_pause("That darn sound starts back up!")
    print_pause("There is no way you can sleep through the noise.")
    choice(items)


def play_again():
    play_again = input("Do you want to play again? (y/n)")
    if play_again == "y":
        play_game()
    elif play_again == "n":
        print_pause("Thanks for playing, see ya next time!")
    else:
        print_pause("Please enter 'y' or 'n'.")
        play_again()


def play_game():
    items = []
    intro()
    choice(items)


play_game()
