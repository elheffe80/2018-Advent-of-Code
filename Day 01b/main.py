import os

number = 0
frequent_numbers = [number]
found = False

while not found:
    with open("\\Users\\bheffron\\Nextcloud\\Projects\\2018-Advent-of-Code\\Day 01b\\input.txt") as input_text:
        for line in input_text:
            number = number + int(line)

            if number in frequent_numbers:
                print("answer: " + str(number))
                found = True
                break
            frequent_numbers.append(number)
