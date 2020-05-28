import random, string

class Names:
    name = []
    list = []
    finalName = ''
    def __init__(self):
        numList = []
        for i in range(10):
            numList.append(str(i))
        symbolList = ['!', '@', '#', '$', '%', '&']
        self.list = symbolList + numList + list(string.ascii_lowercase)#list() method makes a list with given strings

    def nameGen(self):
        characterAmount = input("How many characters do you want to the password? ")
        for i in range(int(characterAmount)):
            self.name.append(random.choice(self.list))
        self.finalName = "".join(self.name)
        return self.finalName
name = Names()
name.nameGen()
print(name.finalName)
