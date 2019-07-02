import sys
from modules.weather import weather

#load arguments:
if len(sys.argv) <= 1:
    print("Error: need to specify file path")
    print("Usage: python script.py your.path ")
    sys.exit(-1)
file_path = sys.argv[1]

def parse(file_path):
    with open("%s/nlu.txt"%file_path) as fp:
        mydict = {}
        for line in fp:
            if("Query:" in line):
                query = line[7:]
            if("Intent:" in line):
                intent = line[8:].rstrip()
            if("Fulfillment:" in line):
                fulfill = line[13:]
            if("key:" in line):
                key = line[8:-2]
            if("string_value:" in line):
                val = line[19:-2]
                mydict[key] = val
        return(intent, mydict, fulfill)

#autres fonctions a implementer


def processAction(intent, fields, fulfillment):

    print(intent)
    print(fields)

    if(intent=="weather" and fields['geo-city']!=""):
        fulfillment = weather.getWeatherResponse(fields['geo-city'], fields['date'])

    return(fulfillment)


if __name__ == '__main__':

    #variable globale d'intent:
    intent = ""
    #dictionnaire qui sera utilise pour les Actions
    dictionnaire = {}
    fulfillment = ""
    (intent, dictionnaire, fulfillment) = parse(file_path)
    monText = open("%s/tts.txt"%file_path,"w+")
    monText.write(processAction(intent, dictionnaire, fulfillment))
    monText.close()
    print("File written")
