import os

print("Veuillez créer le dosssier de votre projet")
path = input("Veuillez rentrer le chemin où vous souhaitez sauvegarder le projet (chemin absolu) ")
name = input("Veuillez rentre le nom de votre projet ")
print("Le chemin que vous souhaitez est : ", path)
print("Création du dossier...")
# Construction du chemin complet du dossier projet
full_path = os.path.join(path, name)
# check si le dossier existe déjà
if not os.path.exists(full_path):
  os.mkdir(full_path)
  # Utilisation de f-string
  print(f"Dossier {name} a été créé !")
else:
  print(f"Dossier {name} existe déjà à l'emplacement : {full_path}")
