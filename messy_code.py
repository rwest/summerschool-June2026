import os
import sys


x = {  'a':1,'b':2 ,'c':3}


def  add_all( a,b ,c ):
    total = 0
    return     a+b+ c


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]


def greet(name='world'):
    print( "hello, "+name+'!' )
    return None


def repeat(text: str, times: int) -> str:
    return text * times


# mypy flags this BEFORE the program ever runs:
message: str = repeat("hi", "four")  # "times" expects int, got str
message2: str = repeat("hello", 3.1415
                       )
