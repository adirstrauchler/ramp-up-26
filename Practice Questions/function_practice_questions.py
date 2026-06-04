import random as r

def alpha(num):
    while i <= num:
        print(i)
        i += 1

def bravo():
    total = 0
    for i in range(1,11):
        total += i
    return total

def charlie(x):
    for i in x:
        print(i**(1/3.0))

def delta():
    while True:
        age = int(input("what is your age"))
        if age >= 0 and age <=100:
            return age

def echo():
    while i < 20:
        i += 1
        x = r.randint(1,1000)
        with open("theFile.txt", "a") as f:
            f.write(" ", x)

def foxtrot(num):
    return num * 2

def golf():
    return r.randint(1,7)

def hotel():
    turns = 1
    while True:
        die1 = golf()
        die2 = golf()
        if die1 == die2:
            print(turns)
            return
        turns += 1

def india(x):
    for i in x:
        if i % 2 == 0:
            print(0)
        else:
            print(1)
def juliett(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
def kilo(x):
    for i in x:
        with open("theFile.txt", "a") as f:
            f.write(" ", i/2)
def lima(name, age):
    for i in range(3):
        if age < 0 or age > 100:
            print("try agein")
        else:
            return age
    age = 0
    return age
def mike(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

def november(grade):
    if grade >= 89 and grade <=100:
        print("You got an A")
    elif grade >= 80 and grade <=89:
        print("You got an B")
    elif grade >= 70 and grade <=79:
        print("You got an C")
    else:
        print("You did not pass")
        
PAY_RATE = 50
def main():
    run = input("what do you want to run")
    if run == "alpha":
        num = input("what nubmber should we count to?")
        alpha(num)
    if run == "bravo":
        print(bravo())
    if run == "charlie":
        list = [1, 2, 3, 4]
        charlie(list)
    if run == "delta":
        age = delta()
        print(f"you are {age} years old")
    if run == "echo":
        echo()
    if run == "function":
        u = 1
        while i < 10:
            print(u)
            u = foxtrot(i)
            i += 1
    if run == "favorite colour a":
        color = input("what is your favorite color?")
        if color == "blue":
            print("Geate choice.")
        elif color == "red":
            print("Poor choice.")
        elif color == "green":
            print("Not a bad choice.")
        else:
            print("Sorry, that's not a primary color.")
    if run == "favorite colour b":
        color = input("what is your favorite color?")
        match color:
            case "blue":
                print("Geate choice.")
            case "red":
                print("Poor choice.")
            case "green":
                print("Not a bad choice.")
            case _:
                print("Sorry, that's not a primary color.")
    if run == "random":
        num = r.randint(1,101)
        if num < 50:
            print("You chose a number less than 50.")
        if num > 50:
            print("You chose a number more than 50.")
    if run == "vacation":
        hotel()
    if run == "india":
        list = [1, 2, 3, 4]
        india(list)
    if run == "juiett":
        juliett(int(input("pick a num")))
    if run == "kilo":
        list = [1, 2, 3, 4]
        kilo(list)
    if run == "ternary":
        hrs = int(input("how many hours did you work"))
        print(PAY_RATE * hrs if hrs > 10 else 0)
    if run == "lima":
        lima(age=int(input("age")), name=(input("name")))
    if run == "celsius":
        for i in range(-20, 21):
            print("celsius", i, "\tfahrenhiet", (9/5)*i +32)
    if run == "fibonacci":
        this = 1
        last = 1
        while i < 20:
            print(this)
            temp = this
            this += last
            last = temp
            i +=1
    if run == "mike":
        num = 1
        mike(num)
    if run == "november":
        num = 1
        november(num)
if __name__ == "__main__":
    main()