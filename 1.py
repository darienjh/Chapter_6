def ask_number(guess, tries, answer):
    while guess != answer:
        if guess > answer:
            tries += 1
            guess = int(input("Enter a lower number"))
        elif guess < answer:
            tries += 1
            guess = int(input("Enter a higher number"))
        else:
            print("invalid answer; You suck. ")
        tries += 1
        return tries
