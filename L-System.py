if False:
    from lib.Processing3 import *

start_string = 'A'
result_string = ''
number_of_generation = 5


def setup():
    global start_string
    global result_string
    global number_of_generation

    size(512, 512)
    background(51)
    stroke(255)

    for _ in range(number_of_generation):
        for i in start_string:
            if i == 'A':
                result_string = result_string + 'AB'
            elif i == 'B':
                result_string = result_string + 'B'
            else:
                result_string = result_string + i
        start_string = result_string
    print(start_string)
