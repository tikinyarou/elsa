# base_string = 'test'
# INSERT_POINT = 2  #分かりやすくするために大文字
# insert_string = '--hoge--'
#
# # 2文字目から挿入したい場合
# def insert_string_to_base(target_string, insert_point, insert_string):
#     return target_string[:insert_point] + insert_string + target_string[insert_point:]
#
#     String('test').insert(2, '--hoge--')
# coding: UTF-8
import sys
import os
import re
#文字コード指定に必要
import codecs

#置換文字列を指定
name_old='elsa' #この文字を含むファイルを操作＋ファイル名の置換元文字列
name_new='nelsa' #ファイル名の置換後文字列
txt_old='M106' #ファイル内の置換元 文字列
txt_new=';' #ファイル内の置換後文字列

#パス指定小楽でスクリプト配置フォルダのファイル一覧取得
files = os.listdir()
for file in files:
    #まず.txtを含むファイルのみ読込
    txt = re.compile(".txt")
    if txt.search(file):
        # ファイル名の置換前後の文字列を指定
        file_new = file.replace(name_old,name_new)

        read_file = codecs.open(file, 'r', 'shift_jis')
        write_file = codecs.open(file_new, 'w', 'shift_jis')

        lines = read_file.readlines() #読み込み
        lines2 = []
        for line in lines:
            line = line.replace(txt_old,txt_new) #テキスト置換
            lines2.append(line) #別リストにする
        else:
            write_file.write(''.join(lines2)) #書き込み
            read_file.close()

#       os.rename(file, file_new)
    else:
        pass
