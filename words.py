import turtle
import const

class words():
    def __init__(self, phrase:str):
        self.phrase = phrase
        self.square = turtle.Turtle(visible=False)
        self.x_pos = const.X_POS
        self.y_pos = const.Y_POS
        
    def start(self, wheel:object):
        self.square.shape("square")
        self.square.fillcolor("white")
        self.square.penup()
        self.square.shapesize(4, 4)
        self.square.setx(self.x_pos)
        self.square.sety(self.y_pos)

        self.dict_square = {
            0: self.square 
        }

        num_squares = list(self.phrase)
        self.fake = self.square.clone()
        self.fake.showturtle()
        self.x_pos += const.X_MOVE
        for index, letter in enumerate(num_squares[1:]):
            if letter is not ' ':
                self.dict_square[index+1] = self.square.clone()
                self.dict_square[index+1].setx(self.x_pos)
                self.dict_square[index+1].sety(self.y_pos)
                self.x_pos += const.X_MOVE
                self.dict_square[index+1].showturtle()
            else:
                self.x_pos = const.X_POS
                self.y_pos -= const.Y_MOVE
    
    def reveal(self, index:int, letter:str):
        write = turtle.Turtle(visible=False)
        write.penup()
        write.goto(self.dict_square[index].pos()[0]+1, self.dict_square[index].pos()[1]-20)
        write.write(letter, font=("Arial", 40))
        write.shapesize(0.1)
        write.showturtle()

    def reveal_all(self, remaining_char:dict):
        for key, values in remaining_char.items():
            if key is not ' ':
                for index in values:
                    write = turtle.Turtle(visible=False)
                    write.penup()
                    write.goto(self.dict_square[index].pos()[0]+1, self.dict_square[index].pos()[1]-20)
                    write.write(key, font=("Arial", 40))
                    write.showturtle()
