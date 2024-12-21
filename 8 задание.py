# 8 задание
word_set = set()
alfavit = set('ОДЕКОЛОН')
for l_1 in alfavit:
 for l_2 in alfavit:
        for l_3 in alfavit:
            for l_4 in alfavit:
                for l_5 in alfavit:
                    for l_6 in alfavit:
                        for l_7 in alfavit:
                            for l_8 in alfavit:
                                new_word = l_1 + l_2 + l_3 + l_4 + l_5 + l_6 + l_7 + l_8
                                word_set.add(new_word)
word_list = sorted(word_set)
max_number = 0
for index in range(len(word_list)):
