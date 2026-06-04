def tallest_skyscraper(list):
    tallest = 0
    # test each biulding
    for biulding in range(len(list[0])):
        count = 0
        # check each floor
        for floor in range(len(list)):
            # begin at lowest floor
            if not list[len(list) - floor - 1][biulding] == 0:
                count += 1
            # if floor doest exist move on to next biulding
            else:
                break
        tallest = max(tallest, count)
    return tallest

def main():
    print(tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]))
    print(tallest_skyscraper([
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]))
    print(tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
])
)
if __name__ == "__main__":
    main()