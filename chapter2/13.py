import sys

def show_first_n_lines(filename, N):
   
    with open(filename, "r") as f:
        for i, line in enumerate(f):
            if i >= N:
                break
            print(line.replace('\t', ' '), end='')

if __name__ == "__main__":
    filename = "/Users/sarangoobattsogt/nlp_100_knocks/chapter2/popular-names.txt"
    N = 10  
    show_first_n_lines(filename, N)
