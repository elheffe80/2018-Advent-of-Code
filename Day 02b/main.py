def find_close(to_be_matched: str, string_file):
    """
    Hope to make a recursive looping thingy that will find a closely matched string
    :param to_be_matched: String value to be matched against list & list itself
    :return: True or False value based on matching tuple containing 1 value
    """
    for line_item in string_file:
        index_of_item = [index for index, (a, b) in enumerate(zip(to_be_matched, line_item)) if a != b]
        if index_of_item != 1:
            print("internal if loop")
            find_close(line_item, string_file)
        else:
            print("Answer: " + line_item)
            return True
    return False

answer = False
with open("\\Users\\bheffron\\Nextcloud\\Projects\\2018-Advent-of-Code\\Day 02b\\input.txt") as input_text:
    while answer == False:
        for line in input_text:
            answer = find_close(line, input_text)
            print("external for loop")

