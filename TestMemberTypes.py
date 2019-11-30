#!/usr/bin/env python
# coding: utf-8

# In[12]:


import unittest
from club import club
from club.member.membertypes import player, staff

class TestMemberTypes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initializing Staff for testing
        cls.zidane = staff('Zinedine Zidane', 'France', 5500000, 9, 'Skipper')
        cls.vazquez = staff('Roberto Vazquez', 'Spain', 3200000, 1, 'Goalkeeping Coach')
        # Initial izing Players for testing
        cls.ramos = player('Sergio Ramos', 'Spain', 15000000, 14, 'Right Back', 15)
        cls.benzema = player('Karim Benzema', 'French', 7920000, 10, 'Striker', 9)
        
    def setUp(self):
        # Initializing Club Info For Testing
        plist = [self.ramos.asList(), self.benzema.asList()]
        slist = [self.zidane.asList(), self.vazquez.asList()]
        self.madrid = club.club(plist, slist)

    @classmethod
    def tearDownClass(cls):
        # Deleting Staff and Player Objects
        del cls.zidane
        del cls.vazquez
        del cls.ramos
        del cls.benzema

    def tearDown(self):
        # Deleting Club Object
        del self.madrid

    def test_updatePosition(self):
        # Testing Updating Players stored inside a club (2 assertions)
        self.madrid.members['players'][0].updatePosition('Center Back')
        self.madrid.members['players'][1].updatePosition('Left Right Out')
        self.assertEqual(self.madrid.members['players'][0].position,'Center Back')
        self.assertEqual(self.madrid.members['players'][1].position, 'Left Right Out')
        # Testing updating players independent of club (2 assertions)
        self.ramos.updatePosition('Bench Warmer')
        self.benzema.updatePosition('Forward')
        self.assertEqual(self.ramos.position, 'Bench Warmer')
        self.assertEqual(self.benzema.position, 'Forward')
        # Testing that assertIs works on the updated players (2 assertions)
        self.assertIs(self.ramos.position, 'Bench Warmer')
        self.assertIs(self.benzema.position, 'Forward')
        
    def test_updateJerseyNum(self):
        # Testing Updating Players stored inside a club (2 assertions)
        self.madrid.members['players'][0].updateJerseyNum(0)
        self.madrid.members['players'][1].updateJerseyNum(9)
        self.assertEqual(self.madrid.members['players'][0].jersey,0)
        self.assertEqual(self.madrid.members['players'][1].jersey, 9)
        # Testing updating players independent of club (2 assertions)
        self.ramos.updateJerseyNum(40000000)
        self.benzema.updateJerseyNum(-43)
        self.assertEqual(self.ramos.jersey, 40000000)
        self.assertEqual(self.benzema.jersey, -43)
        # Testing that assertIs works on the updated players (2 assertions)
        self.assertIs(self.ramos.jersey, 40000000)
        self.assertIs(self.benzema.jersey, -43)
        
    def test_updateTitle(self):
        # Testing Updating Players stored inside a club (2 assertions)
        self.madrid.members['staff'][0].updateTitle('Manager')
        self.madrid.members['staff'][1].updateTitle('Keeper Keeper')
        self.assertEqual(self.madrid.members['staff'][0].title,'Manager')
        self.assertEqual(self.madrid.members['staff'][1].title, 'Keeper Keeper')
        # Testing updating players independent of club (2 assertions)
        self.zidane.updateTitle('Bench Warmer')
        self.vazquez.updateTitle('Forward')
        self.assertEqual(self.zidane.title, 'Bench Warmer')
        self.assertEqual(self.vazquez.title, 'Forward')
        # Testing that assertIs works on the updated players (2 assertions)
        self.assertIs(self.zidane.title, 'Bench Warmer')
        self.assertIs(self.vazquez.title, 'Forward')

    def test_asList(self):
        # Running the asList function on one player and one staff
        ramosList = self.ramos.asList()
        zidaneList = self.zidane.asList()
        # Testing that the output is of type list (2 assertions)
        self.assertIsInstance(ramosList, list)
        self.assertIsInstance(zidaneList, list)
        # Testing that information in lists are correct (4 assertions)
        self.assertEqual(ramosList[0], 'Sergio Ramos')
        self.assertEqual(ramosList[5], 15)
        self.assertEqual(zidaneList[1], 'France')
        self.assertEqual(zidaneList[2], 5500000)

unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:




