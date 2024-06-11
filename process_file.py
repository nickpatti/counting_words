import re
from typing import Dict, List, Tuple

WORD = 0
COUNT = 1


def process_chunk(chunk: str, word_counts: Dict[str, int]) -> Dict[str, int]:
    """
    A function to update word counts in a dictionary, takes a single line of a document at a time.
    :param chunk: one line of a txt document
    :param word_counts: Dictionary with current counts for each word from the input file.
    :return: Dictionary with updated word counts, word as the key and count as the value
    """
    words = re.findall(r'\b\w+\b', chunk.lower())
    for word in words:
        if word_counts.get(word):
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def count_words(file_path, num_of_entries:int = None) -> List[Tuple[str, int]]:
    """
    A function that reads a file, loops over each line to separate the file into
     chunks and returns a word count dictionary
    :param file_path: path to the file
    :param num_of_entries: integer to get the first x amount of entries, if argument not present all entries are returned
    :return: A sorted list of tuples with the count and the word.
    """
    word_counts = dict()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            process_chunk(chunk=line, word_counts=word_counts)
    sorted_list = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    if num_of_entries:
        return sorted_list[:num_of_entries]
    return sorted_list


def format_word_counts(file_path, num_of_entries: int = None) -> str:
    """
    A function that returns a string with the most frequent words in the given document.
    :param file_path: Path to local file
    :param num_of_entries: The amount of items in the sorted list of words to be output
    :return: A string in the format "<count> <word> \n" to show the top x most frequent words
    """
    word_counts = count_words(file_path, num_of_entries)
    output_lines = []
    for index, item in enumerate(word_counts):
        output_lines.append(f"{item[COUNT]} {item[WORD]}")
    output_string = "\n".join(output_lines)
    return output_string
