def sec_to_hours(t):
    hours = int(t//3600) #need to convert t into seconds first
    remaining_sec = t%3600
    minutes = remaining_sec //60
    seconds = remaining_sec % 60

    return hours, minutes, seconds

print(sec_to_hours(90541))