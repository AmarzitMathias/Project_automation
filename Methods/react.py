import os
import subprocess
import json
from pathlib import Path
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import commun  # Importation des fonctions communes

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

    # Modification du package.json (frontend)
    with open("package.json", "r") as file:
        data = json.load(file)
        data["type"] = "module"
    

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
    
    # Création API
    Path("API").mkdir(exist_ok=True)
    os.chdir("API")
    subprocess.run("npm init -y", shell=True)
    subprocess.run("npm install cors", shell=True) 
    subprocess.run("npm install dotenv", shell=True)
    subprocess.run("npm install express", shell=True)
    subprocess.run("npm install pg", shell=True)
    subprocess.run("npm install argon2", shell=True)
    subprocess.run("npm install sequelize", shell=True)
    subprocess.run("npm install pg-hstore", shell=True)
    subprocess.run("npm install cookie-parser", shell=True)

    # Modification du package.json (API)
    with open("package.json", "r") as file:
        data = json.load(file)
        data["scripts"]["dev"] = "node --watch index.js"
        data["type"] = "module"
    with open("package.json", "w") as file:
        json.dump(data, file, indent=2)

    Path("app").mkdir(exist_ok=True)
    (Path("app") / "controllers").mkdir(exist_ok=True)
    (Path("app") / "middlewares").mkdir(exist_ok=True)
    (Path("app") / "schemas").mkdir(exist_ok=True)
    (Path("data").mkdir(exist_ok=True))
    (Path("data") / "models").mkdir(exist_ok=True)

    with open("app/router.js", "w", encoding="utf-8") as file:
        file.write(
        '// Import de l\'usine à routers\n'
        'import { Router } from "express";\n'
        '\n'
        '// Création d\'un router\n'
        'export const router = Router();\n'
        '\n'
        'router.get("/", (req, res) => {\n'
        '  res.send("Le router est bien fonctionnel !");\n'
        '});\n')
        
    commun.environment()

    #Ecriture du sequelize-client.js
    with open("data/sequelize-client.js", "w", encoding="utf-8") as file:
        file.write(
            'import "dotenv/config";\n'
            'import { Sequelize } from "sequelize";\n'
            '\n'
            'export const sequelize = new Sequelize(\n'
            '    process.env.PG_URL,\n'
            '    {\n'
            '        // Correspondance des champs updatedAt et createdAt\n'
            '        define: {\n'
            '            createdAt: "created_at",\n'
            '            updatedAt: "updated_at",\n'
            '        },\n'
            '        dialect: \'postgres\',\n'
            '    }\n'
            ');\n'
            '\n'
            '// test\n'
            'try {\n'
            '    await sequelize.authenticate();\n'
            '    console.log("Connection has been established successfully.");\n'
            '  } catch (error) {\n'
            '    console.error("Unable to connect to the database:", error);\n'
            '  }\n'
        )
    #Ecriture du index.js de l'API
    with open("index.js", "w", encoding="utf-8") as file:
        file.write(
            'import "dotenv/config";\n'
            'import express from "express";\n'
            '\n'
            '// \n'
            '// Import des modules locaux\n'
            'import { router } from "./app/router.js";\n'
            '\n'
            'import cors from "cors";\n'
            'import cookieParser from "cookie-parser";\n'
            '\n'
            'const app = express();\n'
            '\n'
            '// BodyParser permettant d\'interpréter des données fournies dans un POST, un PATCH ou un PUT, en tant que JSON. Ces données seront stockées dans req.body\n'
            'app.use(express.json());\n'
            'app.use(cors({\n'
            '  credentials: true                 // ⬅️ permet les cookies cross-origin\n'
            '}));\n'
            '// Middleware pour accéder à req.cookies\n'
            'app.use(cookieParser());\n'
            '// Configurer l\'application\n'
            'app.use(router);\n'
            '\n'
            '\n'
            '// Lancement du serveur\n'
            'const PORT = process.env.PORT || 3001;\n'
            'app.listen(PORT, () => {\n'
            '  console.log(`🚀 Server started on http://localhost:${PORT}`);\n'
            '});\n'
     )
        
    os.chdir("..")  # Retour au dossier principal du projet
    # Ouverture du projet dans VSCode
    subprocess.run("code .", shell=True)

    # Lancement du serveur de développement
    subprocess.run("pnpm run dev", shell=True)

    exit()