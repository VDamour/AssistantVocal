from gtts import gTTS
import sys
import os

#load arguments:
if len(sys.argv) <= 2:
    print("Error: need to specify file path, language")
    print("Usage: python script.py your.path language.used")
    sys.exit(-1)
file_path = sys.argv[1]
language = sys.argv[2]

monText = open("%s/tts.txt"%file_path,"r+")
text= monText.read()
monText.close()

tts = gTTS(text.decode('utf-8'), language)
tts.save("%s/tts.mp3"%file_path)

os.system("mplayer %s/tts.mp3"%file_path)
