import os
import subprocess

print("Veuillez créer le dosssier de votre projet")
path = input("Veuillez rentrer le chemin où vous souhaitez sauvegarder le projet (chemin absolu) ")


# Vérification du chemin
if not path:
  print("Le chemin ne peut pas être vide")
  exit()
if not os.path.isabs(path):
  print("Le chemin n'est pas absolu. Veuillez entrer un chemin absolu (ex : /home/user/projets ou C:\\Users\\user\\projets).")
  exit()


name = input("Veuillez rentre le nom de votre projet ")
print("Le chemin que vous souhaitez est : ", path)
print("Création du dossier...")

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

#Installation dépendances
subprocess.run("npm init -y", shell=True)
subprocess.run("npm install dotenv", shell=True)
subprocess.run("npm install ejs", shell=True)
subprocess.run("npm install express", shell=True)
subprocess.run("npm install pg", shell=True)
subprocess.run("npm install argon2", shell=True)

#Création du gitignore
file = open(".gitignore", "w")
file.write("node_modules/")
file.close()