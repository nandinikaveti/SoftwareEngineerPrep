def time_conversions(t):
    hours = t//3600
    print(hours)
    remaining_minutes = t % 3600
    minutes = remaining_minutes // 60
    print(minutes)
    remaining_seconds = remaining_minutes % 60
    print(remaining_seconds)



time_conversions(9001)