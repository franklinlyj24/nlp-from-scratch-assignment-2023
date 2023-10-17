import pickle
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--outfile', help='The output pickle file')
    args = parser.parse_args()

    # TODO: replace each entry with (sent_idx, word_idx): label
    my_dict = {(0, 14): 'B-MethodName'}
    with open(args.outfile, 'wb') as f:
        pickle.dump(my_dict, f)
