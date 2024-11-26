29# asks users for file type (integer / image / text/ xxx)
def get_filetype():
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


# main routine goes here
while True:
    file_type = get_filetype()
    print(f"you chose {file_type}")

    if file_type == "xxx":
        break
