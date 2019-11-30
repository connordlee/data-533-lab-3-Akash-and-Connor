#!/usr/bin/env python
# coding: utf-8

# In[27]:


import unittest
from club import club
from club.member.member import member

class TestMember(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initializing members with changes
        cls.vazquez = member('Roberto Vazquez', 'Spain', 3200000, 1)
        cls.zidane = member('Zinedine Zidane', 'France', 5500000, 9)
        
    def setUp(self):
        # Initializing members to be reset each time
        self.ramos = member('Sergio Ramos', 'Spain', 15000000, 14)
        self.benzema = member('Karim Benzema', 'France', 7920000, 10)

    @classmethod
    def tearDownClass(cls):
        # Deleting Members created in setUpClass
        del cls.zidane
        del cls.vazquez

    def tearDown(self):
        # Deleting Members created in setUp
        del self.ramos
        del self.benzema

    def test_updateNationality(self):
        # Updating the nationalities for the members
        self.ramos.updateNationality('Spanish')
        self.benzema.updateNationality('French')
        self.vazquez.updateNationality('Spanish')
        self.zidane.updateNationality('French')
        # Testing that the nationalities updated (4 assertions)
        self.assertEqual(self.ramos.nationality,'Spanish')
        self.assertEqual(self.benzema.nationality, 'French')
        self.assertEqual(self.vazquez.nationality,'Spanish')
        self.assertEqual(self.zidane.nationality, 'French')
        # Testing that the nationalities are all of type string (4 assertions)
        self.assertIsInstance(self.ramos.nationality, str)
        self.assertIsInstance(self.benzema.nationality, str)
        self.assertIsInstance(self.vazquez.nationality, str)
        self.assertIsInstance(self.zidane.nationality, str)
        
    def test_setSalary_getSalary(self):
        # Setting the salaries to something new for the members
        self.ramos.setSalary(1)
        self.benzema.setSalary(2)
        self.vazquez.setSalary(3)
        self.zidane.setSalary(4)
        # Testing that the setSalary worked and that the getSalary pulls the correct information (4 assertions)
        self.assertEqual(self.ramos.getSalary(), 1)
        self.assertEqual(self.benzema.getSalary(), 2)
        self.assertEqual(self.vazquez.getSalary(), 3)
        self.assertEqual(self.zidane.getSalary(), 4)
        # Testing that the getSalary method pulls integers
        self.assertIsInstance(self.ramos.getSalary(), int)
        self.assertIsInstance(self.benzema.getSalary(), int)
        self.assertIsInstance(self.vazquez.getSalary(), int)
        self.assertIsInstance(self.zidane.getSalary(), int)

    def test_newYear(self):
        # Storing temporary variables for years before running newYear method
        ramosYrs = self.ramos.yearsWClub
        benzemaYrs = self.benzema.yearsWClub
        vazquezYrs = self.vazquez.yearsWClub
        zidaneYrs = self.zidane.yearsWClub
        # Running the newYear method
        self.ramos.newYear()
        self.benzema.newYear()
        self.vazquez.newYear()
        self.zidane.newYear()
        # Testing if the new year method increased the value by 1 (4 assertions)
        self.assertEqual(self.ramos.yearsWClub, ramosYrs+1)
        self.assertEqual(self.benzema.yearsWClub, benzemaYrs+1)
        self.assertEqual(self.vazquez.yearsWClub, vazquezYrs+1)
        self.assertEqual(self.zidane.yearsWClub, zidaneYrs+1)
        # Testing if the new year method keeps data as integer (4 assertions)
        self.assertIsInstance(self.ramos.yearsWClub, int)
        self.assertIsInstance(self.benzema.yearsWClub, int)
        self.assertIsInstance(self.vazquez.yearsWClub, int)
        self.assertIsInstance(self.zidane.yearsWClub, int)

unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:




