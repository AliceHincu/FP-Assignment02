from math import sqrt

# ----- UI section ------
# write all functions that have input or print statements here


def read_real_part():
    '''
    Reads the real part of the complex number that was written
    :return: The real part of the complex number (type:int)
    '''

    while True:
        try:
            real_part = int(input("Write the real part of the number: "))
            return real_part
        except ValueError:
            print("Oops! This is not a natural number! Try again!")


def read_imaginary_part():
    '''
    Read the imaginary part of the complex number that was written
    :return: The imaginary part of the complex number (type:int)
    '''

    while True:
        try:
            imaginary_part = int(input("Write the imaginary part of the number: "))
            return imaginary_part
        except ValueError:
            print("Oops! This is not a natural number! Try again!")


def print_menu():
    '''
    Shows the available commands
    :return: Nothing
    '''

    print("\nWelcome! Here are the available commands:")
    print('\t+: adds a new complex number at the final of the list')
    print('\tadd list: adds multiple complex numbers at the final of the list')
    print('\t\tCondition: The real and imaginary parts have to be from Z')
    print('\tshow: shows the current list of complex numbers')
    print('\tFor displaying on the console the longest sequence that observes a given property:')
    print('\t\tp1: The difference between the modulus of consecutive numbers is a prime number.')
    print('\t\tp2: Sum of its elements is 10+10i ')
    print('\t\tCondition: The sequence has to have at least two numbers')
    print('\texit: exit this program')
    print('\t ---- optionals ----')
    print('\t-: delete a current complex number at the desired position')
    print('\tmodify: modifies a current complex number at the desired position')
    print('\thelp: shows the menu instructions again')


def read_command():
    '''
    Reads the command that the person wants to do and checks if it is good.
    :return: The command (type: string)
    '''
    list_of_commands = ['+', '-', 'modify', 'show', 'help', 'exit', 'p1', 'p2', 'add list']
    while True:
        try:
            command = input("\nWrite the command: ")
            if command in list_of_commands:
                return command
            else:
                raise ValueError
        except ValueError:
            print("Oops! That was not a valid command! Please try again (write help if you are stuck): ")


def say_goodbye():
    '''
    Displays a goodbye message when the program is done ^-^
    :return: Nothing
    '''

    print("Goodbye! I hope you enjoyed it!")


def show_list(list):
    '''
    Shows the list of complex numbers
    :param list: The list of complex numbers (type: list)
    :return: Nothing
    '''

    print("\nHere are the complex numbers:")
    if not list:
        print("The list is empty!")
    else:
        for i in range(len(list)):
            re = list[i][0]
            im = list[i][1]
            if re == 0:
                if im == 0:
                    print('\tZ' + str(i) + '= 0')
                else:
                    print('\tZ' + str(i) + ' = ' + str(im) + 'i')
            elif im == 0:
                print('\tZ' + str(i) + ' = ' + str(re))
            else:
                print('\tZ' + str(i) + ' = ' + str(re) + '+' + str(im) + 'i')


def print_delete_error():
    '''
    It's called when you can't delete an element because the list is empty
    :return: Nothing
    '''
    print("Oops! You can't delete a number from an empty list!")


def print_modify_error():
    '''
    It's called when you can't modify an element because the list is empty
    :return: Nothing
    '''
    print("Oops! You can't modify a number from an empty list!")


def read_delete_position(len):
    '''
    It checks if the position is a natural number smaller than the length of list.
    :param len: The position that was written (type: int)
    :return: The position that was written (type: int)
    '''

    while True:
        try:
            poz = int(input("From what position do you want the number to be deleted?(The counting starts from 0): "))
            if poz < 0 or poz >= len:
                raise ValueError
            else:
                return poz
        except ValueError:
            print("Oops! That was either not a natural number or a number which is bigger than the length! Try again: ")


def print_number(i):
    '''
    Displays what number are we reading
    :param i: the index of the number (type: int)
    :return: Nothing
    '''
    print("\nNumber " + str(i+1) + ':')


def read_index():
    '''
    Read how many numbers do we want to add
    :return: how many numbers do we want to add
    '''
    while True:
        try:
            index = int(input("How many numbers do you want to read: "))
            if index <= 0:
                raise ValueError
            else:
                return index
        except ValueError:
            print("Oops! That was not a valid natural number! Try again: ")


def read_modify_position(len):
    '''
    It checks if the position is a natural number smaller than the length of list.
    :param len: The position that was written (type: int)
    :return: The position that was written (type: int)
    '''

    while True:
        try:
            poz = int(input("From what position do you want the number to be modified?(The counting starts from 0): "))
            if poz < 0 or poz >= len:
                raise ValueError
            else:
                return poz
        except ValueError:
            print("Oops! That was either not a natural number or a number which is bigger than the length! Try again: ")


def show_list_p(list, index):
    '''
    It prints the list of the longest sequence which respects a certain property
    :param list: the list of the longest sequence (type: list)
    :param index: from where the sequence starts in the original list (type: int)
    :return: Nothing
    '''
    if not list:
        print("The list is empty!")
    else:
        for i in range(len(list)):
            re = list[i][0]
            im = list[i][1]
            if re == 0:
                if im == 0:
                    print('\tZ' + str(index + i) + '= 0')
                else:
                    print('\tZ' + str(index + i) + ' = ' + str(im) + 'i')
            elif im == 0:
                print('\tZ' + str(index + i) + ' = ' + str(re))
            else:
                print('\tZ' + str(index + i) + ' = ' + str(re) + '+' + str(im) + 'i')


def display_list(list, index):
    '''
    Shows the list of complex numbers that respects the property
    :param list: The list of complex numbers that respects the property (type: list)
    :param index: From where the sequence starts (type: int)
    :return: Nothing
    '''

    print("\nHere is the longest list of complex numbers that respects the property:")
    if not list:
        print("\nThe list is either empty or it does not respect the property/condition!")
    else:
        show_list_p(list, index)


# ----- Function section -----


def read_number():
    '''
    Read the complex number that was written
    :return: The complex number (type: list)
    '''

    real_part = read_real_part()
    imaginary_part = read_imaginary_part()
    complex_number = [real_part, imaginary_part]
    return complex_number


def get_real(number):
    '''
    Returns the real part of the complex number
    :param number: The complex number (type: list)
    :return: The real part of the number (type: int)
    '''

    return number[0]


def get_imaginary(number):
    '''
    Returns the imaginary part of the complex number
    :param number: The complex number (type: list)
    :return: The imaginary part of the number (type: int)
    '''

    return number[1]


def set_real(number, x):
    '''
    It changes the real part of the number
    :param number: The complex number (type: list)
    :param x: The new value for the real part (type: int)
    :return: The new number (type: list)
    '''

    number[0] = x
    return number


def set_imaginary(number, x):
    '''
    It changes the imaginary part of the number
    :param number: The complex number (type: list)
    :param x: The new value for the real part (type: int)
    :return: The new number (type: list)
    '''

    number[1] = x
    return number


def add_number(list_complex):
    '''
    Adds a new complex number to the list
    :param list_complex: The list of complex numbers (type: list)
    :return: Nothing
    '''

    complex_number = read_number()
    list_complex.append(complex_number)


def add_list(list_complex):
    '''
    We add multiple complex numbers
    :param list_complex: the list of complex numbers (type: list)
    :return: Nothing
    '''
    index = read_index()
    for i in range(index):
        print_number(i)
        add_number(list_complex)


def delete_number(list):
    '''
    It deletes a number from the list
    :param list: The list of complex numbers (type: list)
    :return: Nothing
    '''

    if not list:
        print_delete_error()
    else:
        length = len(list)
        poz = read_delete_position(length)
        del list[poz]


def modify_number(list):
    '''
    Modifies the value of a number from the list
    :param list: The list of complex numbers (type: list)
    :return: Nothing
    '''

    if not list:
        print_modify_error()
    else:
        length = len(list)
        poz = read_modify_position(length)
        r = read_real_part()
        i = read_imaginary_part()
        set_real(list[poz], r)
        set_imaginary(list[poz], i)


def find_module(number):
    '''
    It calculates the module of the complex number
    :param number: The complex number (type: list)
    :return: The module (type: float)
    '''
    r = get_real(number)
    i = get_imaginary(number)
    module = sqrt(r ** 2 + i ** 2)
    return module


def verify_if_prime(value):
    '''
    Verifies if the number is prime. If it is type float => not prime
    :param value: The number that has to be checked (type: float)
    :return: true -> it is prime; false -> it is not prime; (type: bool)
    '''
    if not value.is_integer():
        return False
    if value == 0 or value == 1:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    value_root = int(sqrt(value))
    for divisor in range(3, value_root+1, 2):
        if value % divisor == 0:
            return False
    return True


def check_property_1(list):
    '''
    It makes a list of the numbers' modules.
    Then, it checks if the difference between two consecutive modules is a prime number
    It creates a new list which tells us what numbers respect the property.
    1 means the number and the next number from the list are respecting the property.
    :param list: The list of complex numbers (type: list)
    :return: The list that tells us which numbers respects the property (type: list)
    '''
    length = len(list)
    list_modules = []
    for i in range(length):  # i calculate the modules
        list_modules.append(find_module(list[i]))

    list_property = []
    for i in range(length-1):  # i check if the difference is a prime nr
        dif = abs(list_modules[i] - list_modules[i+1])
        if verify_if_prime(dif):
            list_property.append(1)
        else:
            list_property.append(0)
    list_property.append(0)
    return list_property


def do_property_1(list):
    '''
    Returns the longest subsequence that checks the following property:
    -The difference between the modulus of consecutive numbers is a prime number.
    :param list: the list of complex numbers (type: list)
    :return: the longest subsequence (type: list)
    '''
    p1 = check_property_1(list)
    max_length = 0
    max_p1 = []
    max_index = 0

    for i in range(len(p1)):
        p1_final = []
        if p1[i]:
            p1_final.append(list[i])

            for j in range(i + 1, len(p1)):
                if p1[j]:
                    p1_final.append(list[j])
                else:
                    p1_final.append(list[j])
                    break

            if len(p1_final) > max_length:
                max_p1 = p1_final
                max_length = len(p1_final)
                max_index = i
    display_list(max_p1, max_index)


def do_property_2(list):
    '''
    Returns the longest subsequence that checks the following property:
    -Sum of its elements is 10+10i
    :param list: the list of complex numbers (type: list)
    :return: the longest subsequence (type: list)
    '''
    max_length = 0
    max_index = 0
    p2_final = []
    for i in range(len(list)):
        s_i = get_imaginary(list[i])
        s_r = get_real(list[i])
        length = 1
        for j in range(i+1, len(list)):
            s_i += get_imaginary(list[j])
            s_r += get_real(list[j])
            length += 1
            if s_i == 10 and s_r == 10:
                if length > max_length:
                    p2_final = []
                    for k in range(i, j+1):
                        p2_final.append(list[k])
                    max_length = len(p2_final)
                    max_index = i
            elif s_i > 10 or s_r > 10:
                break
    display_list(p2_final, max_index)


def do_command(cmd, list_complex):
    '''
    It executes the command
    :param cmd: The command that was chosen (type: string)
    :param list_complex: The list of complex numbers (type: list)
    :return: Nothing
    '''

    if cmd == 'exit':
        say_goodbye()
    elif cmd == '+':
        add_number(list_complex)
    elif cmd == 'add list':
        add_list(list_complex)
    elif cmd == 'show':
        show_list(list_complex)
    elif cmd == 'help':
        print_menu()
    elif cmd == '-':
        delete_number(list_complex)
    elif cmd == 'modify':
        modify_number(list_complex)
    elif cmd == 'p1':
        do_property_1(list_complex)
    elif cmd == 'p2':
        do_property_2(list_complex)


if __name__ == '__main__':
    print_menu()
    list_complex = [[7, 0], [0, 5], [3, 0], [7, 8], [3, 4], [3, 0], [4, 3], [0, 3], [4, 3], [0, 4]]
    # list_complex =[[9, 1], [1, 9], [3, 4], [3, 0], [4, 3], [0, 3], [0, 2], [7, 8], [2, 4], [3, 3]]
    # list_complex = [[1,1]]
    done = False
    while not done:
        cmd = read_command()
        do_command(cmd, list_complex)
        if cmd == 'exit':
            done = True
