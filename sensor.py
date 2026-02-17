sensor_readings = [3, 4, 7, 8, 10, 12, 5]
valid = []
for i, reading in enumerate(sensor_readings):
    if reading % 2 == 0:
        valid.append((i, reading))
print("Valid sensor readings (hour, value):", valid)