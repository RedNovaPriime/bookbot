def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

# This ensures `main()` is only called when the script is run directly,
# and not when imported as a module.
if __name__ == "__main__":
    main()
