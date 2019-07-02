import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credential/credential.json"
# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import sys

# Instantiates a client
client = speech.SpeechClient()


#load arguments:
if len(sys.argv) <= 2:
    print("Error: need to specify file path and language")
    print("Usage: python script.py your.path language.used")
    sys.exit(-1)

file_path = sys.argv[1]
lang = sys.argv[2]

# The name of the audio file to transcribe
file_name = os.path.join(
os.path.dirname(__file__),
file_path, 'file.raw')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code=lang)

# Detects speech in the audio file
response = client.recognize(config, audio)

for result in response.results:
    monText = open("%s/file.txt"%file_path,"w+")
    monText.write('{}'.format(result.alternatives[0].transcript.encode('utf-8')))
    print('Transcript: {}'.format(result.alternatives[0].transcript.encode('utf-8')))
    monText.close()
