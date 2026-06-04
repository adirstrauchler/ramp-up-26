def number_length(num):
    if num == 0:
        return 1
    return num_length(num, 0)

def num_length(num, length):
    if num < 1:
        return length
    num = num // 10
    return num_length(num, length+1)

def main():
    print(number_length(10))
    print(number_length(5000))
    print(number_length(0))

if __name__ == "__main__":
    main()