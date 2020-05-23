import sys
import pickle


def train_unigram_model(filename):
    '''
    Train a unigram model from a text file.
    And save the trained model to a pickle format as default!
    '''
    word_count_dict = {}
    total_count = 0
    unigram_model = {}

    with open(filename) as f:
        for line in f:
            # split line into an array of words
            words = line.strip().split(' ')
            # append '</s>' to the end of words
            words.append('</s>')

            for word in words:
                if word in word_count_dict:
                    word_count_dict[word] += 1
                else:
                    word_count_dict[word] = 1
                total_count += 1

    # make the unigram model
    for word, count in word_count_dict.items():
        probability = word_count_dict[word] / total_count
        unigram_model[word] = probability

    # write the unigram model to a pickle file
    UNIGRAM_MODEL_FILENAME = 'unigram.pkl'
    with open(UNIGRAM_MODEL_FILENAME, 'wb') as f:
        pickle.dump(unigram_model, f)

    return unigram_model


def main(argv):
    if len(argv) != 2:
        raise Exception('Usage: python train-unigram.py <filename>')
    unigram_model = train_unigram_model(argv[1])
    # print out the trained unigram model
    print('Training is finished!')
    print(unigram_model)


if __name__ == '__main__':
    main(sys.argv)
