# -*- coding: utf-8 -*-
from naoqi import ALProxy
import time
import sys
import codecs



# テキストファイルをList型に落とす
def text_from_file(filename, encoding):
    with codecs.open("./protocol/"+filename, encoding=encoding) as fp:
        contents = fp.read()
        # warning: print contents won't work
        to_say = contents.encode("utf-8")
        list_output = to_say.split()
    return list_output
