import sys
from stats import get_num_words

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

source_title = sys.argv[1]

def get_file():
    with open(source_title) as f:
        file_contents = f.read()
        return file_contents

print(f"=== Report of {source_title} ===")

def main():
    get_num_words(get_file())

main()

print("=== END ===")