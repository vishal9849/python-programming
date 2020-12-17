# 1 First 10 natural numbers using while loop
def first_n_numbers(user_input):
    output = 0
    while user_input > 0:
        print(output)
        output += 1
        user_input -= 1


usr_inp = 10
first_n_numbers(usr_inp)


# 2 Pattern
def space(n=10):
    gap = ''
    while n > 0:
        gap += ' '
        n -= 1
    return gap


def pattern(user_input):
    constant = 1
    count = 1
    space_gap = 10
    while count <= user_input:
        temp = 1
        while temp <= count:
            print(temp, end=' ')
            temp += 1
        space_op = space(space_gap)
        print(space_op, constant)
        count += 1
        space_gap -= 2
        space(space_gap)


usr_inp = 4
pattern(usr_inp)


# Sum of all the numbers between 1 and user given number
def sum_of_numbers(inp=10):
    num_list = list(range(1, inp + 1))
    print(sum(num_list))


user_input = 10
sum_of_numbers(user_input)


# Multiplication table of a given number
def mul_table(n=5):
    op_list = [n * i for i in range(1, 11)]
    for num in op_list:
        print(num)


user_input = 2
mul_table(user_input)


# Finding the elements divisible by 5
def divisible_by_five(inp_list):
    output = [num for num in inp_list if num % 5 == 0]
    for num in output:
        if num <= 150:
            print(num)


user_input = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
divisible_by_five(user_input)


# To find the total digits in a number
def total_digits(inp_num):
    print(len(str(inp_num)))


user_input = 75869
total_digits(user_input)


# 7 pattern
def pattern_n(num):
    while num > 0:
        temp_list = [i for i in range(1, num + 1)]
        for n in temp_list[::-1]:
            print(n, end=' ')
        num -= 1
        print()
        print()


user_input = 5
pattern_n(user_input)


# Revering a given list
def revere_list(inp_num, length_of_list):
    while length_of_list >= 0:
        print(inp_num[length_of_list])
        length_of_list -= 1


user_input = [10, 20, 30, 40, 50]
length = len(user_input) - 1
revere_list(user_input, length)

# Display "Done" end of the loop
for i in range(0, 2):
    print(i)
print("Done")


# Fibonacci series up to 10 terms
def fib_n(inp_elem, total_elem):
    n = total_elem - len(inp_elem)
    start = inp_elem[0]
    prev = inp_elem[1]
    output_list = []
    while n > 0:
        total = prev + start
        output_list.append(total)
        start = prev
        prev = total
        n -= 1
    inp_elem.extend(output_list)

    for item in inp_elem:
        print(item, end=' ')


start_elem = [0, 1]
n_elem = 10
fib_n(start_elem, n_elem)


# Factorial of a given number
def fact_of_n(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    print(fact)


usr_input = 10
fact_of_n(usr_input)


# Displaying prime number between a range
def ret_prime(start, stop):
    flag = 1
    prime_list = []
    list_items = [i for i in range(start_inp, stop_inp + 1)]
    for num in list_items:
        temp_list = [i for i in range(2, (num // 2) + 1)]
        for item in temp_list:
            if num % item == 0:
                flag = 0
        if flag == 1:
            prime_list.append(num)
        flag = 1
    print("Prime numbers between", start, "and", stop, "are:")
    for item in prime_list:
        print(item)


start_inp = 25
stop_inp = 40
ret_prime(start_inp, stop_inp)
