
def charcount(file_contents):

    lower_file_contents = file_contents.lower()
    char_count = {}

    for char in lower_file_contents:
        if char.isalpha():  # Check if it's an alphabetic character
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1 

    char_count = [{"char": char, "num": count} for char, count in char_count.items()]

    char_count.sort(reverse=True, key=sort_on)

    return char_count

def sort_on(dict):
    return dict["num"]



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)  # Display the contents of the file to the console
        words = file_contents.split()
        wordcount = len(words)

        #print(charcount(file_contents))

    sorted_char_list = charcount(file_contents)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{wordcount} words found in the document\n")

    for entry in sorted_char_list:
        char = entry["char"]
        num = entry["num"]
        print(f"The '{char}' character was found {num} times")

    print(f"--- End report ---")


main()

