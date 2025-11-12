import sys

def get_variety(file):
    col1_set = {l.strip().split("\t")[0] for l in file}
    return len(col1_set)

def main():
    
    filename = "/Users/sarangoobattsogt/nlp_100_knocks/chapter2/popular-names.txt"
    with open(filename, "r") as file:
        print(get_variety(file))

if __name__ == "__main__":
    main()