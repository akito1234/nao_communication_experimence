# -*- coding: utf-8 -*-
from naoqi import ALProxy
import time
import sys
import codecs
from utils import * 
import qi
import argparse
import sys
import os
#---------------------------------
# 通信設定
#---------------------------------
#IP_address = "localhost"
#host = 58978
IP_address = "192.168.11.4"
host = 9559

# nao dictionary
nao_dict = "/home/nao/.local/share/PackageManager/apps/.lastUploadedChoregrapheBehavior/behavior_1/.."

# 初期設定
tts = ALProxy("ALTextToSpeech", IP_address, host)
tts.setLanguage("Japanese")
tts.say(r"\rst\tst")
aup = ALProxy("ALAudioPlayer", IP_address, host)

#--------------------------------
# Introduction Section
#--------------------------------
def introduction():
    introduction_list_text = text_from_file('01_Introduction.txt', 'utf-8')
    for i in range(len(introduction_list_text)):
        tts.say(introduction_list_text[i])
        system_introduction(i)
        time.sleep(1)
        

def system_introduction(id):
    if id == 5:
        # 正解音
        correct_or_wrong_sound(val=True)
    elif id == 6:
        # 不正解音
        correct_or_wrong_sound(val=False)
    else:
        return 0
    pass

def correct_or_wrong_sound(val=True):
    if val == True:
        fileID = aup.post.playFile("/home/nao/.local/share/PackageManager/apps/.lastUploadedChoregrapheBehavior/behavior_1/../Quiz-Correct_Answer02-3.wav", 1, 1)
        time.sleep(1)
    elif val ==False:
        fileID = aup.post.playFile("/home/nao/.local/share/PackageManager/apps/.lastUploadedChoregrapheBehavior/behavior_1/../Quiz-Wrong_Buzzer02-3.wav", 1, 1)
        time.sleep(1)
    else:
        return 0
#--------------------------------
# Stress Section
#--------------------------------
def stress():
    stress_list_text = text_from_file('02_Stress_mental_arithmetic.txt', 'utf-8')
    for i in range(len(stress_list_text)):
        tts.say(stress_list_text[i])
        st_system_introduction(i)
        judge_answer()

def judge_answer():
    try:
        #正解は１，間違いは0
        input_val = input("Please Input Correct: 1, Wrong: 0\n")
        if input_val == 1:
            fileID = aup.post.playFile("/home/nao/.local/share/PackageManager/apps/.lastUploadedChoregrapheBehavior/behavior_1/../Quiz-Correct_Answer02-3.wav", 1, 1)
            tts.say(r"\rspd=120\\vct=135\正解です\rst\.")
            time.sleep(1)
            
            print u"NAO: せいかーい"
        elif input_val == 0:

            fileID = aup.post.playFile("/home/nao/.local/share/PackageManager/apps/.lastUploadedChoregrapheBehavior/behavior_1/../Quiz-Wrong_Buzzer02-3.wav", 1, 1)
            tts.say(r"\vct=125\ ぶっ \vct=160\ ぶぅぅぅ！\rst\.")
            time.sleep(1)
            
            print u"NAO: せいかーい"
        else:
            print "command error detected"

    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)


def st_system_introduction(id):
    if id == 5:
        # 正解音
        correct_or_wrong_sound(val=True)
    elif id == 6:
        # 不正解音
        correct_or_wrong_sound(val=False)
    else:
        return 0
    pass


#--------------------------------
# Amusement Section
#--------------------------------



def from_file(tts, filename, encoding):
    with codecs.open(filename, encoding=encoding) as fp:
        contents = fp.read()
        # warning: print contents won't work
        to_say = contents.encode("utf-8")
        list_output = to_say.split()
    for i in range(len(list_output)):
        tts.say(list_output[i])
        # コマンド入力を待つ
        judge_answer()


   

if __name__ == "__main__":
    # ------------------
    # 会話を開始
    # ------------------
    # 01.Introduction
    introduction()
    # 02. Stress
    stress()
    # 03. Amusement




  
   