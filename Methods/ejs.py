import os
import subprocess
import json

import commun

def setup_ejs_project():
    #Installation dépendances
    #ejs et init à enlever pour exclusive à ejs

    subprocess.run("npm init -y", shell=True)
    subprocess.run("npm install ejs", shell=True) 
    subprocess.run("npm install dotenv", shell=True)
    subprocess.run("npm install express", shell=True)
    subprocess.run("npm install pg", shell=True)
    subprocess.run("npm install argon2", shell=True)

    # Stockage du fichier en dict afin de pouvoir le modifier
    with open("package.json", "r") as file:
        data = json.load(file)
        data["scripts"]["dev"] = "node --watch index.js"
        data["type"] = "module"

    with open("package.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

    commun.public()

    commun.environment()

    os.mkdir("app")
    os.mkdir("app/controllers")

    with open("app/controllers/main.controller.js", "w", encoding="utf-8") as file:
        file.write("""// import * as dataMapper from "../models/data-mapper.js"; //Import BDD

    export const mainController = {
    renderHomePage: (req, res) => {
        res.render("index");
    },
    
    //  Ou sinon:
    // export function renderHomePage(req, res) {
    //   res.render("home-view");
    // }
    // async homePage(req, res) { //version DB
    //     try {
    
    //       // récupérer les données des figurines dans la BDD ==> communiquer avec la BDD, on utilise le dataMapper
    //       const figurines = await figurineDataMapper.getAllFigurines(); // [{}, {}, {}]
    
    //       // fournir les données des figurines à la vue pour affichage
    //       res.render("accueil", { figurines });
    
    //     } catch (error) {
    //       console.error(error);
    //       res.status(500).render("errors/500");
    //     }
    //   },

    };
    export default mainController;""")
    
    with open("app/router.js", "w", encoding="utf-8") as file:
     file.write("""// Import de l'usine à routers
    import { Router } from "express";

    // Import du controlleur
    import { mainController } from "./controllers/main.controller.js";

    // Création d'un router
    export const router = Router();

    // === Paramétrage du router ===

    // --- Route / ---
    router.get("/", mainController.renderHomePage);""")
    
    os.mkdir("app/middleware")

    with open("app/middleware/not-found.middleware.js", "w", encoding="utf-8") as file:
        file.write("""export const notFoundMiddleware = (req, res) => {
    res.status(404).render("404");
    };""")

    os.makedirs("app/views/partial")
    os.mkdir("app/models")

    with open("app/models/data-mapper.js", "w", encoding="utf-8") as file:
        file.write("""import client from "./database-client.js";


    const NomAMettre = {
    async Function() {
        const result = await client.query('SELECT * FROM "figurine"'); // { command, rowCount, oid, rows: [{}, {}, {}] }
        const cequetuveux = result.rows; // [{}, {}, {}]
        return cequetuveux;
    },


    };


    export default NomAMettre;""")
    
    with open("app/models/database-client.js", "w", encoding="utf-8") as file:
        file.write("""// Ce fichier défini un CLIENT pg pour notre base de données que l'on utilisera dans nos controlleurs


    // Import des variables du .env (permet d'utiliser process.env)
    import "dotenv/config";


    // import du module pg
    import pg from "pg";


    // Création d'un client Postgres vers notre BDD locale
    const client = new pg.Client(process.env.PG_URL);


    // Connexion du client vers la BDD
    // Création d'un tunnel de connexion vers la BDD
    // client est un objet JS (que l'on va utiliser dans les controlleurs) qui permet de faire des requêtes SQL vers la BDD
    client.connect();


    // Au choix : export par défaut
    export default client;


    // Au choix : export nommé
    export { client };""")
    
    with open("index.js", "w", encoding="utf-8") as file:
        file.write("""import "dotenv/config";
    import express from "express";
    // Import des modules locaux
    import { router } from "./app/router.js";
    import { notFoundMiddleware } from "./app/middleware/not-found.middleware.js";

    const app = express();
    // Configure le view engine
    app.set("view engine", "ejs"); // => pour préciser quel view engine on utilise
    app.set("views", "./app/views"); // => pour préciser à EJS dans quel dossier trouver les fichiers .ejs lors des res.render()

    // Configure le dossier public
    app.use(express.static("./public"));

    // BodyParser permettant d'interpréter des données fournies dans un POST, un PATCH ou un PUT, en tant que JSON. Ces données seront stockées dans req.body
    app.use(express.json());

    // Configurer l'application
    app.use(router);
    app.use(notFoundMiddleware);

    // Lancement du serveur
    const PORT = process.env.PORT || 3000;
    app.listen(PORT, () => {
    console.log(`🚀 Server started on http://localhost:${PORT}`);
    });
    """)
    
    with open("app/views/index.ejs", "w", encoding="utf-8") as file:
        file.write("""<!DOCTYPE html>
    <html lang="fr">
    <head>
    <meta charset="UTF-8" />
    <title>Test EJS</title>
    <link rel="stylesheet" href="/css/index.css" />
    </head>
    <body>
    <div class="centered">
        <h1> Ceci est un test </h1>
    </div>
    </body>
    </html>
    """)
    
    with open("public/css/index.css", "w", encoding="utf-8") as file:
        file.write("""body, html {
    height: 100vh;
    margin: 0;
    }
    .centered {
    height: 100%;
    display: flex;
    justify-content: center; /* centre horizontalement */
    align-items: center;    /* centre verticalement */
    font-family: Arial, sans-serif;
    margin: auto;
    }

    .centered h1 {
    font-size: 36px;
    margin: 0;
    }
    """)

    with open("app/views/404.ejs", "w", encoding="utf-8") as file:
        file.write("""<!DOCTYPE html>
    <html lang="fr">
    <head>
    <meta charset="UTF-8" />
    <title>Test EJS</title>
    <link rel="stylesheet" href="/css/index.css" />
    </head>
    <body>
    <div class="centered">
        <h1> Ceci est la page 404 </h1>
    </div>
    </body>
    </html>
    """)

    subprocess.run("code .", shell=True)
    exit()