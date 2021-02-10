docstring = """ ReverseList
    Submitted by Ye-Hwan Kim
    Submitted: Feb 10, 2021
    Enhancements in this release:
    Experiment with slicing, concatenation, and recursive functions
"""


def print_header():
    """ Print program and author's names """
    print("Recursion and Lists")
    print("Ye-Hwan Kim")


def reverse_a_list(my_list):
    """ Reverse the order of my_list """
    length = len(my_list)
    print(length)
    if length == 1:
        return my_list
    return_value = my_list[length - 1:length] + reverse_a_list(
        my_list[0:length - 1])
    return return_value


def main():
    print_header()
    alphabet = [chr(ascii_value) for ascii_value in
                range(ord("a"), ord("z") + 1)]
    print(alphabet)
    print(reverse_a_list(alphabet))
    print(alphabet)


if __name__ == "__main__":
    main()
