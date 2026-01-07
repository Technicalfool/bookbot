from posix import PRIO_PGRP

from stats import char_stats, char_stats_sorted, word_count


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)

    # print(char_stats_sorted(char_stats(book_text)))

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + file_path + "...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    for pair in char_stats_sorted(char_stats(book_text)):
        print(f"{pair['char']}: {pair['num']}")
    print("============= END ===============")


main()
