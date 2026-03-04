"""
License: Apache
Organization: UNIR
"""

import os
import sys
import argparse

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a word list file.")
    parser.add_argument('filename', help='Path to the file containing words (one per line)')
    parser.add_argument('dup', choices=['yes', 'no'], help='yes to remove duplicates, no to keep them')
    parser.add_argument('--sort', action='store_true', help='Sort the output alphabetically')

    args = parser.parse_args()

    filename = args.filename
    remove_duplicates = args.dup.lower() == 'yes'
    do_sort = args.sort

    print(f"Reading words from file {filename}")
    file_path = os.path.join('.', filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"File {filename} does not exist, using sample list")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    if do_sort:
        word_list = sort_list(word_list)

    print(word_list)
