#!/usr/bin/env python
# coding: utf-8

# In[6]:


import unittest
from club import club
from club.fan.fantype import domestic, international

class TestFanType(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initializing domestic 
        cls.connor = domestic("Connor Lee", "Sergio Ramos", 5, "Madrid", True, 8)
        cls.joe = domestic("Joe Miller", "Eden Hazard", 7, "Valencia", False, 12)
        # Initializing international
        cls.akash = international("Akash Dhatavkar", "Leo Messi", 4, "Kelowna", "Canada", "TV")
        cls.jane = international("Jane Doe", "Marco Reus", 8, "San Francisco", "US", "Online")
        
    def setUp(self):
        # Initializing Club Info For Testing
        dlist = [self.connor.asList(), self.joe.asList()]
        ilist = [self.akash.asList(), self.jane.asList()]
        self.madrid = club.club(domesticList = dlist, internationalList = ilist)

    @classmethod
    def tearDownClass(cls):
        # Deleting Staff and Player Objects
        del cls.connor
        del cls.akash
        del cls.joe
        del cls.jane

    def tearDown(self):
        # Deleting Club Object
        del self.madrid

    def test_updateTicketStatus(self):
        # Testing Update Ticket Status
        self.madrid.fans["domestic"][0].updateTicketStatus(False)
        self.madrid.fans["domestic"][1].updateTicketStatus(True)
        self.assertFalse(self.madrid.fans["domestic"][0].hasSeasonTickets, False)
        self.assertTrue(self.madrid.fans["domestic"][1].hasSeasonTickets, True)
        # Testing update domestic independent of club 
        self.connor.updateTicketStatus(True)
        self.joe.updateTicketStatus(False)
        self.assertEqual(self.connor.hasSeasonTickets, True)
        self.assertEqual(self.joe.hasSeasonTickets, False)
        # Testing that assertIs works on the updated domestic 
        self.assertIs(self.connor.hasSeasonTickets, True)
        self.assertIs(self.joe.hasSeasonTickets, False)
        
    def test_updateViewMatches(self):
        # Testing Update View Matches
        self.madrid.fans["international"][0].updateViewMatches("Online")
        self.madrid.fans["international"][1].updateViewMatches("TV")
        self.assertEqual(self.madrid.fans["international"][0].viewMatches, "Online")
        self.assertEqual(self.madrid.fans["international"][1].viewMatches, "TV")
        # Testing update international independent of club 
        self.akash.updateViewMatches("TV")
        self.jane.updateViewMatches("Online")
        self.assertEqual(self.akash.viewMatches, "TV")
        self.assertEqual(self.jane.viewMatches, "Online")
        # Testing that assertIs works on the updated players (2 assertions)
        self.assertIs(self.akash.viewMatches, "TV")
        self.assertIs(self.jane.viewMatches, "Online")

    def test_asList(self):
        # Running the asList function on one player and one staff
        connorList = self.connor.asList()
        akashList = self.akash.asList()
        # Testing that the output is of type list (2 assertions)
        self.assertIsInstance(connorList, list)
        self.assertIsInstance(akashList, list)
        # Testing that information in lists are correct (4 assertions)
        self.assertEqual(connorList[0], "Connor Lee")
        self.assertEqual(connorList[5], 8)
        self.assertEqual(akashList[1], "Leo Messi")
        self.assertEqual(akashList[2], 4)

unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:




