#!/usr/bin/env python
# coding: utf-8

# In[8]:


import unittest
from club import club
from club.member.membertypes import player, staff

class TestClub(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Temproary variables to be stored into the club
        ramos = player('Sergio Ramos', 'Spain', 15000000, 14, 'Right Back', 15)
        benzema = player('Karim Benzema', 'French', 7920000, 10, 'Striker', 9)
        vazquez = staff('Roberto Vazquez', 'Spain', 3200000, 1, 'Goalkeeping Coach')
        zidane = staff('Zinedine Zidane', 'France', 5500000, 9, 'Skipper')
        plist = [ramos.asList(), benzema.asList()]
        slist = [vazquez.asList(), zidane.asList()]
        # Initializing club with 2 players and 2 staff
        cls.madrid = club.club(plist, slist)
        
    def setUp(self):
        # Initializing members to be reset each time
        self.p1 = player('Player 1', 'Knowhere', 4000000, 5, 'Midgard', 42)
        self.p2 = player('Player 2', 'Canada', 8300000, 7, 'Center Mid', 22)
        self.s1 = staff('Staff 1', 'Spain', 63000, 23, 'Groundskeeper')
        self.s2 = staff('Staff 2', 'Spain', 83000, 3, 'Accountant')


    @classmethod
    def tearDownClass(cls):
        # Deleting the club
        del cls.madrid

    def tearDown(self):
        # Deleting Members created in setUp
        del self.p1
        del self.s1
        del self.p2
        del self.s2

    def test_addPlayer(self):
        # Temporary variable to track original length of list
        origLen = len(self.madrid.members['players'])
        # Adding new player to the club
        name, nationality, salary, yearsWClub, position, jersey = self.p1.asList()
        self.madrid.addPlayer(name, nationality, salary, yearsWClub, position, jersey)
        # Assertions to confirm length change and info update (4 assertions)
        self.assertEqual(len(self.madrid.members['players']), origLen+1)
        self.assertEqual(self.madrid.members['players'][origLen].name, 'Player 1')
        self.assertEqual(self.madrid.members['players'][origLen].nationality, 'Knowhere')
        self.assertEqual(self.madrid.members['players'][origLen].getSalary(), 4000000)
        # Adding new player to the club
        name, nationality, salary, yearsWClub, position, jersey = self.p2.asList()
        self.madrid.addPlayer(name, nationality, salary, yearsWClub, position, jersey)
        # Assertions to confirm length change and info update (4 assertions)
        self.assertEqual(len(self.madrid.members['players']), origLen+2)
        self.assertEqual(self.madrid.members['players'][origLen+1].yearsWClub, 7)
        self.assertEqual(self.madrid.members['players'][origLen+1].position, 'Center Mid')
        self.assertEqual(self.madrid.members['players'][origLen+1].jersey, 22)
        
    def test_addStaff(self):
        # Temporary variable to track original length of list
        origLen = len(self.madrid.members['staff'])
        # Adding new player to the club
        name, nationality, salary, yearsWClub, title = self.s1.asList()
        self.madrid.addStaff(name, nationality, salary, yearsWClub, title)
        # Assertions to confirm length change and info update (4 assertions)
        self.assertEqual(len(self.madrid.members['staff']), origLen+1)
        self.assertEqual(self.madrid.members['staff'][origLen].name, 'Staff 1')
        self.assertEqual(self.madrid.members['staff'][origLen].nationality, 'Spain')
        self.assertEqual(self.madrid.members['staff'][origLen].getSalary(), 63000)
        # Adding new player to the club
        name, nationality, salary, yearsWClub, title = self.s2.asList()
        self.madrid.addStaff(name, nationality, salary, yearsWClub, title)
        # Assertions to confirm length change and info update (4 assertions)
        self.assertEqual(len(self.madrid.members['staff']), origLen+2)
        self.assertEqual(self.madrid.members['staff'][origLen+1].yearsWClub, 3)
        self.assertEqual(self.madrid.members['staff'][origLen+1].title, 'Accountant')
        
        
###########################################################################################
#############              NOTE: This needs 1 more assertion              #################
###########################################################################################
    def test_removePlayer(self):
        # Temporary variable to track original length of list
        origLen = len(self.madrid.members['players'])
        # Delete first player
        self.madrid.removePlayer('Sergio Ramos')
        # Assertions to verify new list length (1 assertion)
        self.assertEqual(len(self.madrid.members['players']), origLen-1)
        # For Loop to get list of remaining players then assertion to check if player still in list (1 assertion)
        remainingPlayers = []
        for player in self.madrid.members['players']:
            remainingPlayers.append(player.name)
        self.assertNotIn('Sergio Ramos', remainingPlayers)
        # Delete Second player
        self.madrid.removePlayer('Karim Benzema')
        # Assertions to verify new list length (1 assertion)
        self.assertEqual(len(self.madrid.members['players']), origLen-2)
        # For Loop to get list of remaining players then assertion to check if player still in list (1 assertion)
        remainingPlayers = []
        for player in self.madrid.members['players']:
            remainingPlayers.append(player.name)
        self.assertNotIn('Sergio Ramos', remainingPlayers)


###########################################################################################
#############              NOTE: This needs 1 more assertion              #################
###########################################################################################
    def test_removeStaff(self):
        # Temporary variable to track original length of list
        origLen = len(self.madrid.members['staff'])
        # Delete first Staff Member
        self.madrid.removeStaff('Roberto Vazquez')
        # Assertions to verify new list length (1 assertion)
        self.assertEqual(len(self.madrid.members['staff']), origLen-1)
        # For Loop to get list of remaining staff then assertion to check if staff still in list (1 assertion)
        remainingStaff = []
        for staff in self.madrid.members['staff']:
            remainingStaff.append(staff.name)
        self.assertNotIn('Roberto Vazquez', remainingStaff)
        # Delete first Staff Member
        self.madrid.removeStaff('Zinedine Zidane')
        # Assertions to verify new list length (1 assertion)
        self.assertEqual(len(self.madrid.members['staff']), origLen-2)
        # For Loop to get list of remaining staff then assertion to check if staff still in list (1 assertion)
        remainingStaff = []
        for staff in self.madrid.members['staff']:
            remainingStaff.append(staff.name)
        self.assertNotIn('Zinedine Zidane', remainingStaff)
        
    def test_updatePlayer(self):
        # Code to test updating each player attribute individually
        self.madrid.updatePlayer('Player 1', nationality='Spain') # Updating nationality
        self.madrid.updatePlayer('Player 1', salary=15000000) # Updating Salary
        self.madrid.updatePlayer('Player 1', yearsWClub=14) # Updating yearsWClub
        self.madrid.updatePlayer('Player 1', position='Right Back') # Updating position
        self.madrid.updatePlayer('Player 1', jersey=15) # Updating jersey        
        # Code to test updating all player attributes at the same time
        self.madrid.updatePlayer('Player 2', 'French', 7920000, 10, 'Striker', 9)
        # Assertions to verify that the individual changes occured as expected (5 assertions)
        self.assertEqual(self.madrid.members['players'][0].nationality, 'Spain')
        self.assertEqual(self.madrid.members['players'][0].getSalary(), 15000000)
        self.assertEqual(self.madrid.members['players'][0].yearsWClub, 14)
        self.assertEqual(self.madrid.members['players'][0].position, 'Right Back')
        self.assertEqual(self.madrid.members['players'][0].jersey, 15)
        # Assertions to verify that the bulk changes occured as expected (5 assertions)
        self.assertEqual(self.madrid.members['players'][1].nationality, 'French')
        self.assertEqual(self.madrid.members['players'][1].getSalary(), 7920000)
        self.assertEqual(self.madrid.members['players'][1].yearsWClub, 10)
        self.assertEqual(self.madrid.members['players'][1].position, 'Striker')
        self.assertEqual(self.madrid.members['players'][1].jersey, 9)
        
    def test_updateStaff(self):
        # Code to test updating each staff attribute individually
        self.madrid.updateStaff('Staff 1', nationality='Spain') # Updating nationality
        self.madrid.updateStaff('Staff 1', salary=3200000) # Updating Salary
        self.madrid.updateStaff('Staff 1', yearsWClub=1) # Updating yearsWClub
        self.madrid.updateStaff('Staff 1', title='Goalkeeping Coach') # Updating position     
        # Code to test updating all staff attributes at the same time
        self.madrid.updateStaff('Staff 2', 'France', 5500000, 9, 'Skipper')
        # Assertions to verify that the individual changes occured as expected (4 assertions)
        self.assertEqual(self.madrid.members['staff'][0].nationality, 'Spain')
        self.assertEqual(self.madrid.members['staff'][0].getSalary(), 3200000)
        self.assertEqual(self.madrid.members['staff'][0].yearsWClub, 1)
        self.assertEqual(self.madrid.members['staff'][0].title, 'Goalkeeping Coach')
        # Assertions to verify that the bulk changes occured as expected (4 assertions)
        self.assertEqual(self.madrid.members['staff'][1].nationality, 'France')
        self.assertEqual(self.madrid.members['staff'][1].getSalary(), 5500000)
        self.assertEqual(self.madrid.members['staff'][1].yearsWClub, 9)
        self.assertEqual(self.madrid.members['staff'][1].title, 'Skipper')

unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:




