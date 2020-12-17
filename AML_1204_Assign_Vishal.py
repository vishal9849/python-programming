import math
import random


# Part-1) The simplest encryption algorithm!
def caesar_cypher(user_input, num_rotations):
    enc_alp = tuple()
    for alp in user_input:
        if alp.isalpha():
            enc_alp += (chr(ord(alp) + num_rotations),)
        elif alp.isnumeric():
            enc_alp += (str(int(alp) + num_rotations),)
    return ''.join(enc_alp)


user_inp = input("Enter a string:")
num_rot = int(input("Enter the number for rotating:"))
print(caesar_cypher(user_inp, num_rot))


# Part-2) Binary Search Algorithm Implementation in Python
def bin_search(inp_list, num_to_search):
    inp_list.sort()
    print("Sorted List", inp_list)
    high = len(inp_list) - 1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if num_to_search == inp_list[mid]:
            print("Element Found")
            return True
        elif num_to_search > inp_list[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False


input_list = [item + 3 for item in range(5)]
random.shuffle(input_list)
print("Input List", input_list)
num_to_find = int(input("Enter a number: "))
print(bin_search(input_list, num_to_find))


# Part-3) Formula Implementation
def estimate_pi():
    constant = (2 * math.sqrt(2)) / 9801
    summation = 0
    k = 0
    output = 0
    while output < 10 ** -15:
        summation += math.factorial(4 * k) * (1103 + (26390 * k)) / \
                         ((math.factorial(k) ** 4) * (396 ** (4 * k)))

        k += 1
        output = constant * summation
    return 1/output


print(estimate_pi())
