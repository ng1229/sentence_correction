# 교정이 필요한 단어 색 변경
def word_color(dict_index, sentence):
    print('입력하신 문장입니다. : ' + sentence)
    for key in (dict_index):
        item = dict_index[key]
        sentence = sentence.replace(item, '\x1b[1;33m' + item + '\x1b[1;m') # 노란색으로 지정
    print('교정이 필요한 단어들입니다. : ' + sentence)





