import turtle
import time
import random
import const

class wheel():
    def __init__(self, wheel_path:str):
        self.image_folder_base = wheel_path
        self.screen = turtle.Screen()
        self.screen.setup(1600, 800)
        self.arrow = turtle.Turtle(visible=False)
        self.wof = turtle.Turtle(visible=False)
        self.prizes = const.PRIZES
        #Previous spin degree
        self.prev_spin_deg = 0

    def start(self):
        self.show_image()
        self.pointer()

    def show_image(self):
        self.wof.penup()
        self.wof.setx(-300)
        self.wof.sety(0)
        #Register the wheel images
        for i in range(360):
            self.screen.addshape(self.image_folder_base + str(i) + ".gif")
        #Show first image
        self.wof.shape(self.image_folder_base + str(0) + ".gif")
        self.wof.showturtle()

    def prize(self, degree:float) -> str:
        prizes = {
            "0": "325",
            "1": "100",
            "2": "450",
            "3": "25",
            "4": "500",
            "5": "bankrupt",
            "6": "125",
            "7": "300",
            "8": "225",
            "9": "350",
            "10": "275",
            "11": "free play",
            "12": "200",
            "13": "400",
            "14": "175",
            "15": "475",
            "16": "75",
            "17": "bankrupt",
            "18": "425",
            "19": "50",
            "20": "375",
            "21": "250",
            "22": "150",
            "23": "lose a turn"
        }
        
        if int(degree) < 7:
            degree += 360
        
        prize_degree = int(degree) - 7
        return prizes[str(prize_degree // 15)]

    def pointer(self):
        self.arrow.shape("triangle")
        self.arrow.penup()
        self.arrow.back(310)
        self.arrow.left(90)
        self.arrow.forward(340)
        self.arrow._rotate(180)
        self.arrow.showturtle()
        self.arrow.shapesize(2)
        self.perm_arrow = self.arrow.clone()
        self.arrow.hideturtle()

    def spin(self):
        #Get a random index
        idx = random.randint(0, len(self.prizes)-1)
        #Get result from the list of sectors
        result = self.prizes[idx]
        #Calculate the ending degree of the wheel to spin
        end_deg = (idx * 15) + 2
        #Spin the wheel
        self.spin_wheel_gui(self.prev_spin_deg, end_deg)
        #Save the last spin position
        self.prev_spin_deg = end_deg
        return result


    def spin_wheel_gui(self,start_deg, end_deg):
        if start_deg > end_deg:
            for i in range(start_deg, 359):
                self.wof.shape(self.image_folder_base + str(i) + ".gif")
            for i in range(end_deg):
                self.wof.shape(self.image_folder_base + str(i) + ".gif")
        else:
            for i in range(start_deg, end_deg):
                self.wof.shape(self.image_folder_base + str(i) + ".gif")








    # def spin(self, s:int) -> float:
    #     self.arrow.back(110)
    #     speed = s
    #     self.arrow.speed(speed)
    #     stop = False

    #     stop_count = 0

    #     while not stop:
    #         for i in range(360):
    #             stop_count += 1
    #             if not stop:
    #                 self.arrow.forward(110)
    #                 self.perm_arrow.setposition(self.arrow.pos())
    #                 self.perm_arrow.setheading(self.arrow.heading())
    #                 self.arrow.back(110)
    #                 self.arrow.right(1)

    #                 if stop_count == s:
    #                     self.arrow.setheading(self.perm_arrow.heading())
    #                     self.arrow.setposition(self.perm_arrow.pos())
    #                     stop = True
    #             else:
    #                 break

    #     return self.prize(self.arrow.heading())
    #     pass


                
