from phrase import phrase
from game import game
from player import player
from wheel import wheel
from words import words
import const

import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

print("******The Wheel of Fortune******")
def start():
    return(initial_player())

def initial_player():
    for i in range(1,4):
        #Why assign to the list you saved in const? :)
        const.PLAYERS[i-1] = player()
        const.PLAYERS[i-1].set_name(input(f"Name of Player {i}: "))

    print(f"Welcome {const.PLAYERS[0].name}, {const.PLAYERS[1].name}, {const.PLAYERS[2].name}!")
    return const.PLAYERS

def start_game(player_list:list, phrase:str):
    wheel_img_folder_path = os.path.join(__location__,const.IMG_FOLDER,const.IMG_BASE_NAME)
    #Call game constructor and pass the phrase for game instance variable
    ready = game(phrase)
    #Load up wheel image
    w = wheel(wheel_img_folder_path)
    #Shows wheel image and pointer
    w.start()
    #Words constructor
    wor = words(phrase)
    #Print out blank words
    wor.start(w)
    #Call start_wof from game object
    ready.start_wof(player_list, w, wor)

if __name__ == "__main__":
    #List of players
    players = start()
    p = phrase()
    #Get phrase from phile
    phrase = p.random(os.path.join(__location__,'WofFPhrases.txt'))
    #Go to start game function
    start_game(players, phrase)
