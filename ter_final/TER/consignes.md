# Organisation du projet:

+ 1 répertoire /wakeword/snowboy/ 
	+ scrip.py point d'entré (param: chemin vers fichier du mot clé, niveau de tolérance, ...)
	+ sortie: rien, effet de bord: mot clé détecté. (script bloquant)
+ /VAD/nomscript/
	+ scrip.py point d'entré (param: chemin vers fichier audio)
	+ sortie: réponse binaire enregistrement fichier(besoin de continuer le script ou pas)
+ /STT/GSpeechAPI/
	+ scrip.py point d'entré (param: chemin vers fichier audio, et langue de l'enregistrement)
	+ sortie: texte brut 
	+répertoire credential permettant l'execution(lien relatif)
+ /NLU/DialogFlow/
	+ scrip.py point d'entré (param: langue, texte, session_id?)
	+ sortie: le json en texte brut
	+répertoire credential permettant l'execution
+ /Action/...
+ /TTS/GTTS/
