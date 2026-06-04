def calculate_age():
    for i in range(3):
        name = input("what is your name ")
        age = input("how old are you ")
        if name.isalpha() and age.isdigit():
            years = int(age)
            if years > 1 and years < 100:
                print("\"Acceptable\" ")
                return
        print("try again ")
    print("\"Unacceptable\" ")

if __name__ == "__main__":
    calculate_age()