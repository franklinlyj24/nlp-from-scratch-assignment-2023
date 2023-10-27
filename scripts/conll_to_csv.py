import csv


paths = [
    "../data/test_output_Jean-Baptiste_roberta-large-ner-english.conll",
    "../data/test_output_dslim_bert-large-NER.conll",
    "../data/test_output_sileod_deberta-v3-base-tasksource-nli.conll",
    "../data/test_output_bert-base-cased.conll",
    "../data/test2_output_Jean-Baptiste_roberta-large-ner-english.conll",
    "../data/test2_output_dslim_bert-large-NER.conll",
    "../data/test2_output_sileod_deberta-v3-base-tasksource-nli.conll",
    "../data/test2_output_bert-base-cased.conll",
]

for path in paths:
    rows = []
    with open(path, 'r') as f:
        i = 1
        for line in f:
            if line == '\n':
                rows.append([i, 'X'])
            else:
                input, target = line.strip().split('\t')
                rows.append([i, target])
            i += 1
    while rows[-1][1] == 'X':
        rows = rows[:-1]
            
    # name of csv file  
    filename = path.replace('.conll', '.csv')
        
    # writing to csv file  
    with open(filename, 'w') as csvfile:
        # creating a csv writer object  
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(["id", "target"])
        csvwriter.writerows(rows)