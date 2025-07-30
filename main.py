import sys
if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import get_num_words, get_char_count,get_sorted_characters_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents   
def main():
    book_text = get_book_text(sys.argv[1])
    result = get_num_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {result} total words")
    print("--------- Character Count -------")
    char_result =get_char_count(book_text)
    sorted_characters = get_sorted_characters_list(char_result)
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()
