#!/usr/bin/env python
# coding: utf-8

# In[2]:


import unittest

from TestMemberTypes import TestMemberTypes
from TestMember import TestMember
from TestFanType import TestFanType
from TestFan import TestFan

from TestClub import TestClub


def TestSuiteClub():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestMemberTypes))
    suite.addTest(unittest.makeSuite(TestMember))
    suite.addTest(unittest.makeSuite(TestFanType))
    suite.addTest(unittest.makeSuite(TestFan))
    suite.addTest(unittest.makeSuite(TestClub))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
TestSuiteClub()


# In[ ]:




