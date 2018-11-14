class Player:

    def __init__(self, id, fname='', lname=''):
        self.id = id
        self.firstName = fname
        self.lastName = lname

    def getId(self):
        return self.id

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getFullName(self):
        return self.firstName + " " + self.lastName

    def editName(self, first, last):
        self.firstName = first
        self.lastName = last

    def __str__(self):
        return '{} {}'.format(self.firstName, self.lastName)

