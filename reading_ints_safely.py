def read_int(prompt, min, max):
    prompt = input("Enter your number: ")

    user_fail = True
    while user_fail:
        try:
            prompt = int(prompt)
            if prompt < min or prompt > max:
                print("Error: the value is not within permitted range(", min, max, ")")
                prompt = input("Enter your number: ")
            else:
                user_fail = False

        except ValueError:
            print("You have failed to enter an integer, try again")
            prompt = input("Enter your number: ")

    return prompt


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
