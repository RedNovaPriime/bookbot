
def charcount(file_contents):

    lower_file_contents = file_contents.lower()
    char_count = {}

    for char in lower_file_contents:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)  # Display the contents of the file to the console
        words = file_contents.split()
        wordcount = len(words)

        print(charcount(file_contents))
main()

