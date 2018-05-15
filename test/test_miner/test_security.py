'''
Created on 15.05.2018

@author: Mirco
'''

# path hack
import sys, os
dirname = os.path.dirname(__file__)
print(dirname)
src_dirname = dirname.replace('test/test_miner', 'src')
print(src_dirname)
sys.path.insert(0, os.path.abspath(src_dirname))

# sys.path.insert(0, os.path.abspath('E:\git-repositories\stock-data-miner\src'))


import unittest
from miner.security import Security, SecurityDataMinerBloomberg

class TestSecurity(unittest.TestCase):

    def setUp(self):
        self.stock = Security('E.On', 'EOAN')
        self.stock.price = 10
        self.stock.book = 250
        self.stock.shares_outstanding = 50


    def test_get_P_to_B(self):
        self.assertEqual(self.stock.get_P_to_B(), 0.04)

    def test_get_B_to_P(self):
        self.assertEqual(self.stock.get_B_to_P(), 25)
        
    def test_get_market_cap(self):
        self.assertEqual(self.stock.get_market_cap(), 500)
        
    def test_get_B_to_M(self):
        self.assertEqual(self.stock.get_B_to_M(), 0.5)
        
class TestSecurityDataMinerBloomberg(unittest.TestCase):
    
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'bloomberg-eoan-2018-05-15.html')
    file = open(filename, 'r')
    html_example = file.read()
    file.close()
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.miner = SecurityDataMinerBloomberg('')
        
    
    def test___parse_human_readable_number_to_int(self):
        self.assertEqual(1200000000, self.miner._SecurityDataMinerBloomberg__parse_human_readable_number_to_int('1.2B'))
        self.assertEqual(2300000, self.miner._SecurityDataMinerBloomberg__parse_human_readable_number_to_int('2.3M'))

    def test_mine_price(self):
        self.miner.update_html_soup(TestSecurityDataMinerBloomberg.html_example)
        self.assertEqual(self.miner.mine_price(), 9.29)
        
    def test_mine_price_to_book(self):
        self.miner.update_html_soup(TestSecurityDataMinerBloomberg.html_example)
        self.assertEqual(self.miner.mine_price_to_book(), 4.5789)
        
    def test_mine_shares_outstanding(self):
        self.miner.update_html_soup(TestSecurityDataMinerBloomberg.html_example)
        self.assertEqual(self.miner.mine_shares_outstanding(), 2.2 * 10**9)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()