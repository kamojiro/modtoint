#import sys
#input = sys.stdin.readline
import modtoint
import unittest
from math import gcd

class TestModToInt(unittest.TestCase):
    def test_smallcase(self):
        Q = 10**9+7
        root = int( Q**(1/2))
        smallcase = int( Q**(1/4))
        invs = []
        for i in range(root+1):
            invs.append(pow(i,Q-2,Q))
        for i in range(1,smallcase):
            for j in range(1,smallcase):
                t = gcd(i,j)
                value = str(i//t) + "/" + str(j//t)
                estimated = modtoint.get_original(i*invs[j]%Q, Q, root)
                self.assertEqual(value,estimated)

    # almost 1 minites
    def test_denominator_smallcase(self):
        Q = 10**9+7
        root = int( Q**(1/2))
        smallcase = int( Q**(1/4))
        invs = []
        for i in range(root+1):
            invs.append(pow(i,Q-2,Q))
        for i in range(1,root):
            for j in range(1,smallcase):
                t = gcd(i,j)
                value = str(i//t) + "/" + str(j//t)
                estimated = modtoint.get_original(i*invs[j]%Q, Q, root)
                self.assertEqual(value,estimated)


if __name__ == '__main__':
    unittest.main()
