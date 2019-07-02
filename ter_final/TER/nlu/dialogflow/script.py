import argparse
import uuid
import sys
import dialogflow
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credential/credential.json"

#load arguments:
if len(sys.argv) <= 3:
    print("Error: need to specify file path, language and session Id")
    print("Usage: python script.py your.path language.used session.id")
    sys.exit(-1)
txt_path = sys.argv[1]
language = sys.argv[2]
session = sys.argv[3]

def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversaion."""
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    for text in texts:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(
            session=session, query_input=query_input)

        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text.encode('utf-8')))
        print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text.encode('utf-8')))
        print('mon test:', response.query_result.parameters)
        #Enregistrement dans fichier
        myFile= open("%s/nlu.txt"%txt_path,"w+")
        myFile.write('Query: {}\n'.format(response.query_result.query_text.encode('utf-8')))
        myFile.write('Intent: {}\n'.format(response.query_result.intent.display_name))
        myFile.write('Fulfillment: {}\n'.format(
            response.query_result.fulfillment_text.encode('utf-8')))
        myFile.write('{}'.format(response.query_result.parameters))
        myFile.close()


monText = open("%s/file.txt"%txt_path,"r+")
txt= monText.read()
detect_intent_texts("rpi-dhrnpg","ID%s"%session,[txt],language)
monText.close()
