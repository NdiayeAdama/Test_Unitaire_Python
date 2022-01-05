import main
import unittest


class TestUtils(unittest.TestCase):
    def test_checkPwd(self):
        self.assertTrue(main.checkPwd("Fatima2204#*2022"))
        self.assertTrue(main.checkPwd("AminateBalde1251#23"))
        self.assertTrue(main.checkPwd("Celloubalde05011994#29"))


    def test_checkPwd2(self):
        self.assertTrue(main.checkPwd("Camilledelacourt25#23"))
        #self.assertFalse(main.checkPwd("12Fatima2204#*23"))
        #self.assertFalse(test.checkPwd("CamilleDeLacour"))
        #self.assertTrue(test.checkPwd("ami"))



if __name__ == '__main__':
    unittest.main()