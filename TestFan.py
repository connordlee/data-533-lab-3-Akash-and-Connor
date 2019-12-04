#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
from club import club
from club.fan.fan import fan

class TestFan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initializing members with changes
        cls.connor = fan("Connor Lee", "Sergio Ramos", 5, "Kelowna")
        cls.akash = fan("Akash Dhatavkar", "Leo Messi", 5, "Kelowna")
        
    def setUp(self):
        # Initializing members to be reset each time
        self.joe = fan("Joe Miller", "Eden Hazard", 5, "London")
        self.jane = fan("Jane Doe", "Sergio Ramos", 5, "Kelowna")

    @classmethod
    def tearDownClass(cls):
        # Delete SetUpClass
        del cls.connor
        del cls.akash

    def tearDown(self):
        # Delete SetUp 
        del self.joe
        del self.jane

    def test_getFavouritePlayer_setFavouritePlayer(self):
        # Set New Favourite Player
        self.connor.setFavouritePlayer("Virgil Van Dijk")
        self.akash.setFavouritePlayer("Cristiano Ronaldo")
        self.joe.setFavouritePlayer("Sadio Mane")
        self.jane.setFavouritePlayer("Mo Salah")
        # Test setFavouritePlayer using the getFavouritePlayer 
        self.assertEqual(self.connor.getFavouritePlayer(), "Virgil Van Dijk")
        self.assertEqual(self.akash.getFavouritePlayer(), "Cristiano Ronaldo")
        self.assertEqual(self.joe.getFavouritePlayer(), "Sadio Mane")
        self.assertEqual(self.jane.getFavouritePlayer(), "Mo Salah")
        # Test to check Instance is correct
        self.assertIsInstance(self.connor.getFavouritePlayer(), str)
        self.assertIsInstance(self.akash.getFavouritePlayer(), str)
        self.assertIsInstance(self.joe.getFavouritePlayer(), str)
        self.assertIsInstance(self.jane.getFavouritePlayer(), str)
        
    def test_getPurchaseMerchandise_setPurchaseMerchandise(self):
        # Set Purchase Merchandise
        self.connor.setPurchasedMerchandise(7)
        self.akash.setPurchasedMerchandise(4)
        self.joe.setPurchasedMerchandise(9)
        self.jane.setPurchasedMerchandise(3)
        # Test setPurchaseMerchandise using the getPurchaseMerchandise 
        self.assertEqual(self.connor.getPurchasedMerchandise(), 7)
        self.assertEqual(self.akash.getPurchasedMerchandise(), 4)
        self.assertEqual(self.joe.getPurchasedMerchandise(), 9)
        self.assertEqual(self.jane.getPurchasedMerchandise(), 3)
        # Test to check Instance is correct
        self.assertIsInstance(self.connor.getPurchasedMerchandise(), int)
        self.assertIsInstance(self.akash.getPurchasedMerchandise(), int)
        self.assertIsInstance(self.joe.getPurchasedMerchandise(), int)
        self.assertIsInstance(self.jane.getPurchasedMerchandise(), int)

    def test_getCurrentCity_setCurrentCity(self):
        # Set New Favourite Player
        self.connor.setCurrentCity("Vancouver")
        self.akash.setCurrentCity("Paris")
        self.joe.setCurrentCity("Geneva")
        self.jane.setCurrentCity("San Francisco")
        # Test setPurchaseMerchandise using the getPurchaseMerchandise 
        self.assertEqual(self.connor.getCurrentCity(), "Vancouver")
        self.assertEqual(self.akash.getCurrentCity(), "Paris")
        self.assertEqual(self.joe.getCurrentCity(), "Geneva")
        self.assertEqual(self.jane.getCurrentCity(), "San Francisco")
        # Test to check Instance is correct
        self.assertIsInstance(self.connor.getCurrentCity(), str)
        self.assertIsInstance(self.akash.getCurrentCity(), str)
        self.assertIsInstance(self.joe.getCurrentCity(), str)
        self.assertIsInstance(self.jane.getCurrentCity(), str)

unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:




