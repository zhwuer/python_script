#coding=utf-8

from wxpy import *
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
bot = Bot(cache_path=True)


for line in open('list'):
    friend = bot.friends().search(line.decode('utf-8'))[0]
    print(friend.name)
    time.sleep(2)
    friend.send('2018新年快乐！你可能以为这是群发，事实可不是这样的亲爱的%s' % friend.name)

    
