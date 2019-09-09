import pandas as pd

# 데이터 구축된 파일에서 단어 or 숙어를 dictionary 형태로 불러오기
def read_dict():
    word_phrase_csv = pd.read_csv('../resource/word_phrase_dict.csv')
    word_phrase_del = word_phrase_csv.fillna('None')
    word_phrase_dict = word_phrase_del.set_index('before').T.to_dict('dict')

    return word_phrase_dict




