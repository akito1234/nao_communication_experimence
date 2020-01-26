#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Example: Use play Method"""

import qi
import argparse
import sys
import os

def main(session):
    """
    This example uses the play method.
    """
    # Get the service ALAudioPlayer.

    audio_player_service = session.service("ALAudioPlayer")

    #Loads a file and launchs the playing 5 seconds later

    fileId = audio_player_service.loadFile("/home/nao/.local/share/PackageManager/apps/.lastUploadedChoregrapheBehavior/behavior_1/../Quiz-Correct_Answer02-3.wav")
    audio_player_service.play(fileId)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.11.4",
                        help="Robot IP address. On robot or Local Naoqi: use '192.168.11.4'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)