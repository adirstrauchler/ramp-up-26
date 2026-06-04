def ave_spd(time_up, speed_up, speed_down):
    distance = (speed_up/60)*time_up
    time_down = (distance/speed_down)*60
    total_distance = distance*2
    total_time = time_up + time_down
    ave_speed = (total_distance / total_time)*60
    return int(ave_speed)

def main():
    print(ave_spd(18, 20, 60))
    print(ave_spd(30, 10, 30))
    print(ave_spd(30, 8, 24))
if __name__ == "__main__":
    main()