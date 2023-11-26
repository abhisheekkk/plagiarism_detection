from difflib import SequenceMatcher

with open('./project/demo1.txt') as one_file, open('./project/demo2.txt') as two_file:
    data_file1 = one_file.read()
    data_file2 = two_file.read()
    matches = SequenceMatcher(None, data_file1, data_file2).ratio()
    print(f" The plagiarized content is{matches*100}% ")