import const
import sys
import threading
from time import sleep
import _thread as thread

def quit_function(fn_name):
    # print to stderr, unbuffered in Python 2.
    print('{0} took too long'.format(fn_name), file=sys.stderr)
    sys.stderr.flush() # Python 3 stderr is likely buffered.
    thread.interrupt_main() # raises KeyboardInterrupt

def exit_after(s):
    '''
    use as decorator to exit process if 
    function takes longer than s seconds
    '''
    def outer(fn):
        def inner(*args, **kwargs):
            timer = threading.Timer(s, quit_function, args=[fn.__name__])
            timer.start()
            try:
                result = fn(*args, **kwargs)
            finally:
                timer.cancel()
            return result
        return inner
    return outer




@exit_after(const.TIMEOUT)
def get_user_choice(can_buy_vowel):
    while True:
        print("You have 10 Seconds to make your selection!!!")
        print("Press enter to move to next player's turn if time exceeded")
        choice = input("Enter 1 to buy a vowel, 2 to choose a consonant and 3 to solve the puzzle: ")
        if choice == "1"  and can_buy_vowel:
            return const.CHOICE_VOWEL
        elif choice == "2":
            return const.CHOICE_CONSONANT
        elif choice == "3":
            return const.CHOICE_GUESS_PHRASE
        else:
            print("Invalid choice or insufficient funds")

def get_vowel_input():
    while True:
        vowel = input("Please enter your vowel: ").upper()
        if vowel in const.VOWEL:
            return vowel

def get_consonant_input():
    while True:
        consonant = input("Please enter your consonant: ").upper()
        if consonant in const.CONSONANT:
            return consonant

def get_phrase():
    while True:
        phrase = input("Please enter your phrase: ").upper()
        if phrase.replace(' ','').isalpha():
            return phrase

def consonant_success_action():
    while True:
        action = input("Enter 1 to spin the wheel again, 2 to buy a vowel and 3 to solve the puzzle: ")
        if action == "1":
            return const.CHOICE_SPIN_AGAIN
        elif action == "2":
            return const.CHOICE_VOWEL
        elif action == "3":
            return const.CHOICE_GUESS_PHRASE
        else:
            print("Invalid choice")

def vowel_success_action():
    while True:
        action = input("Enter 1 to spin the wheel again, 2 to buy another vowel: ")
        if action == "1":
            return const.CHOICE_SPIN_AGAIN
        elif action == "2":
            return const.CHOICE_VOWEL
        else:
            print("Invalid Choice")

def free_play_letter():
    while True:
        letter = input("Please enter a letter: ").upper()
        if letter.isalpha() and len(letter) == 1:
            return letter



