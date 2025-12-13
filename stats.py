def number_of_words(book):
    with open(book) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
    print(f"Found {num_words} total words")


def characters_number_in_book(book):
    with open(book, 'r') as f:
        file_contents = f.read()
        char_counts = {}
        for char in file_contents:
            if char.isalpha():
              if char.lower() in char_counts:
                char_counts[char.lower()] += 1
              else:
                char_counts[char.lower()] = 1
    return char_counts
            
def sorted_dictonary(dic):
    sorted_chars = sorted(dic.items(), key=lambda item: (-item[1], item[0]))
    for char, count in sorted_chars:
        print(f"{char}: {count}")