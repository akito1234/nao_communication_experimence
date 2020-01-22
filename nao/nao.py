# -*- coding: utf-8 -*-
from naoqi import ALProxy
import time
import sys
import codecs

#---------------------------------
#通信設定
#---------------------------------
#IP_address = "localhost"
#host = 52836
IP_address = "192.168.11.4"
host = 9559

#--------------------------------
#　フローファイル
#--------------------------------

# キーボード入力
print("------Keyboard input------")
tts = ALProxy("ALTextToSpeech", IP_address, host)
def introduction():
    pass

def say_from_file(tts, filename, encoding):
    with codecs.open(filename, encoding=encoding) as fp:
        contents = fp.read()
        # warning: print contents won't work
        to_say = contents.encode("utf-8")
        list_output = to_say.split()
    for i in range(len(list_output)):
        tts.say(list_output[i])
        # コマンド入力を待つ
        judge_answer()

def judge_answer():
    try:
        #正解は１，間違いは0
        input_val = input("Please Input Correct: 1, Wrong: 0\n")
        if input_val == 1:
            tts.say(r"\rspd=110\\vct=150\ウレシーーーーーーッ、、メッッチャウレシーーーーーーッ")
            print u"NAO: せいかーい"
        elif input_val == 0:
            #tts.say("ざんねーん")
            tts.say(r"\rspd=110\\vct=130\ちょっと \vct=140\ 無茶ぶりしちゃいましたネッ？")
            print u"NAO: せいかーい"
        else:
            print "command error detected"

    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)

    

def main():
    tts = ALProxy("ALTextToSpeech", IP_address, host)
    tts.setLanguage("Japanese")
    say_from_file(tts, 'math_protocal.txt', 'utf-8')
    pass


if __name__ == "__main__":
    main()




  
   