def single_root_words(root_word, *other_words):
    same_words = []
    root_word_upper = root_word.upper()
    for i in other_words:
        if root_word_upper in i.upper() or i.upper() in root_word_upper:
            same_words.append(i)
    return same_words


res_1 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
res_2 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(res_1)
print(res_2)
