 # lab02Tests.py    Tests for lab02, UCSB CS8, P. Conrad, 04/14/2014

                  # this is so we can set up testing of functions

# the imports below import the functions we want to test

from lab02Funcs import perimRect
from lab02Funcs import isList
from lab02Funcs import isAdditivePrimaryColor
from lab02Funcs import isSimpleNumeric
from lab02Funcs import areaRect
from lab02Funcs import *
  # This is how you do testing in Python

    # Every test case should be a function definition
    # The name should start with test_ and the parameter should be "self".
    # Then, you can write tests using self.assertEqual(actual, expected) and 
    # self.assertAlmostEquals(actual, expected, numberOfDecimalPlaces)
    #
    # If an answer should be exact (e.g. integer math), use assertEqual
    # If an answer is approximate (floating pt math, square roots, pi, etc.)
    #    use assertAlmostEqual

def test_perimRect1():
        assert(perimRect(2,3) == 10)

def test_perimRect2():
        assert(perimRect(4,2.5) == 13.0, 2) 
        # accurate to two decimal places

def test_perimRect3():
        assert(perimRect(3,3) == 12)

    ### @@@ TODO @@@ 
    ### ADD THREE TEST CASES for areaRect here.
def test_areaRect():
        assert(areaRect(2, 2) == 4)
def test_areaRect():
        assert(areaRect(2, 2.5) == 5)
def test_areaRect():
        assert(areaRect(4, 4) == 16)


    ###


def test_isList1():
        assert( isList(3) ==  False)

def test_isList2():
        assert( isList([3])==   True)

def test_isList3():
        assert( isList([5,10,15,20])==  True)

def test_isList4():
        assert( isList("foo")==   False)

def test_isList5():
        assert( isList(["John","Paul","Ringo","George"])==   True)

def test_isList6():
        assert( isList([])== True)


    ### @@@ HERE, WRITE FOUR TEST CASES FOR isString
    ### @@@   one for a string of length 0, 
    ### @@@   one for a string of length 4,
    ### @@@   two values that are not strings.

def test_isString():
        assert(isString("","","","","")== True)
def test_isString():
        assert(isString(5434234324) == False)
def test_isString():
        assert(isString([]) == False)
        
    # tests for isPrimaryColor

def test_isPrimaryColor1():
        assert( isAdditivePrimaryColor("blue")== True)
#def test_isPrimaryColor1andahalf():
#        assert( test_isPrimaryColor1andahalf("green") == False)

def test_isPrimaryColor2():
        assert( isAdditivePrimaryColor("black")==    False)

def test_isPrimaryColor3():
        assert( isAdditivePrimaryColor(42)==    False)


    # tests for isSimpleNumeric

def test_isSimpleNumeric1():
        assert( isSimpleNumeric(5)==   True)

def test_isSimpleNumeric2():
        assert( isSimpleNumeric(3.5)==   True)

def test_isSimpleNumeric3():
        assert( isSimpleNumeric("5")==   False)

def test_isSimpleNumeric4():
        assert( isSimpleNumeric([5])==   False)

def test_isSimpleNumeric5():
        assert( isSimpleNumeric(6.0221415E23)==   True)
   
# This code says: when you run this file, run the tests!

#if __name__ == '__main__':
#    unittest.main(exit=False)

#if __name__ == "__main__":
#    pytest.main()


