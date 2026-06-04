def print_numbers():
    for i in range(1000):
        u = i
        while u > 1:
            if u % 10 == 3:
                print(str(i), end = " | ")
                break
            u //= 10
if __name__ == "__main__":
    print_numbers()