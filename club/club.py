from club.member import membertypes as mt
from club.fan import fantype as ft
class club:
    def __init__(self, playerList=None, staffList=None, domesticList = None, internationalList = None):
        self.members = {'players':[], 'staff':[]}
        self.fans = {'domestic':[], 'international':[]}
        
        if playerList!=None:
            for player in playerList:
                self.addPlayer(player[0], player[1], player[2], player[3], player[4], player[5])
        
        if staffList!=None:
            for staff in staffList:
                self.addStaff(staff[0], staff[1], staff[2], staff[3], staff[4])
        
        if domesticList!=None:
            for domestic in domesticList:
                self.addDomestic(domestic[0], domestic[1], domestic[2], domestic[3], domestic[4], domestic[5])        
        
        if internationalList!=None:
            for international in internationalList:
                self.addInternational(international[0], international[1], international[2], international[3], international[4], international[5])        
    
    def addPlayer(self, name, nationality, salary, yearsWClub, position, jersey):
        newPlayer = mt.player(name, nationality, salary, yearsWClub, position, jersey)
        self.members['players'].append(newPlayer)
        
    def addDomestic(self, name, favouritePlayer, purchasedMerchandise, currentCity, hasSeasonTickets, yearsSinceFan):
        newDomestic = ft.domestic(name, favouritePlayer, purchasedMerchandise, currentCity, hasSeasonTickets, yearsSinceFan)
        self.fans['domestic'].append(newDomestic)
    
    def addStaff(self, name, nationality, salary, yearsWClub, title):
        newStaff = mt.staff(name, nationality, salary, yearsWClub, title)
        self.members['staff'].append(newStaff)
        
    def addInternational(self, name, favouritePlayer, purchasedMerchandise, currentCity, country, viewMatches):
        newInternational = ft.international(name, favouritePlayer, purchasedMerchandise, currentCity, country, viewMatches)
        self.fans['international'].append(newInternational)
        
    def displayPlayers(self, salary=None):
        for player in self.members['players']:
            player.display()
            if salary==True:
               print("         Salary:", player.getSalary())
            print("\n")
            
    def displayDomestic(self):
        for domestic in self.fans['domestic']:
            domestic.display()
            print("\n")
    
    def displayStaff(self, salary=None):
        for staff in self.members['staff']:
            staff.display()
            if salary==True:
               print("         Salary:", staff.getSalary())
            print("\n")
    
    def displayInternational(self):
        for international in self.fans['international']:
            international.display()
            print("\n")
    
    def displayMembers(self, salary=None):
        self.displayStaff(salary)
        self.displayPlayers(salary)

    def displayFans(self):
        self.displayDomestic()
        self.displayInternational()

    def removePlayer(self, name):
        for player in self.members['players']:
            if player.name == name:
                self.members['players'].remove(player)
                
    def removeDomestic(self, name):
        for domestic in self.fans['domestic']:
            if domestic.name == name:
                self.fans['domestic'].remove(domestic)

    def removeStaff(self, name):
        for staff in self.members['staff']:
            if staff.name == name:
                self.members['staff'].remove(staff)

    def removeInternational(self, name):
        for international in self.fans['international']:
            if international.name == name:
                self.fans['international'].remove(international)

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

    def updateDomestic(self, name, favouritePlayer = None, purchasedMerchandise = None, currentCity = None, hasSeasonTickets = None, yearsSinceFan = None):
        for domestic in self.fans['domestic']:
            if domestic.name == name:
                break
        if favouritePlayer != None:
            domestic.setFavouritePlayer(favouritePlayer)
        if purchasedMerchandise != None:
            domestic.setPurchasedMerchandise(purchasedMerchandise)
        if currentCity != None:
            domestic.setCurrentCity(currentCity)
        if hasSeasonTickets != None:
            domestic.updateTicketStatus(hasSeasonTickets)
        if yearsSinceFan != None:
            domestic.yearsSinceFan = yearsSinceFan


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

    def updateInternational(self, name, favouritePlayer = None, purchasedMerchandise = None, currentCity = None, country = None, viewMatches = None):
        for international in self.fans['international']:
            if international.name == name:
                break
        if favouritePlayer != None:
            international.setFavouritePlayer(favouritePlayer)
        if purchasedMerchandise != None:
            international.setPurchasedMerchandise(purchasedMerchandise)
        if currentCity != None:
            international.setCurrentCity(currentCity)
        if country != None:
            international.country = country
        if viewMatches != None:
            international.updateViewMatches(viewMatches)