#!/usr/bin/python

import tabula
import sys
reload(sys)  
sys.setdefaultencoding('utf8')


f = open('/Users/Jartus/words.txt', 'a+b')
for i in range(20):
    df = tabula.read_pdf("/Users/Jartus/Library/Mobile Documents/com~apple~CloudDocs/IELTS/IELTS_Writing.pdf", pages=i)
    for indexs in df.index:
        try:
            f.write(df.loc[indexs].values[1].strip() + '    ' + df.loc[indexs].values[0].strip() + '\n')
        except AttributeError:
            continue

f.close()