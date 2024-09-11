
# Read in File and declare Variables
lines = open("input.txt").read().strip().split("\n")
replaces = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e",
            "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e", "zero": "z0o"}


def getSolution(lines):
    nums = []

    for line in lines:
        line = line.strip()
        first_digit = None
        last_digit = None

        # Iterating over each character in the line
        for char in line:
            if char.isdigit():
                if first_digit is None:
                    first_digit = char
                last_digit = char

        # Getting the wanted format of number
        if first_digit is not None and last_digit is not None:
            nums.append(int(first_digit + last_digit))

    # Calculate the wanted solution
    print(sum(nums))


# First solution without replacements
getSolution(lines)

# Replace written-out numbers with digits
replaced_lines = []
for line in lines:
    for replace in replaces:
        line = line.replace(replace, replaces[replace])
    replaced_lines.append(line)

# Solution after replacements
getSolution(replaced_lines)
