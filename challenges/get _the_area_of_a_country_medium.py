WORLD_LANDMAS = 148940000
def area_of_country(country, area):
    percent_of_world = area/WORLD_LANDMAS
    return f"{country} is {percent_of_world:.2%} of the total world's landmass"

def main():
    print(area_of_country("Russia", 17098242))
    print(area_of_country("USA", 9372610))
    print(area_of_country("Iran", 1648195))
    
if __name__ == "__main__":
    main()