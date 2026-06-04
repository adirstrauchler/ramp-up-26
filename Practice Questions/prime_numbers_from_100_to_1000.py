def print_numbers():
    for i in range(100, 1000):
        if is_prime(i):
            print(str(i) + " | ", end = "")
def is_prime(num):
    for i in range(2, num -1):
        if num % i == 0:
            return False
    return True
if __name__ == "__main__":
    print_numbers()