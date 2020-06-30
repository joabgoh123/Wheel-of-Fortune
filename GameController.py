from BankruptState import Bankrupt
from FreePlayState import FreePlay
from NumberState import Number
from LoseTurnState import LoseTurn
import re

class GameController():
    def __init__(self, phrase, wheel, words, dict_char, game):
        self.game = game
        self.phrase = phrase
        #Initial State
        self.state = None
        self.wheel = wheel
        self.words = words
        self.dict_char = dict_char
        self.bankrupt = Bankrupt(self)
        self.number= Number(self)
        self.loseTurn = LoseTurn(self)
        self.freePlay = FreePlay(self)
        self.reveal = re.sub('[A-Za-z]', "_ ", self.phrase)
        self.guessed_letters = set()

    def set_state(self, state):
        if state.isnumeric():
            self.state = "number"
        else:
            self.state = state

    def play(self, player):
        turn_ongoing = True
        while turn_ongoing == True:
            while True:
                spin = input("Press enter to spin: ")
                if spin.lower() == '' or spin == '':
                    self.result = self.wheel.spin()
                    self.set_state(self.result)
                    print(f"{player.name} has landed on {self.result}!\n")
                    break
            if self.state == "bankrupt":
                turn_ongoing = self.bankrupt.play(player)
            elif self.state == "lose a turn":
                turn_ongoing = self.loseTurn.play(player)
            elif self.state == "number":
                turn_ongoing = self.number.play(player)
            elif self.state == "free play":
                turn_ongoing = self.freePlay.play(player)
            

    def reveal_words(self, choice:str) -> bool:
        count = 0
        if choice in self.dict_char:
            for index in self.dict_char[choice]:
                self.words.reveal(index, choice)
                self.reveal = self.reveal[:index] + choice + self.reveal[index:]
                count += 1

            print(self.reveal)
            del self.dict_char[choice]
            return True, count
        else:
            print(f"Sorry! The letter {choice} is not in the puzzle!")
            return False, 0



    


