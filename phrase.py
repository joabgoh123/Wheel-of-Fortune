import random

class phrase:
    # this function generates a random phrase from the txt file
    def random(self, file_path:str) -> list:
        file = open(file_path, "r") #1st, open the txt file
        string1 = file.readlines() #2nd, read the contents inside the file

        list1 = [] #set a list to store the phrases
        for i in string1:
            if i != "":
                #keep adding the phrases from txt file to list
                list1.append(i.strip()) 

        return self.generate(list1) #call the generate function

    # this function generates a random phrase from the list
    def generate(self, phrase:list) -> str:
        return phrase[random.randint(0, len(phrase)-1)]
        #returns 1 random phrase only
