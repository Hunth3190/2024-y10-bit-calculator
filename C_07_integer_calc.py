# Ask user for width and loop until they
# enter a number that is more than zero
def int_check(question, low):
    error = f"please enter a number that is more than {low}\n"
    while True:

        # get input and check it's a number smore than 'low'
        try:
            response = int(input(question))

            if response >= low:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


def integer_calc():
    integer = int_check("Integer: ", 0)

    raw_binary = bin(integer)

    binary = raw_binary[2:]
    num_bits = len(binary)

    answer = f"{integer} in binary is {binary}. We ned {num_bits} to represent it."

    return answer


image_ans = integer_calc()
print(image_ans)
