def count_words(source):
    content = source
    words = content.split()
    word_count = len(words)
    print(f"Word count: {word_count}")

def count_characters(source):
    content = source
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

def character_report(source):
    character_list = sort_dict(count_characters(source))
    sorted_dict = dict(character_list)
    for i in sorted_dict:
        if i.isalpha():
            print(f"'{i}: {sorted_dict[i]}'")
            
def get_num_words(imported_source):
        source = imported_source
        count_words(source)
        character_report(source)