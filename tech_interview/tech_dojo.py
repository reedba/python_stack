


class Animal:
    def __init__(self, type):
        self.type = type

    def talk(self):
        if self.type == 'dog':
            print('bark')
        if self.type == 'cat':
            print('Meow')




dog = Animal('dog')
cat = Animal('cat')


dog.talk()
cat.talk()