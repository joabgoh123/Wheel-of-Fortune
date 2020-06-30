import re
from AbstractState import State
import parse_input
# from parser import get_user_choice, get_vowel_input, get_consonant_input, get_phrase
import const
class Number(State):
    def __init__(self,game_controller):
        self.game_controller = game_controller

    def play(self, player):
        time_exceeded = False
        try:
            #I didn't see the part where not enough money for vowel need spin again
            # choice = parse_input.get_user_choice(can_buy_vowel = player.vowel_cost(amount= const.VOWEL_COST))
            choice = parse_input.get_user_choice(True)
            if choice == const.CHOICE_VOWEL and not player.vowel_cost(amount=const.VOWEL_COST):
                print("Not enough money to buy vowel! Spin again!")
                return True

        except KeyboardInterrupt:
            time_exceeded = True

        if time_exceeded == True:
            return False

        if choice == const.CHOICE_VOWEL:
            player.deduct(const.VOWEL_COST)
            return self.handle_vowel(player)
        elif choice == const.CHOICE_CONSONANT:
            return self.handle_consonant(player)
        elif choice == const.CHOICE_GUESS_PHRASE:
            self.handle_guess_phrase(player)

