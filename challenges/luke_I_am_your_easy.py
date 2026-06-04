RELATION = {"Darth Vader":"father","Leia":"sister","Han":"brother in law","R2D2":"droid"}
def relation_to_luke(name):
    return f"Luke, I am your {RELATION[name]}"

def main():
    print(relation_to_luke("Darth Vader"))
    print(relation_to_luke("Leia"))
    print(relation_to_luke("Han"))

if __name__ == "__main__":
    main()