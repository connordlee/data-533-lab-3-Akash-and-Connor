from club.member.member import member as m

class player(m):
    def __init__(self, name, nationality, salary, yearsWClub, position, jersey):
        m.__init__(self, name, nationality, salary, yearsWClub)
        self.position = position
        self.jersey = jersey

    def updatePosition(self, newPosition):
        self.position = newPosition
    
    def updateJerseyNum(self, newJersey):
        self.jersey = newJersey

    def asList(self):
        return [self.name, self.nationality, self.getSalary(), self.yearsWClub, self.position, self.jersey]

    def display(self):
        m.display(self)
        print("       Position: {}\n  Jersey Number: {}".format(self.position, self.jersey))

class staff(m):
    def __init__(self, name, nationality, salary, yearsWClub, title):
        m.__init__(self, name, nationality, salary, yearsWClub)
        self.title = title
    
    def updateTitle(self, newTitle):
        self.title = newTitle
    
    def display(self):
        m.display(self)
        print("      Job Title: {}".format(self.title))

    def asList(self):
        return [self.name, self.nationality, self.getSalary(), self.yearsWClub, self.title]


