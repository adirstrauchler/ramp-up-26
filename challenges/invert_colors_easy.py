def color_invert(color):
    return invert(color[0]), invert(color[1]), invert(color[2])

def invert(num):
    return (255 - num) % 256

def main():
    print(color_invert((255, 255, 255)))
    print(color_invert((0, 0, 0)))
    print(color_invert((165, 170, 221)))

if __name__ == "__main__":
    main()