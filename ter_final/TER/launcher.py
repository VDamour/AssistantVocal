import os
import signal
import sys
import subprocess
import random

#donnees du mot cle
current_wakeword = "snowboy" #l'api utilisee
model_name = "alexa_best.umdl" #le model utilise pour le mot cle
wsensitivity = 0.5 #sensibilite du model allant de 0 a 1

#donnees pour la VAD
current_vad = "self_made_vad"
file_path = os.getcwd()

#donnees pour le stt
current_stt = "google_speech_api"
language = 'fr-FR'

#donnees pour le NLU
current_nlu = "dialogflow"

#donnees bloc Actions
current_actions = "test_action"

#donnees TTS
current_tts = "gtts"


print(file_path)

def launch_wakeword(cur_wake, mod_name,  wsensit):
    print("Wakeword detection:")
    #os.system("rm file.raw") #suppression des donnees des anciennes demandes
    #print(os.getcwd()) #recuperation position actuelle
    detected=(os.system("python wakeword/%s/script.py wakeword/%s/resources/%s %s" %(cur_wake, cur_wake, mod_name, wsensit)))
    #print(test) #recuperation sortie: 0 si tout s'est bien passe autre int sinon
    if(detected==0):
        print("Detected!")
        print("...................................")
        launch_vad(current_vad, file_path)
        return True
        os.system("rm file.txt")
    else:
        return False

def launch_vad(cur_vad, file_path):
    print("Voice Activity Detection:")
    #suppression de l'ancien fichier enregistre:
    vad = (os.system("python vad/%s/script.py %s/" %(cur_vad, file_path)))
    print("...................................")

def launch_stt(cur_stt, file_path, lang):
    print("Speech To Text:")
    os.chdir("stt/%s/" %cur_stt)
    os.system("python script.py %s %s" %(file_path, lang))
    os.chdir(file_path)
    #os.system("rm file.raw") #suppression des donnees des anciennes demandes
    print("...................................")
    if(fileCheck("file.txt")):
        launch_nlu(file_path, lang, random.randint(100,10000))

def launch_nlu(txt_path, lang, session_id):
    print("Natural Language Understanding")
    global current_nlu
    os.chdir("nlu/%s/" %current_nlu)
    os.system("python script.py %s %s %s"%(txt_path, lang, session_id))
    os.chdir(txt_path)
    print("...................................")

def launch_actions(file_path, current_actions):
    print("Actions")
    os.system("python action/%s/script.py %s"%(current_actions,file_path))
    os.chdir(file_path)
    print("...................................")

def launch_tts(file_path, current_tts, lang):
    print("Text to Speech:")
    os.chdir("tts/%s/" %current_tts)
    os.system("python script.py %s %s"%(file_path, lang))
    os.chdir(file_path)
    print("...................................")


#verifie si un fichier existe ou non
def fileCheck(fn):
    try:
      open(fn, "r")
      return True
    except IOError:
      return False

def main():
    print(" ===================================================")
    print("||=================================================||")
    print("||       Bonjour, dites \'Alexa\' pour demarer       ||")
    print("||=================================================||")
    print(" ===================================================")
    test = launch_wakeword(current_wakeword,  model_name, wsensitivity)
    if(fileCheck("file.raw")):
        launch_stt(current_stt, file_path, language)
        launch_actions(file_path, current_actions)
        launch_tts(file_path, current_tts, language)
    return(test)

if __name__ == '__main__':
    #premier lancement pour la gestion de la boucle
    test = main()
    while test:
        test=main()
