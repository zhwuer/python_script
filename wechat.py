# -*- coding: utf-8 -*-

from wxpy import *
import time, sys

def countdownbomb(bot):
    who = findUser(bot)
    number = int(input("\n轰炸的次数："))
    n = int(input("\n轰炸频率(次/秒，请勿大于2)："))
    a = list(range(number))
    for i in a[::-1]:
        who.send('倒计时：%d'%i)
        time.sleep(1/n)

def turing(bot):
    tuling = Tuling(api_key='c6c63b14d0344309911bbccae822e479')
    isOnline = True
    @bot.register()
    def reply_my_friend(msg):
        nonlocal isOnline
        print(msg)
        if msg.text == 'shutup' or msg.text == 'turnon':
            if msg.text == 'shutup':
                msg.reply_msg('Turing机器人关闭')
                isOnline = False
            if msg.text == 'turnon':
                msg.reply_msg('Turing机器人开启')
                isOnline = True
        if isinstance(msg.chat, Friend) and isOnline:
            if msg.sender.remark_name == 'papa' or msg.sender.remark_name == 'mum':
                return
            if msg.type == 'Recording' or msg.type == 'Picture' or msg.type == 'Card':
                if msg.type == 'Recording':
                    msg.get_file('/Users/Jartus/Desktop/%s' % msg.file_name)
                    msg.reply_msg('语音消息我不听，还给你<-.->')
                msg.forward(msg.sender)
                return
            if msg.type == 'Text':
                tuling.do_reply(msg)
        else:
            if isinstance(msg.chat, Group) and msg.is_at and isOnline:
                tuling.do_reply(msg)
            else:
                return
    bot.join()

def bomb(bot):
    str = input("\n要轰炸的文本：")
    who = findUser(bot)
    number = int(input("\n轰炸的次数："))
    n = int(input("\n轰炸频率(次/秒，请勿大于2)："))
    for i in range(number):
        who.send(str)
        time.sleep(1/n)

def show(bot):
    @bot.register()
    def print_messages(msg):
        print(msg)
    bot.join()

def findUser(bot):
    str = input("\n昵称：")
    userlist = bot.friends().search(str)
    while not userlist:
        print('没有找到此人，请重新输入')
        str = input("\n昵称：")
        userlist = bot.friends().search(str)
    while userlist[0].name!=str:
        print('没有找到此人，请重新输入')
        str = input("\n昵称：")
        userlist = bot.friends().search(str)
    return userlist[0]

def AFK(bot):
    @bot.register()
    def auto_reply(msg):
        if not isinstance(msg.chat, Group):
            if msg.sender.remark_name == 'papa' or msg.sender.remark_name == 'mum':
                return
        if msg.text == 'assignment':
            return '继续想呗<-.->'
        if msg.text == 'hi':
            turing(bot)
        if msg.text == 'CZH':
            return '微信号：Soberclown'
        if msg.text == '忙啥呢':
            return '忙IELTS'
        if msg.text == '最近咋样':
            return '详情见回复忙啥呢'
        if isinstance(msg.chat, Group) and not msg.is_at:
            return
        if isinstance(msg.chat, Friend):
            print(msg)
            return 'Do not disturb, I am on a tight schedule today.        私以为您可能会问以下问题        1.与assignment有关的问题请留言或者如果想查看我的源代码请直接回复assignment        2.与debug有关的问题请把报错信息截图发给我（如果比较急请回复CZH获得崔正浩爸爸的联系方式）        3.我在忙什么？请直接回复忙啥呢        4.最近过得怎么样？请直接回复最近咋样        5.回复hi和turing机器人聊天            Have a nice day :)'
        else:
            return
    bot.join()

def surface():
    print('\n\t\tWelcome to WeChat Assisstant!\n')
    print('\t\t1.倒计时消息轰炸\n')
    print('\t\t2.自定义文本消息轰炸\n')
    print('\t\t3.调用turing机器人聊天\n')
    print('\t\t4.离开模式\n')
    print('\t\t0.退出')
    num = input("\nEnter a number:")
    return num

def main():
    print('Please Scan the QR_CODE and login your WeChat')
    print('Wait a minutes....')
    bot = Bot(cache_path=True)
    num = surface()
    while 1:
        if num == '0':
            break
        if num == '1':
            countdownbomb(bot)
        else:
            if num == '2':
                bomb(bot)
            else:
                if num == '3':
                    turing(bot)
                else:
                    if num == '4':
                        AFK(bot)
                    else:
                        if num == '5':
                            show(bot)
                        else:
                            print('Wrong Number！！！')
        num = surface()

main()
