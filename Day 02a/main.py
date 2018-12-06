three_count = 0
two_count = 0

with open("\\Users\\bheffron\\Nextcloud\\Projects\\2018-Advent-of-Code\\Day 02a\\input.txt") as input_text:
    for line in input_text:
        letter_dict = {}
        for letter in line:
            if letter in letter_dict:
                letter_dict[letter] = letter_dict[letter] + 1
            else:
                letter_dict[letter] = 1
        print(letter_dict)
        if [v for (k,v) in letter_dict.items() if v ==  2]:
            two_count = two_count + 1
        if [v for (k, v) in letter_dict.items() if v == 3]:
            three_count = three_count + 1
    print("Answer is " + str(two_count) + " * " + str(three_count) + ": " + str(two_count * three_count))