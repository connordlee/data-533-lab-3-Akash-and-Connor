class member:
    def __init__(self, name, nationality, salary, yearsWClub):
        self.name = name
        self.nationality = nationality
        self.__salary = salary
        self.yearsWClub = yearsWClub
        
    def updateNationality(self, newNationality):
        self.nationality = newNationality
        
    def setSalary(self, newSalary):
        self.__salary = newSalary
        
    def getSalary(self):
        return self.__salary
    
    def newYear(self):
        self.yearsWClub += 1

    def display(self):
        print("           Name: {}\n    Nationality: {}\nYears With Club: {}".format(self.name, self.nationality, self.yearsWClub))
