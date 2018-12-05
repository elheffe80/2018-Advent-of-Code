import math

input_text = open("\\Users\\bheffron\\Nextcloud\\Projects\\Advent of Code 2018\\Puzzle 01\\input.txt","r")
answer = 0
for line in input_text:
    answer = answer + int(line)
print(answer)
