def main() -> str:
    book_path = "books/frankenstein.txt"
    book_text = get_text(book_path)
    print(book_text)


def get_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

    
main()