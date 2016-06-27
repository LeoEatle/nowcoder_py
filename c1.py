import random

class User():
    type = "User"

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return "im" + self.name + str(self.uid)


class Admin(User):
    type = "Admin"

    def __init__(self, name, aid, group):
        self.name = name
        self.aid = aid
        self.group = group

    def __repr__(self):
        return "im" + self.name +  str(self.aid) + self.group



def demo_random():
    print random.choice('abcdefghijklmn')
    test = ['a','b',3,'f']
    #print random.shuffle(test)
    random.shuffle(test)
    print test





print User('leo', 23)
print Admin('lara', 11, 'a')
demo_random()


