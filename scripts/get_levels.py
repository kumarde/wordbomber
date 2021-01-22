import sys
import math

LEVELS = ["easy", "medium", "hard"]

def read_ngram_distribution(f):
    out = []
    for l in open(f, 'r'):
        l = l.strip()
        out.append(l)
    return out

def get_level_indices(ngram_list):
    total = len(ngram_list)
    # Easy from 0 – 30%
    easy = (0, math.floor(total * 0.3))
    # Medium from 30 – 50%
    medium = (math.floor(total * 0.3) + 1, math.floor(total * 0.5))
    # Hard from 50 – 100%
    hard = (math.floor(total * 0.5) + 1, math.floor(total * 0.8))
    return [easy, medium, hard]

def write_levels(n_level, n):
    for i, level in enumerate(LEVELS):
        ngrams = n_level[i]
        with open("data/"+str(n)+"_"+level+".csv", 'w') as ofile:
            for gram in ngrams:
                ofile.write(gram + "\n")

def get_levels(level_indices, grams):
    out = []
    for i, level in enumerate(LEVELS):
        indices = level_indices[i]
        out.append(grams[indices[0]:indices[1]])
    return out

def main():
    twogram_f = sys.argv[1]
    threegram_f = sys.argv[2]

    two_grams = read_ngram_distribution(twogram_f)
    three_grams = read_ngram_distribution(threegram_f)

    two_indices = get_level_indices(two_grams)
    three_indices = get_level_indices(three_grams)
   
    two_levels = get_levels(two_indices, two_grams)
    three_levels = get_levels(three_indices, three_grams)

    write_levels(two_levels, 2)
    write_levels(three_levels, 3)


if __name__ == "__main__":
    main()
