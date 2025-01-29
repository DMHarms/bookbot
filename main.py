file_contents = ""
source = "books/frankenstein.txt"

def get_file():
    with open(source) as f:
        file_contents = f.read()
        return file_contents
        
def count_words():
    content = get_file()
    words = content.split()
    word_count = len(words)
    print(f"word count: {word_count}")

def main():
    count_words()

main()