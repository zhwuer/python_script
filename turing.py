# -*- coding: utf-8 -*-

from wxpy import *
import time, sys, random, os, re

bot = Bot(cache_path=True)
tuling = Tuling(api_key='c6c63b14d0344309911bbccae822e479')
isOnline = True
@bot.register(except_self=False)
def auto_reply(msg):
    global isOnline
    print(msg)
    if isinstance(msg.chat, Group) or isinstance(msg.chat, MP):
        return
    if msg.sender == bot.self:
        if msg.text == 'shutup':
            msg.reply_msg('Turing机器人关闭')
            isOnline = False
        if msg.text == 'turnon':
            msg.reply_msg('Turing机器人开启')
            isOnline = True

        temp = re.findall(r'启动消息轰炸器', msg.text)
        str = re.findall(r'启动消息轰炸器：(.+?)，(.+?)次', msg.text)
        if str != None:
            text = str[0][0]
            num = int(str[0][1])
        if temp != None:
            for i in range(num):
                msg.receiver.send(text)
                time.sleep(1/2)
        return
    elif msg.text == 'shutup' or msg.text == 'turnon':
        msg.reply_msg('Permission Denied')
    if isOnline:
        if isinstance(msg.chat, Friend):
            if msg.sender.remark_name == 'papa' or msg.sender.remark_name == 'mum':
                return
            if msg.type == 'Recording' or msg.type == 'Picture':
                if msg.type == 'Recording':
                    msg.get_file('%s/%s' % (os.getcwd(), msg.file_name))
                    msg.reply_msg('发啥语音啊，发文字！')
                if msg.type == 'Picture':
                    msg.reply_image('%s/pic/pic%s.jpg' % (os.getcwd(), random.randint(1, 137)))
                return
            if msg.type == 'Text':
                tuling.do_reply(msg)
    else:
        return
embed()
bot.join()
