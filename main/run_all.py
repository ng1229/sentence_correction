"""
[Title] Sentence Correction
[Author] Namgyu Roh(ng911229@gmail.com)
[Description]
  - 빅데이터 청년인재 Team project
[References]
  -
"""
import pandas as pd

from utility import read_dict
from utility import word_color
from utility import word_correction_index
from utility import word_correction
from utility import word_upper

sentence = input('>>> ') # 교정 원하는 문장 입력
# sample : but this study is important

word_phrase_dict = read_dict.read_dict() # 데이터 사전 불러오기
dict_index = word_correction_index.word_corrections_index(sentence, word_phrase_dict) # 각 단어, 숙어별 index 값 필요
word_colored = word_color.word_color(dict_index, sentence) # 교정이 필요한 단어 색 변경
sentence_final = word_correction.word_correction(dict_index, sentence, word_phrase_dict) # 교정 작업
word_upper.word_upper(sentence_final) # 문장의 첫글자 or 고유명사 대문자로 변경
