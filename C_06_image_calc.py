# Ask user for width and loop until they
# enter a number that is more than zero
def int_check(question, low):
    error = f"please enter a number that is more than {low}\n"
    while True:

        # get input and check it's a number more than 'low'
        try:
            response = float(input(question))

            if response >= low:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


def image_calc():
    width = int_check("Width: ", 1)
    height = int_check("Height: ", 1)
    print(height)

    num_pixels = width * height
    num_bits = num_pixels * 24

    answer = f"Number of pixals: {width} x {height} = {num_pixels} " \
             f"\nNumber of bits {num_pixels} x 24 = {num_bits}"

    return answer

image_ans = image_calc()
print(image_ans)