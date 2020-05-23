import pickle
import sys
import math


def load_unigram_model():
    MODEL_FILE_NAME = 'unigram.pkl'
    return pickle.load(open(MODEL_FILE_NAME, 'rb'))


def test_unigram_model(filename, unigram_model):
    """
    Print out the entropy and coverage given the testing file 
    and trained unigram model
    """
    lambda_unknown = 0.05
    lambda_known = 1 - lambda_unknown
    V = 1e6
    W = 0
    H = 0
    unknown_count = 0

    with open(filename) as f:
        for line in f:
            words = line.strip().split(' ')
            words.append('</s>')

            for word in words:
                W += 1
                prob = lambda_unknown / V
                if word in unigram_model:
                    prob += lambda_known * unigram_model[word]
                else:
                    unknown_count += 1
                H += -math.log2(prob)

        print(f'entropy = {H / W}')
        print(f'coverage = {(W - unknown_count) / W}')


def main(argv):
    if len(argv) != 2:
        raise Exception('Usage: python test-unigram.py <filename>')

    # load unigram model
    unigram_model = load_unigram_model()

    # test and print
    test_unigram_model(sys.argv[1], unigram_model)


if __name__ == '__main__':
    main(sys.argv)
