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


# ask user for width (3 times for testing purposes)
for item in range(0, 2):
    width = int_check("How many pixels wide: ", 1)
    print(width)

    print()

for item in range(0, 2):
    height = int_check("Height: ", 1)
    print(height)

for item in range(0, 2):
    integer_value = int_check("What is your favourite integer", 0)
