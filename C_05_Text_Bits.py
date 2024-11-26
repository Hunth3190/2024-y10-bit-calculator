def calc_text_bites():
    response = input("Enter some text...")
    num_chars = len(response)
    num_bits = num_chars * 8
    answer = f"{response} has {num_chars} characters." \
             f"\nwe meed {num_chars} x 8bits to represent it" \
             f"\nwhich is {num_bits} bits"
    return answer


text_ans = calc_text_bites()
print(text_ans)
