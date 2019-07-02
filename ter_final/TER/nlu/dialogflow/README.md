# DialogFlow

La plupart des setups en ligne sur https://dialogflow.com/docs/getting-started/basic-fulfillment-conversation
1. Mise en place de l'agent weather2 en ligne,
2. création d'un répertoire du nom de l'agent et d'un fichier index.js correspondant.
3. Nécessité de créer un Bucket(non précisé dans le tuto):
    + aller sur Google Cloud Project,
    + à droite dans stockage,
    + créer nouveau Bucket: term1info.
4. gcloud beta functions deploy nomProjet --stage-bucket nomBucket --trigger-http.
5. URL à retenir:  https://us-central1-test-1521556446148.cloudfunctions.net/test
6. (optionnel) ajout d'une API externe
    + https://us-central1-test-1521556446148.cloudfunctions.net/weatherWebhook
7. Simplement terminer l'installation en suivant es étapes disponibles sur: https://github.com/dialogflow/dialogflow-python-client-v2




## Problème d'authentification:
Problème d'import lors du lancement de monTest.py qui est sensé vérifier l’authentification.
````bash
+ pip install google-cloud
+ pip install --upgrade protobuf
+ sudo pip install --upgrade protobuf
+ pip install google-cloud
+ sudo pip install --upgrade google-cloud
vérifications:
+ pip show google-cloud
+ python -c "from google.cloud import storage"
(pas d'erreur retournée)
````
Après récupération de la clé essaie de dialog.py: où trouver le session_id?
C'est un identifuant de la cession de communication en cours permettant la réutilisation de contexte et l'identification d'un utilisateur. Il est à attribuer par le programmeur.


### Sources:

suivre tuto de création d'un assistant puis:
+ https://dialogflow.com/docs/getting-started/basic-fulfillment-conversation
+ faire les étapes de 1 à 5: https://cloud.google.com/functions/docs/quickstart
+ installations: https://cloud.google.com/sdk/docs/


##Résultats:
utilisation de la commande:
"python dialog.py"
retourne un "intent" et le format "json" de la réponse.
