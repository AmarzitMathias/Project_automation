import os
import subprocess
import json
from pathlib import Path
import commun

def setup_react_project(name):

    # Nettoyage du nom pour package.json name
    valid_name = name.strip().lower().replace(" ", "-")

    # Création du projet React avec ViteJS
    subprocess.run(
        f"pnpm create vite {name} --template react-ts",
        shell=True,
        input=f"{valid_name}\n",
        text=True
    )
    # Se placer dans le dossier du projet
    os.chdir(name)

    # Installation des dépendances
    subprocess.run("pnpm install", shell=True)

    # Création des fichiers d'environnement
    with open(".env", "w", encoding="utf-8") as file:
        file.write("#VITE_API_URL=rentrez l'adresse de votre API \n")
    with open(".env.example", "w", encoding="utf-8") as file:
        file.write("#VITE_API_URL=http://XXX.XXX.XXX.XXX:XXXX \n")
    
    # Ajouter .env au .gitignore
    with open(".gitignore", "a", encoding="utf-8") as file:
        file.write("\n # Ajout par l'automatisation\n.env\n")

    # Création du dossier public et sous-dossiers
    Path("public").mkdir(exist_ok=True)
    (Path("public") / "css").mkdir(exist_ok=True)
    (Path("public") / "image").mkdir(exist_ok=True)
    (Path("public") / "js").mkdir(exist_ok=True)
    
    # Modification du dossier src
    (Path("src") / "components").mkdir(exist_ok=True)
    (Path("src") / "style").mkdir(exist_ok=True)
    (Path("src") / "@types").mkdir(exist_ok=True)
    
    # Ouverture du projet dans VSCode
    subprocess.run("code .", shell=True)

    # Lancement du serveur de développement
    subprocess.run("pnpm run dev", shell=True)
    
    exit()