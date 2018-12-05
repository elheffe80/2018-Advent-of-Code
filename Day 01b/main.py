import os

number = 0
frequent_numbers = [number]
found = False

while not found:
    with open("\\Users\\bheffron\\Nextcloud\\Projects\\Advent of Code 2018\\Day 02\\input.txt") as input_text:
        for line in input_text:
            number += int(line)

            if str(number) in frequent_numbers:
                print("answer: " + number)
                found = True
                break
            frequent_numbers.append(line)
            print(number)
        #print(str(number))
print("this is a test")