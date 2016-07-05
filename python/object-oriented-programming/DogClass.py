class Dog:
    def __init__(self, name, month, day, year, speakText):
        # Constructor of the class
        # self references the object itself
        self.name = name
        self.month = month
        self.day = day
        self. year = year
        self.speakText = speakText

    def __str__(self):
        # the str() operator was overloaded
        # such methods also called Magic Methods in Python
        return 'Dog name: ' + self.name + '\n' + \
               'Birth-date: ' + self.birthDate() + '\n' + \
               'Bark type: ' + self.speakText

    def speak(self):
        # Accessor method
        # returns the speakText
        return self.speakText

    def getName(self):
        # Accessor method
        # returns the name of the Dog
        return self.name

    def birthDate(self):
        # Accessor method
        # returns a string representing the birthday date
        return str(self.month) + '/' + str(self.day) + '/' + str(self.year)

    def changeBark(self, bark):
        # Mutator method
        # changes the speakText of the Dog object
        self.speakText = bark

def main():
    boyDog = Dog('Mesa', 5, 15, 2004, 'WOOOOF')
    girlDog = Dog('Sequoia', 5, 6, 2004, 'barkbark')
    print(str(boyDog))
    print(str(girlDog))
    boyDog.changeBark('woofywoofy')
    print(boyDog.speak())
    print(str(boyDog))


if __name__ == "__main__":
    # evaluates to True if the script was run from a shell
    main()