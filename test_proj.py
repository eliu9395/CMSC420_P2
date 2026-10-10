# This is provided to you so that you can test your bst.py file with a particular tracefile.

import argparse
import csv
import proj

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-tf', '--tracefile')
    args = parser.parse_args()
    tracefile = args.tracefile

    t = proj.BST()
    with open(tracefile, "r") as f:
        reader = csv.reader(f)
        lines = [l for l in reader]
        for l in lines:
            if l[0] == 'insert_standard':
                t.insert_standard(int(l[1]))
            if l[0] == 'insert_nonstandard':
                t.insert_nonstandard(int(l[1]))
            if l[0] == 'delete_nonstandard':
                t.delete_nonstandard(int(l[1]))
            if l[0] == 'search':
                print(t.search(int(l[1])))
            if l[0] == 'dump':
                print(t.dump())