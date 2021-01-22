import sys
import operator

def word2ngrams(text, n=3):
  """ Convert word into character ngrams. """
  return [text[i:i+n] for i in range(len(text)-n+1)]

def main():
    dictionary = sys.argv[1]

    num_words = 0
    twogram_to_count = {}
    threegram_to_count = {}
    
    for l in open(dictionary, 'r'):
        l = l.strip()
        twograms = word2ngrams(l, 2)
        for gram in twograms:
            twogram_to_count[gram] = twogram_to_count.get(gram, 0) + 1
        threegrams = word2ngrams(l, 3)
        for gram in threegrams:
            threegram_to_count[gram] = threegram_to_count.get(gram, 0) + 1
        num_words += 1

    sorted_two_grams = sorted(twogram_to_count.items(), key=operator.itemgetter(1), reverse=True)
    sorted_three_grams = sorted(threegram_to_count.items(), key=operator.itemgetter(1), reverse=True)

    with open("data/2gram_distribution.csv", 'w') as ofile:
        for gram, count in sorted_two_grams:
            frac = float(count)/num_words
            ofile.write(gram + " " + str(count) + " " + str(frac) + "\n")
    
    with open("data/3gram_distribution.csv", 'w') as ofile:
        for gram, count in sorted_three_grams:
            frac = float(count)/num_words
            ofile.write(gram + " " + str(count) + " " + str(frac) + "\n")

if __name__ == "__main__":
    main()

