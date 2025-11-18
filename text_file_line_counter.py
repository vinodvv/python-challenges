import string

def analyze(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    line_count = len(content.split("\n"))
    word_count = len(content.split())
    character_count = len(content)

    return content, line_count, word_count, character_count


def unique_words(text):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    words = set(cleaned_text.split())
    return words


if __name__ == "__main__":
    while True:
        print("Type 'exit' to Quit.\n")
        file_name = input("Enter the filename to analyze: ").strip()
        if file_name.lower() == "exit":
            print("Good Bye!")
            break
        if not file_name:
            print("Please enter a valid filename.\n")
            continue

        try:
            content, line_count, word_count, character_count = analyze(file_name)
            unique_word_set = unique_words(content)
        except FileNotFoundError:
            print(f"File '{file_name}' not found. Please try again.\n")
            continue
        except Exception as e:
            print(f"An error occurred: {e}\n")
            continue

        print("\nText File Analyzer")
        print("=" * 20)
        print(f"\nAnalyzing file: {file_name}\n")
        print("Statistics")
        print("-" * 20)
        print(f"Lines: {line_count}")
        print(f"Words: {word_count}")
        print(f"Unique words: {len(unique_word_set)}")
        print(f"Characters: {character_count}\n")
        print("Analysis complete!\n")
