#!/bin/sh

#sudo apt-get install python-virtualenv python-dev
#python -m virtualenv env
#source env/bin/activate

cd wakeword/snowboy/
sudo apt-get install swig3.0 python-pyaudio sox libatlas-base-dev portaudio19-dev
pip install -r requirements.txt
cd ../../

cd stt/google_speech_api/
pip install -r requirements.txt
cd ../../

cd nlu/dialogflow/
pip install -r requirements.txt
cd ../../

cd tts/gtts
sudo apt-get install mplayer
pip install -r requirements.txt
cd ../../

cd action/test_action/modules/weather
pip install -r requirements.txt
cd ../../../../
