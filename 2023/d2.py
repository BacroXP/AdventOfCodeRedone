
# Read in File and declare Variables
games = open("input.txt").read().strip().split("\n")
solution = 0
solution2 = 0

# Cycle through the rounds
for i, game in enumerate(games):
    red, blue, green = 0, 0, 0
    for round in game.split(": ")[1].split("; "):

        # Get Maximum of the numbers
        for values in round.split(", "):
            value, id = values.split(" ")

            match id:
                case "red":
                    if red < int(value):
                        red = int(value)
                case "blue":
                    if blue < int(value):
                        blue = int(value)
                case "green":
                    if green < int(value):
                        green = int(value)
    
    # Add Possible Match Ids
    if 12 >= red and 13 >= green and 14 >= blue:
        solution += i + 1
    
    # Add the Power of a throw
    solution2 += red * blue * green

print(solution)
print(solution2)
