filename = 'pi_digits.txt'

# Making a list from a file
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())