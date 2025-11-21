import sys
from stats import get_num_words, sort_words


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    content = get_book_text(sys.argv[1])
    count = get_num_words(content)
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    char_dict = sort_words(content)
    for d in char_dict:
        if d["name"].isalpha():
            print(f"{d['name']}:{d['num']}")
    print("============= END ===============")


def get_book_text(path: str):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents


if __name__ == "__main__":
    main()
