# coding=utf-8

from wxpy import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

bot = Bot()
tuling = Tuling(api_key='c6c63b14d0344309911bbccae822e479')

ques_file = open('question', 'a+b')
ans_file = open('answer', 'a+b')

question = []
answer = []
@bot.register()
def auto_reply(msg):
    if isinstance(msg.chat, MP):
        question.append(str(msg))
        string = tuling.do_reply(msg)
        answer.append(string)

embed()

for i in range(len(question)):
    ques_file.write(question[i] + '\n')

for i in range(len(answer)):
    ans_file.write(answer[i] + '\n')

ques_file.close()
ans_file.close()
