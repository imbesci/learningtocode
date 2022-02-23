import math
def area(base, height):
    '''(number, number)-> number

Finds the area of a triangle with the base and the height'''
    return base*height/2

def square_return(num):
    return num**2
def square_print(num):
    print("The square of num is", "num **2")


def celciusconv(f):
    '''(float)->float
Returns the temperature in celcius from a parameter in Fahrenheit.'''
    return (f-32)*5/9

def perimeter(s1, s2, s3):
    return s1+s2+s3

def semiperimeter(s1,s2,s3):
    '''(float)(float)(float)->float
Returns half the perimeter of a triangle using the float values of the 3 side lengths.'''
    return perimeter(s1, s2, s3)/2

def area_hero(side1, side2, side3):
    '''(number, number, number)-> float'''
    semi= semiperimeter(side1, side2, side3)
    areahero = (semi*(semi-side1)*(semi-side2)*(semi-side3))
    areaherosq = math.sqrt(areahero)
    return areaherosq

    
