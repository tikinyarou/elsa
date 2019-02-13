# coding: UTF-8
import sys
import os
import re
#文字コード指定に必要
import codecs
#置換文字列を指定
name_old='v001' #この文字を含むファイルを操作＋ファイル名の置換元文字列
name_new='v002' #ファイル名の置換後文字列
tempm109='M109' #ファイル内の置換元 文字列
tempm106='M106'#ファイル内の置換元 文字列
temp=';' #ファイル内の置換後文字列
#上でとりあえず温度の除外する
#z軸を書き換える必要があるかもしらんスマートにやる方法がわかんない
#wで書き込みモードで開いた時に使う
#z軸を検索してライン番号引く１で挿入プラス１で挿入する
servoON='G93'#サーボをオンにする
servoOFF='G94'#サーボをオフにする

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
            line = line.replace(tempm106,temp) #テキスト置換
            if line.find("Z") >= 0:
                print line[:-1]
                test = line[]
                line.insert(test-1,'servoOFF\n')
                line.insert(test+1,'servoON\n')
            lines2.append(line) #別リストにする
        else:
            write_file.write(''.join(lines2)) #書き込み
            read_file.close()

        # for line in lines:
        #     if line.find("Z") >= 0:
        #         print line[:-1]
        #         line.insert(line[]-1,'servoOFF\n')
        #         line.insert(line[]+1,'servoON\n')
                #上のプログラムここに書く意味あるのかわからん
                #行を指定して書き込みしろよな
                #insertてきたので室力された文字列をどうにかする

        # with open(path_w) as f:
        #     l = f.readlines()
        #
        # l.insert(0, 'FIRST\n')
        #
        # with open(path_w, mode='w') as f:
        #     f.writelines(l)
        #
        # with open(path_w) as f:
        #     print(f.read())

        # i = 0
        # while i >= 0:
        #   m = pTXC.search(dna, i)
        #   if m:
        #     print(m.start())
        #     print(m.end())
        #     i = m.start() + 1
        #   else:
        #     break

#       os.rename(file, file_new)
    else:
        pass
