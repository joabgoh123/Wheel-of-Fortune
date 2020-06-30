class player():
    def __init__(self):
        self.name = ''
        self.balance = 0

    def deduct(self, amount:int):
        self.balance -= amount

    def increase(self, amount:int):
        self.balance += amount

    def set_name(self, name:str):
        self.name = name

    def bankrupt(self):
        self.balance = 0

    def vowel_cost(self, amount:int) -> bool:
        if self.balance < amount:
            return False
        else:
            return True