import argparse
import pickle

if __name__ == '__main__':
    '''
    This script converts a txt file that's already tokenized by the spacy tokenizer
    to a file in CoNLL format
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', help='spacy tokenized txt file')
    parser.add_argument('-d', '--dict', help='pickle file containing labels')
    parser.add_argument('-o', '--outfile', help='The output conll file')
    args = parser.parse_args()

    sentences = []
    with open(args.dict, 'rb') as f:
        labels_dict = pickle.load(f)
    with open(args.infile) as f:
        for line in f.readlines():
            sentences.append(line)
    
    with open(args.outfile, 'w') as f:
        for i, sent in enumerate(sentences):
            for j, token in enumerate(sent.split()):
                tag = '0'
                if (i, j) in labels_dict:
                    tag = labels_dict[(i, j)]
                f.write(f"{token}\t{tag}\n")
            f.write('\n')  # Add a newline to separate sentences

    