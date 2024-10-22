def censor_sentence(sentence):
    with open('input2.txt', 'r', encoding='utf-8') as file:
        forbidden_words = file.read().split()
    words = sentence.split()
    censored_words = []
    for word in words:
        lowercase_word = word.lower()
        for fword in forbidden_words:
            if (lowercase_word.find(fword) >= 0):
                censored_word = lowercase_word.replace(fword, '*' * len(fword))
                censored_words.append(censored_word)
                break
        else:
            censored_words.append(word)
    censored_sentence = ' '.join(censored_words)
    print(censored_sentence)

sentence = "Hello, world ! Python IS the programming language of thE future. My EMAIL is .... PYTHON is awesome!!!!"
censor_sentence(sentence)