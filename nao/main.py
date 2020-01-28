# -*- coding: utf-8 -*-
from naoqi import ALProxy
import datetime
import sys
import codecs
from utils import * 
import qi
import argparse
import os
import time
import csv

#---------------------------------
# 通信設定
#---------------------------------
#IP_address = "localhost"
#host = 54711
IP_address = "192.168.11.4"
host = 9559

# 初期設定
tts = ALProxy("ALTextToSpeech", IP_address, host)
tts.setLanguage("Japanese")
aup = ALProxy("ALAudioPlayer", IP_address, host)

# Audio path
correct_path = "/home/nao/.local/share/PackageManager/apps/.lastUploadedChoregrapheBehavior/behavior_1/../Quiz-Correct_Answer02-3.wav"
wrong_path = "/home/nao/.local/share/PackageManager/apps/.lastUploadedChoregrapheBehavior/behavior_1/../Quiz-Wrong_Buzzer02-3.wav"
thinking_path = "/home/nao/.local/share/PackageManager/apps/.lastUploadedChoregrapheBehavior/behavior_1/../timecount_5s.wav"
shine_path =  "/home/nao/.local/share/PackageManager/apps/.lastUploadedChoregrapheBehavior/behavior_1/../shine1.wav"
kansei_path =  "/home/nao/.local/share/PackageManager/apps/.lastUploadedChoregrapheBehavior/behavior_1/../kansei2.wav"


#--------------------------------
# Introduction Section
#--------------------------------

#--------------------------------
# Stress Section
#--------------------------------

def introduction():
    print("introduction ... started")
    starttime = datetime.datetime.now()
    introduction_list_text = text_from_file('02_Stress_Introduction.txt', 'utf-8')
    for i in range(len(introduction_list_text)):
        tts.say(introduction_list_text[i])
        system_introduction(i)
        time.sleep(1)
    print("introduction ... finished")
    endtime = datetime.datetime.now()
    return starttime, endtime

def system_introduction(id):
    if id == 5:
        # 正解音
        fileID = aup.post.playFile(correct_path, 1, 1)
        time.sleep(1)
    elif id == 6:
        # 不正解音
        fileID = aup.post.playFile(wrong_path, 1, 1)
        time.sleep(1)
    else:
        return 0

def stress():
    # 暗算タスク
    starttime = datetime.datetime.now()
    print("stress task ... started")    
    stress_list_text = text_from_file('02_Stress_mental_arithmetic.txt', 'utf-8')
    for i in range(len(stress_list_text)):
        # 問題を2回繰り返す
        tts.say(stress_list_text[i])
        if i == 0:
            tts.say("もう一度いうよ")
            time.sleep(1)
        else:
            time.sleep(1)
        tts.say(stress_list_text[i])
        # シンキングタイム(5s)
        judge_answer()
    print("stress task ... finished")
    endtime = datetime.datetime.now()
    return starttime, endtime

def outroduction():
    print("outroduction ... started")
    starttime = datetime.datetime.now()
    introduction_list_text = text_from_file('02_Stress_outroduction.txt', 'utf-8')
    for i in range(len(introduction_list_text)):
        tts.say(introduction_list_text[i])
        time.sleep(1)
    print("outroduction ... finished")
    endtime = datetime.datetime.now()
    return starttime, endtime


def judge_answer():
    try:
        fileID = aup.post.playFile(thinking_path , 1, 1)
        time.sleep(5)
        #正解は１，間違いは0 聞き直しは2?(未実装)
        input_val = input("Please Input Correct: 1, Wrong: 0\n")
        
        if input_val == 1:
            fileID = aup.post.playFile(correct_path, 1, 1)
            tts.say(r"\rspd=120\\vct=135\正解です\rst\.")
            time.sleep(1) 
            print u"NAO: せいかーい"
        elif input_val == 0:
            fileID = aup.post.playFile(wrong_path, 1, 1)
            tts.say(r"\vct=125\ ぶっ \vct=160\ ぶぅぅぅ！\rst\.")
            time.sleep(1)
            print u"NAO: ざんねーん"
        else:
            # 聞き直し(未実装)
            print "command error detected"

    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)

#--------------------------------
# Amusement Section
#--------------------------------
def amusement_introduction():
    print("amusement ... started")
    starttime = datetime.datetime.now()
    amusement_list_text = text_from_file('03_Amusement.txt', 'utf-8')
    for i in range(len(amusement_list_text)):
        tts.say(amusement_list_text[i])
        amusement_system_introduction(i)
        time.sleep(1)

    print("amusement ... finished")
    endtime = datetime.datetime.now()
    return starttime, endtime

def amusement_system_introduction(id):
    if id == 6 or id == 17 or id == 26 or id == 42 or id == 59 or id == 64:
        # 音を鳴らす．(ピロピロリーン)
        fileID = aup.post.playFile(shine_path, 1, 1)
        time.sleep(1)
        print "Play"
    elif id == 19 or id == 36 or id == 51 or id == 68:
        # 音を鳴らす．ポップな音
        fileID = aup.post.playFile(kansei_path, 1, 1)
        time.sleep(1)
        print "Play"
    else:
        return 0


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
    Neutral_Time =300

    # 01.Introduction
    print "Experimence Start"
    print "Neutral Section Start"
    print datetime.datetime.now()
    neutral_start = datetime.datetime.now()
    time.sleep(Neutral_Time)
    print datetime.datetime.now()
    neutral_finish = datetime.datetime.now()
    print "Neutral Section Finished"
    

    # 02. Stress
    intro_start,intro_finish = introduction()
    print "stress intro finished "

    stress_start,stress_finish = stress()
    print "stress archimetic finished "

    outro_start,outro_finish = outroduction()
    print "stress outro finished "


    # 02.5  Questionnaire
    tts.say("1分はんごに次のセクションに移動するよ")
    time.sleep(90)


    # 03. Amusement
    amusement_start,amusement_finish = amusement_introduction()
    print "amusement finished "



    # 実験情報を出力
    with open('robot_communication_{}.csv'.format(datetime.datetime.now().strftime("%Y_%m_%d__%H_%M_%S")), 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Section","StartDatetime","FinishDatetime"])
        writer.writerow(['Neutral', neutral_start, neutral_finish])
        writer.writerow(['Stress intro', intro_start, intro_finish])
        writer.writerow(['Stress archimetic', stress_start, stress_finish])
        writer.writerow(['Stress outro', outro_start, outro_finish])
        writer.writerow(['Amusement', amusement_start, amusement_finish])

    print u"アプリケーションを終了"