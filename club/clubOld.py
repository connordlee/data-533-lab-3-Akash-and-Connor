from club.member import membertypes as mt
class club:
    def __init__(self, playerList=None, staffList=None):
        self.members = {'players':[], 'staff':[]}
        if playerList!=None:
            for player in playerList:
                self.addPlayer(player[0], player[1], player[2], player[3], player[4], player[5])
        self.fans = {'domestic':[], 'international':[]}
        if staffList!=None:
            for staff in staffList:
                self.addStaff(staff[0], staff[1], staff[2], staff[3], staff[4])
        self.fans = {'domestic':[], 'international':[]}
    
    def addPlayer(self, name, nationality, salary, yearsWClub, position, jersey):
        newPlayer = mt.player(name, nationality, salary, yearsWClub, position, jersey)
        self.members['players'].append(newPlayer)
    
    def addStaff(self, name, nationality, salary, yearsWClub, title):
        newStaff = mt.staff(name, nationality, salary, yearsWClub, title)
        self.members['staff'].append(newStaff)
        
    def displayPlayers(self, salary=None):
        for player in self.members['players']:
            player.display()
            if salary==True:
               print("         Salary: ${}".format(player.getSalary()))
            print("\n")
            
    def displayStaff(self, salary=None):
        for staff in self.members['staff']:
            staff.display()
            if salary==True:
               print("         Salary: ${}".format(staff.getSalary()))
            print('\n')
    
    def displayMembers(self, salary=None):
        self.displayStaff(salary)
        self.displayPlayers(salary)

    def removePlayer(self, name):
        for player in self.members['players']:
            if player.name == name:
                self.members['players'].remove(player)

    def removeStaff(self, name):
        for staff in self.members['staff']:
            if staff.name == name:
                self.members['staff'].remove(staff)

    def updatePlayer(self, name, nationality=None, salary=None, yearsWClub=None, position=None, jersey=None):
        for player in self.members['players']:
            if player.name == name:
                break
        if nationality != None:
            player.updateNationality(nationality)
        if salary != None:
            player.setSalary(salary)
        if yearsWClub != None:
            player.yearsWClub = yearsWClub
        if position != None:
            player.updatePosition(position)
        if jersey != None:
            player.updateJerseyNum(jersey)

    def updateStaff(self, name, nationality=None, salary=None, yearsWClub=None, title=None):
        for staff in self.members['staff']:
            if staff.name == name:
                break
        if nationality != None:
            staff.updateNationality(nationality)
        if salary != None:
            staff.setSalary(salary)
        if yearsWClub != None:
            staff.yearsWClub = yearsWClub
        if title != None:
            staff.updateTitle(title)
