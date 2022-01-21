#Вам необходимо найти самый длинный префикс среди полученного списка строк.
#Строки состоят только из английских букв в нижнем регистре.

def longest_prefix(list_words: list):
    prefix = ''
    for symbols in zip(*list_words):
        if len(set(symbols)) == 1:
            prefix += symbols[0]
        else:
            break

    return prefix

# def longest_prefix(inp: list):
#     return (''.join([(symb[0]) if len(set(symb)) == 1 else '|' for symb in zip(*inp)]).split('|')[0])

# мой вариант.
# def longest_prefix(list_of_words):
#     min_len = min((len(word) for word in list_of_words))
#     pref = ''
#     for i in range(min_len):
#         finish = False
#         for word in list_of_words:
#             if word[i] != list_of_words[0][i]:
#                 finish = True
#                 break
#         if finish:
#             break
#         else:
#             pref = pref + list_of_words[0][i]
#
#     return pref

if __name__ == '__main__':
    assert longest_prefix(['flower', 'flow', 'flight']) == 'fl'
    assert longest_prefix(['car', 'cir']) == 'c'
    assert longest_prefix(['sol', 'ution']) == ''
