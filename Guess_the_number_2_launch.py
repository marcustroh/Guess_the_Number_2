
user_begin = input("""Welcome to Guess the Number 2!

Figure out the number in range 0 - 1000 and I will try to guess it!

Please type in OK to begin!
""")

if user_begin == 'OK' or 'ok':
    None

min = 0
max = 1000

pc_try = 1
while pc_try < 10:
    guess = int((max - min) / 2 + min)
    print(f"I am guessing: {guess}")
    print("""Am I right?
    1. Yes?
    2. No?""")
    user_option = input("What is your answer? Please select the option and press enter: ")
    if user_option == "1":
        print("I Won!")
        break
    elif user_option == "2":
        print("""Is it to high?
    1. Yes
    2. No""")
        user_option = input("What is your answer? Please select the option and press enter: ")
        if user_option == "1":
            max = guess
            pc_try = pc_try + 1
        elif user_option == "2":
            print("""Is it too low?
    1. Yes
    2. No""")
            user_option = input("What is your answer? Please select the option and press enter: ")
            if user_option == "1":
                min = guess
                pc_try = pc_try + 1
            elif user_option == "2":
                print("Do not lie!")
            else:
                print("Incorrect value - please enter 1 or 2 and press enter")
        else:
            print("Incorrect value - please enter 1 or 2 and press enter")
    else:
        print("Incorrect value - please enter 1 or 2 and press enter")

print("""You Won! 
I have used all af my 10 attempts..
Thanks for playing!""")
