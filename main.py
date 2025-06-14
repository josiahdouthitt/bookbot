from stats import get_num_words, get_word_count, make_count_list
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

with open(path) as f:
    file_contents = f.read()
    count_total = get_word_count(file_contents)
    count_list = make_count_list(count_total)
    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file_contents)} total words")
    print("--------- Character Count -------")
    for i in count_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")