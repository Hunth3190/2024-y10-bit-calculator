def statement_generator(statement, decoration):
    print(f"{decoration * 5} {statement} {decoration * 5}")


def instructions():
    statement_generator("instructions", "-")

    print('''
Instructions go here.
-instruction 1
-instruction 2
-etc   
     ''')


def get_filetype():
    """asks users for file type (integer / image / text/ xxx)"""

    while True:
        response = input("file type: ").lower()

        if response == "xxx" or response == "i":
            return response

        elif response in ['integer', 'int']:
            return "integer"

        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        elif response in ["text", 'txt', 't']:
            return "text"

        else:
            print("please enter a valid file type")


want_instructions = input("press <enter> to read the instructions "
                          "or any key to continue")

if want_instructions == "":
    instructions()

# main routine goes here
while True:
    file_type = get_filetype()

    if file_type == 'i':

        want_image = input("Press <enter> for an integer or any key for an image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"you chose {file_type}")

    if file_type == "xxx":
        break
