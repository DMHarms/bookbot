source = "books/frankenstein.txt"

print(f"=== Report of {source} ===")

def get_file():
    with open(source) as f:
        file_contents = f.read()
        return file_contents

def count_words():
    content = get_file()
    words = content.split()
    word_count = len(words)
    print(f"Word count: {word_count}")

def count_characters():
    content = get_file()
    lowercase_content = content.lower()
    d_characters = {}
    for i in lowercase_content:
        d_characters[i] = 0
    for i in lowercase_content:
        d_characters[i] += 1
    return d_characters

def sort_dict(unsorted_dict):
    unsorted_list = list(unsorted_dict.items())
    sorted_list = sorted(unsorted_list, key=lambda x: x[1])
    return sorted_list

def character_report():
    character_list = sort_dict(count_characters())
    sorted_dict = dict(character_list)
    for i in sorted_dict:
        if i.isalpha():
            print(f"The letter '{i}' was found {sorted_dict[i]} times")

def main():
    count_words()
    character_report()

main()

print("=== END ===")