#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        number = ""
        if i % 15 == 0:
            number = "FizzBuzz"
        elif i % 3 == 0:
            number = "Fizz"
        elif i % 5 == 0:
            number = "Buzz"
        print(number, end=" ") if number else print(i, end=" ")
