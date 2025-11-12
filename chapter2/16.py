import random

filename = "/Users/sarangoobattsogt/nlp_100_knocks/chapter2/popular-names.txt"
output_file = "shuffled_popular-names.txt"


with open(filename, "r") as f:
    lines = f.readlines()


random.shuffle(lines)


with open(output_file, "w") as f:
    f.writelines(lines)

print(output_file)

