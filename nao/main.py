# -*- coding: utf-8 -*-
from naoqi import ALProxy
import time
import sys
import codecs
from utils import * 

#---------------------------------
# 通信設定
#---------------------------------
#IP_address = "localhost"
#host = 58978
IP_address = "192.168.11.4"
host = 9559


# 初期設定
tts = ALProxy("ALTextToSpeech", IP_address, host)
tts.setLanguage("Japanese")
aup = ALProxy("ALAudioPlayer", IP_address, host)


#--------------------------------
# Introduction Section
#--------------------------------
tts = ALProxy("ALTextToSpeech", IP_address, host)
def introduction():
    introduction_list_text = text_from_file('01_Introduction.txt', 'utf-8')
    for i in range(len(introduction_list_text)):
        tts.say(introduction_list_text[i])
        system_introduction(i)
        time.sleep(1)
        

def system_introduction(id):
    if id == 2:
        # 正解音
        correct_or_wrong_sound(val=True)
    elif id == 3:
        # 不正解音
        correct_or_wrong_sound(val=False)
    else:
        return 0
    pass

def correct_or_wrong_sound(val=True):
    if val == True:
        fileID = aup.post.playFile("/Users/akito/source/repos/nao/nao/sound/Quiz-Correct_Answer02-3.wav", 1, 100)
        
    elif val ==False:
        fileID = aup.post.playFile("/Users/akito/source/repos/nao/nao/sound/Quiz-Wrong_Buzzer02-3.wav", 1, 100)
    else:
        return 0

#--------------------------------
# Stress Section
#--------------------------------


#--------------------------------
# Amusement Section
#--------------------------------





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
    # ------------------
    # 会話を開始
    # ------------------
    # 01.Introduction
    #introduction()
    # 02. Stress

    # 03. Amusement

    time.sleep(5)
    
    #fileID = aup.loadFile("Quiz-Wrong_Buzzer02-3.wav", 1, 0)
    fileID = aup.post.playFile("/home/nao/Quiz-Correct_Answer02-3.wav",1,0)
    print fileID
    time.sleep(5)
    
    #ap.loadSoundSet("Aldebaran")
    #fileId = ap.post.playSoundSetFile("Quiz-Wrong_Buzzer02-3.wav")
    #fileID = aup.post.playFile("/Users/akito/source/repos/nao/nao/sound/Quiz-Wrong_Buzzer02-3.wav", 0.5, 1.0)
    ###aup.play(fileID)
    #print "play music!"
    #print fileID
    ##time.sleep(10)

    ##fileId = aup.loadFile("/../Quiz-Buzzer02.wav")
    ##aup.play(fileId)

    ##ap.loadSoundSet("Aldebaran")
    ##fileId = ap.post.playSoundSetFile("filename")


    #say_from_file(tts, 'math_protocal.txt', 'utf-8')
    pass


if __name__ == "__main__":
    main()




  
   