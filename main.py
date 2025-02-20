def main() -> str:
    book_path = "books/frankenstein.txt"
    book_text = get_text(book_path)
    book_word_count = count_words(book_text)
    book_character_count = count_characters(book_text)
    print(book_text)
    print(f"{book_word_count} words found in the document")
    print(book_character_count)


def count_words(book_text):
    return len(book_text.split())


def count_characters(book_text):
    count_dict = {}
    book_text_lower = book_text.lower()
    for letter in book_text_lower:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    return count_dict


def get_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents


main()