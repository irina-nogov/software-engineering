def count_characters(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    char_count = {}
    for char in text:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1

    return char_count


character_counts = count_characters('sam5.txt')
for char, count in character_counts.items():
    print(f"символ '{char}' встречается  {count} раз(а)")
