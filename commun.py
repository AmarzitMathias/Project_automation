import os
from pathlib import Path

def environment():
# Ajout d'un.env et .env.example
    with open(".env", "w", encoding="utf-8") as file:
        file.write("PORT=3000 \n PG_URL=postgres://user:password@localhost:5432/db")
    with open(".env.example", "w", encoding="utf-8") as file:
        file.write("PORT=XXXX \n PG_URL=postgres://user:password@localhost:5432/db")

def public():
    Path("public").mkdir(exist_ok=True)
    (Path("public") / "css").mkdir(exist_ok=True)
    (Path("public") / "image").mkdir(exist_ok=True)
    (Path("public") / "js").mkdir(exist_ok=True)

def gitignore():
    #Création du gitignore
    file = open(".gitignore", "w")
    file.write("node_modules/\n.env")
    file.close()