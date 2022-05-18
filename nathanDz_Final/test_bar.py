import unittest
from bar import *
# Objects:
alc_test_1 = Alcohol("Vodka", 45)       # Alcohol Test 1
alc_test_2 = Alcohol("Teqilla", 50)     # Alcohol Test 2
alc_test_3 = Alcohol("Everclear", 95)   # Alcohol Test 3

garn_test_1 = Garnish("Lime", 1)        # Garnish Test 1
garn_test_2 = Garnish("Orange", 1)      # Garnish Test 2
garn_test_3 = Garnish("Mint", 3)        # Garnish Test 3

top_test_1 = Topper("GingerBeer", False)#  Topper Test 1
top_test_2 = Topper("RedBull", False)   #  Topper Test 2
top_test_3 = Topper("Club Soda", False) #  Topper Test 3

mix_test_1 = MixedDrinks("Mix1",alc_test_1,1,garn_test_1,top_test_1,1,1)

class Test_Bar(unittest.TestCase):
    def testAlcohol_1_(self):
        ans = alc_test_1.getAlcType()
        correct = "Vodka"
        self.assertEqual(ans,correct)
    def testAlcohol_2_(self):
        ans = alc_test_2.getProof()
        correct = 50
        self.assertEqual(ans,correct)
    def testAlcohol_3_(self):
        ans = alc_test_3.getAlcType()
        correct = "Everclear"
        self.assertEqual(ans,correct)
    
    def testGarnish_1_(self):
        ans = garn_test_1.getGarnType()
        correct = "Lime"
        self.assertEqual(ans,correct)
    def testGarnish_2_(self):
        ans = garn_test_2.getAmmount()
        correct = 1
        self.assertEqual(ans,correct)
    def testGarnish_3_(self):
        ans = garn_test_3.getGarnType()
        correct = "Mint"
        self.assertEqual(ans,correct)
    
    def testTopper_1_(self):
        ans = top_test_1.getTopType()
        correct = "GingerBeer"
        self.assertEqual(ans,correct)
    def testTopper_2_(self):
        ans = top_test_2.getContainsLiquor()
        correct = False
        self.assertEqual(ans,correct)
    def testTopper_3_(self):
        ans = top_test_3.getTopType()
        correct = "Club Soda"
        self.assertEqual(ans,correct)

    def testMixedDrink_1_(self):
        ans = mix_test_1.getDrinkName()
        correct = "Mix1"  
        self.assertEqual(ans,correct)
    def testMixedDrink_2_(self):
        ans = mix_test_1.getAlc()
        correct = alc_test_1
        self.assertEqual(ans,correct)     
    def testMixedDrink_3_(self):
        ans = mix_test_1.getAfOZ()
        correct = 1
        self.assertEqual(ans,correct)
    def testMixedDrink_4_(self):
        ans = mix_test_1.getGarn()
        correct = garn_test_1
        self.assertEqual(ans,correct)
    def testMixedDrink_5_(self):
        ans = mix_test_1.getTop()
        correct = top_test_1
        self.assertEqual(ans,correct)
    def testMixedDrink_6_(self):
        ans = mix_test_1.getTfOZ()
        correct = 1
        self.assertEqual(ans,correct)
    def testMixedDrink_7_(self):
        ans = mix_test_1.getPrice()
        correct = 1
        self.assertEqual(ans,correct)
    def testMixedDrink_8_(self):
        ans = mix_test_1.getDrink()
        correct = "Mix1"
        self.assertEqual(ans,correct)
    def testMixedDrink_9_(self):
        ans = mix_test_1.getTop()
        correct = top_test_1
        self.assertEqual(ans,correct)

if __name__ == "__main__":
    unittest.main(verbosity=2)
