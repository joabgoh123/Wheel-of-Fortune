from AbstractState import State
class Bankrupt(State):
    def __init__(self,game_controller):
        self.game_controller = game_controller

    def play(self, player):
        player.bankrupt()
        print(player.name + "'s balance is : " + str(player.balance))
        return False

        