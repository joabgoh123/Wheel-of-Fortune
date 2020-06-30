from AbstractState import State
import parse_input
import const
class FreePlay(State):
    def __init__(self,game_controller):
        self.game_controller = game_controller
    
    def play(self, player):
        time_exceeded = False
        try:
            letter = parse_input.free_play_letter()
        except KeyboardInterrupt:
            time_exceeded = True

        if time_exceeded == True:
            return False


        if letter in self.game_controller.phrase and letter not in self.game_controller.guessed_letters:
            _ , _ = self.game_controller.reveal_words(letter)
        
        action = parse_input.consonant_success_action()
        if action == const.CHOICE_SPIN_AGAIN:
            return True
        elif action == const.CHOICE_VOWEL:
            return self.handle_vowel(player)
        else:
            return self.handle_guess_phrase(player)
    
