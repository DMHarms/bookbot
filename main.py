source = "books/frankenstein.txt"

def count_words():
    content = get_file()
    words = content.split()
    word_count = len(words)
    print(f"word count: {word_count}")

def count_characters():
    content = get_file()
    lowercase_content = content.lower()
    d_characters = {}
    for i in lowercase_content:
        d_characters[i] = 0
    for i in lowercase_content:
        d_characters[i] += 1
    print(d_characters)

def get_file():
    with open(source) as f:
        file_contents = f.read()
        return file_contents

def main():
    # count_words()
    count_characters()

main()