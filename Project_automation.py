import os
import subprocess
import json
import commun
from Methods import ejs 


def main():
  type_project = input("Veuillez choisir le projet que vous souhaitez: EJS ou React (ViteJS)")
  type_project = type_project.lower()
  print("Le projet choisi est : ", type_project)
  print("Veuillez créer le dossier de votre projet")
  path = input("Veuillez rentrer le chemin où vous souhaitez sauvegarder le projet (chemin absolu)")


  # Vérification du chemin
  if not path:
    print("Le chemin ne peut pas être vide")
    exit()
  if not os.path.isabs(path):
    print("Le chemin n'est pas absolu. Veuillez entrer un chemin absolu (ex : /home/user/projets ou C:\\Users\\user\\projets).")
    exit()


  name = input("Veuillez rentrer le nom de votre projet : ")
  print("Le chemin que vous souhaitez est : ", path)
  print("Création du dossier...")

  match type_project:
    case "ejs":
      # Construction du chemin complet du dossier projet
      full_path = os.path.join(path, name)
      # Vérification si le dossier existe déjà
      if not os.path.exists(full_path):
        try:
          os.mkdir(full_path)
          # Utilisation de f-string
          print(f"Dossier {name} a été créé à l'emplacement : {full_path}")
        except Exception as error:
          print(f"Une erreur est survenue lors de la création du dossier : {error}")
      else:
        print(f"Le dossier {name} existe déjà à l'emplacement : {full_path}")

      #Changement de chemin actuel
      os.chdir(full_path)
      print(os.getcwd())

      ejs.setup_ejs_project()

    case "react":
      print("Ceci est un projet React")


main()