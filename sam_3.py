def analyze_text(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            letter_count = sum(c.isalpha() for c in text)
            word_count = len(text.split())
            line_count = text.count('\n') + 1
            print(f"Input file contains:\n{letter_count} letters\n{word_count} words\n{line_count} lines")
    except FileNotFoundError:
        print("Файл не найден.")

analyze_text('input1.txt')