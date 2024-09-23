def single_root_words(root_word, *other_words):
    same_words = []
    root_word_x = root_word.upper()
    for i in other_words:
        other_words_x = i.upper()
        if root_word_x in other_words_x or other_words_x in root_word_x:
            same_words.append(i)
    return same_words




result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)