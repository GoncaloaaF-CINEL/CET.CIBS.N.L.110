import unittest

import utils

class MyTestCase(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(6, utils.soma(1,5))
        self.assertRaises(TypeError, utils.soma)

    """
    + +
    + -
    - +
    - - 
    0 +
    0 -
    - 0
    + 0
    
    l +
    l -
    - l
    + l
    
    
    
    """

    def test_fresol(self):
        self.assertSetEqual({3.0, 2.0}, set(utils.fresolv(1,-5,6)))

    def test_fresol_eq(self):
        self.assertSetEqual({2.0, 2.0}, set(utils.fresolv(1,-4,4)))








    def test_ip_valid(self):
        for o1 in range(1, 256):
            for o2 in range(0, 256):
                       # print(o1, o2, o3, o4)
                        self.assertTrue(utils.idIpValid(f"{o1}.{o2}.{0}.{0}"))









    def test_ip_invalid(self):
        self.assertFalse(utils.idIpValid("256.0.0.1"))


if __name__ == '__main__':
    unittest.main()
