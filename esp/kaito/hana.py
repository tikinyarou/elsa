# -*- coding:utf-8 -*-
# 後ろの文字をハードコードしてます・・・．
# 使い方：
# > python thiscode.py
# > 入力待ち
# > {あかい,あおい,きいろい}はな
# あかいはな
# あおいはな
# きいろいはな

import re

# 標準入力
print ('入力待ち')
x = input()


pre = re.compile('\{.+\}')
in_pre = pre.match(x)
brace = re.compile('[\{\}]')
in_pre_list = re.sub(brace,'',in_pre.group()).split(',')

in_bac = 'はな'


# 前の各文字と後ろを出力する
for pre in in_pre_list:
    print (pre + in_bac)
