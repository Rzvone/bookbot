from stats import number_of_words, characters_number_in_book, sorted_dictonary
import sys

if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)

print(f"============ BOOKBOT ============")
print(f"Analyzing book found at books/frankenstein.txt...")
print(f"----------- Word Count ----------")
number_of_words(sys.argv[1])
print(f"--------- Character Count -------")
characters_number_in_book(sys.argv[1])
char_count = characters_number_in_book(sys.argv[1])
sorted_dictonary(char_count)
print(f"============= END ===============")