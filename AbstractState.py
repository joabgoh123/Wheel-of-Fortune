from abc import ABC, abstractmethod
import const
import parse_input
class State(ABC):
    def __init__(self,game_controller):
        self.game_controller = game_controller
        super.__init__()
        self.pattern = r'[a-zA-Z]'
        self.vowel = const.VOWEL
        self.consonent = const.CONSONANT

    @abstractmethod
    def play(self, player):
        pass
    
    def handle_vowel(self, player):
        vowel = parse_input.get_vowel_input()
        #Check is letter in phrase
        if vowel in self.game_controller.phrase and vowel not in self.game_controller.guessed_letters:
            _ , _ = self.game_controller.reveal_words(vowel)
            self.game_controller.guessed_letters.add(vowel)
            print(player.name + "'s balance is : " + str(player.balance))
            action = parse_input.vowel_success_action()
            self.check_game_completed(player)

            if action == const.CHOICE_SPIN_AGAIN:
                return True
            elif action == const.CHOICE_VOWEL:
                return self.handle_vowel(player)
            else:
                return False
        else:
            return False

    def handle_consonant(self, player):
        consonant = parse_input.get_consonant_input()
        #Check is letter in phrase
        if consonant in self.game_controller.phrase and consonant not in self.game_controller.guessed_letters:
            _ , count = self.game_controller.reveal_words(consonant)
            player.increase(count * int(self.game_controller.result))
            print(player.name + "'s balance is : " + str(player.balance))
            self.game_controller.guessed_letters.add(consonant)
            action = parse_input.consonant_success_action()
            self.check_game_completed(player)

            if action == const.CHOICE_SPIN_AGAIN:
                return True
            elif action == const.CHOICE_VOWEL:
                return self.handle_vowel(player)
            else:
                return self.handle_guess_phrase(player)

    def handle_guess_phrase(self, player):
        phrase = parse_input.get_phrase()
        if phrase == self.game_controller.phrase:
            letters_in_phrase = [letter for letter in self.game_controller.phrase if letter != ' ']
            for letter in letters_in_phrase:
                self.game_controller.guessed_letters.add(letter)
            self.check_game_completed(player)
    
    def check_game_completed(self, player):
        if len(set(self.game_controller.phrase)) == len(set(self.game_controller.guessed_letters)) + 1:
            self.game_controller.game.game_end(player)


    



