import argparse
import csv

if __name__ == '__main__':
    '''
    This script converts a test CoNLL file with no labels to txt
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', help='The input conll file')
    parser.add_argument('-o', '--outfile', help='The output txt file')
    args = parser.parse_args()

    result = []
    paragraph = []
    with open(args.infile, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # Skip the header row
        header = next(csv_reader)
        
        for row in csv_reader:
            if row[1] == '':
                result.append(' '.join(paragraph))
                paragraph = []
            else:
                paragraph.append(row[1])
        if paragraph:
            result.append(' '.join(paragraph))
    
    with open(args.outfile, 'w') as txt_file:
        txt_file.write('\n'.join(result))
