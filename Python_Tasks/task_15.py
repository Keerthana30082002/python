def sum_numbers(*args):
    return sum(args)


def concat_strings(*args):
    return "".join(args)


def print_info(*args, **kwargs):
    print("Positional arguments: ", args)
    print("Keyword Arguments: ", kwargs)


numbers_sum = sum_numbers(1, 2, 3, 4, 5)
print("Sum of numbers: ", numbers_sum)
string = concat_strings("Hello", " ", "world", "!")
print("Concatenated Strings: ", string)
print_info(10, "Orange", name="Keerthu", age=21)
