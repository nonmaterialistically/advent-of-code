file = open('input.txt', 'r')
Lines = file.readlines()

longitude = 0
latitude = 0
currentdegrees = 0

M = list()
for line in Lines:
    M.append(line)

for line in M:
    action = line.strip()[0]
    value = int(line.strip()[1:])
    if action == "N":
        longitude += value
    elif action == "S":
        longitude -= value
    elif action == "E":
        latitude += value
    elif action == "W":
        latitude -= value
    elif action == "L":
        currentdegrees -= int(value)
    elif action == "R":
        currentdegrees += int(value)
    elif action == "F":
        if currentdegrees%360 == 270:     #north
            longitude += value
        elif currentdegrees%360 == 90:    #south
            longitude -= value
        elif currentdegrees%360 == 0:     #east
            latitude += value
        elif currentdegrees%360 == 180:   #ovest
            latitude -= value
print("Part one:", abs(latitude)+abs(longitude))

longitude = 0
latitude = 0
waypointlon = 1
waypointlat = 10

for line in M:
    action = line.strip()[0]
    value = int(line.strip()[1:])
    if action == "N":
        waypointlon += value
    elif action == "S":
        waypointlon -= value
    elif action == "E":
        waypointlat += value
    elif action == "W":
        waypointlat -= value
    elif action == "L":
        if value == 180:
            waypointlon, waypointlat = -waypointlon, -waypointlat
        elif value == 90:
            waypointlon, waypointlat = waypointlat, -waypointlon
        elif value == 270:
            waypointlon, waypointlat = -waypointlat, waypointlon
    elif action == "R":
        if value == 180:
            waypointlon, waypointlat = -waypointlon, -waypointlat
        elif value == 90:
            waypointlon, waypointlat = -waypointlat, waypointlon
        elif value == 270:
            waypointlon, waypointlat = waypointlat, -waypointlon
    elif action == "F":
        for _ in range(value):
            longitude += waypointlon
            latitude += waypointlat
print("Part two:", abs(latitude)+abs(longitude))