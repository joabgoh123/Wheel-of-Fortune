import itertools
import signal
import time
import re
import sys
import const
import random
from GameController import GameController


class game():
    def __init__(self, phrase:str):
        self.vowel = const.VOWEL
        self.consonant = const.CONSONANT
        self.phrase = phrase
        print(self.phrase)
        self.reveal = re.sub('[A-Za-z]', "_ ", self.phrase)
        print(self.reveal)
        self.pattern = r'[a-zA-Z]'
        self.success_choice = r'[1-3]'
        self.char_location()
        self.player_list = None
        
        self.gameController = None

    #dict_char in instance variable idx for each character
    def char_location(self):
        unique_char = set(self.phrase)
        self.dict_char = {}
        for each_char in unique_char:
            self.dict_char[each_char] = [index for index, char in enumerate(self.phrase) if char == each_char]

    def start_wof(self, player_list:list, wheel:object, words:object):
        self.wheel = wheel
        self.words = words
        self.player_list = player_list
        print(self.phrase)
        #Instantiate Game Controller
        self.gameController = GameController(self.phrase, wheel, words, self.dict_char, self)
        for i in itertools.count():
            turn = i % 3
            self.turn(player_list[turn])

    def turn(self, player):
        print(f"{player.name}'s turn!")
        print(f"Balance: ${player.balance}")
        return self.gameController.play(player)
    
    def game_end(self, player):
        print(f"Congratulations {player.name} you have won!")
        self.words.reveal_all(self.dict_char)
        self.player_list.sort(key=lambda x: x.balance, reverse = True)
        print("========Score Board========")
        for player in self.player_list:
            print(player.name + ": " + str(player.balance))
        print("Game will close in 15 seconds")
        time.sleep(15)
        sys.exit()




        

