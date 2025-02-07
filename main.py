def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)  # Display the contents of the file to the console
        words = file_contents.split()
        wordcount = len(words)
        print(wordcount)

main()