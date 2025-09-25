# Project_automation

## Présentation

Ce projet permet d'automatiser la création de structures de projets web, au choix en EJS (Express/EJS) ou en React (ViteJS + API Express). Il propose une interface interactive en ligne de commande pour guider l'utilisateur dans la création de son projet.

Lorsque vous lancez le script principal `Project_automation.py`, une interface interactive en ligne de commande vous guide : vous choisissez le type de projet (EJS ou React), le chemin absolu de création et le nom du projet. Le script vérifie l’existence du dossier, le crée si besoin, puis génère automatiquement toute la structure adaptée (routes, contrôleurs, vues, API, etc.), installe les dépendances nécessaires, crée les fichiers d’environnement, puis ouvre le projet dans Visual Studio Code.

Une fois le processus d’automatisation terminé, aucune modification manuelle n’est nécessaire pour obtenir un front-end et un back-end fonctionnels.
Il vous suffit simplement d’exécuter les commandes indiquées dans ce guide pour démarrer et utiliser votre projet immédiatement.

⚠️ En raison de la diversité des bases de données possibles, la configuration de la connexion à la base de données n’est pas automatisée.
Il vous suffit simplement de renseigner l’URL de votre base de données dans le fichier .env généré à la racine du projet (ou dans le dossier API pour l’API).
Le projet sera alors prêt à communiquer avec votre base de données.

 ℹ️ Les sections EJS et React ci-dessous présentent en détail tous les fichiers et dossiers générés automatiquement lors du processus d’automatisation, ainsi que leur utilité dans la structure du projet.

## EJS

### Front-end

- **public/css/index.css**  
  Feuille de style principale pour les vues EJS.
- **index.js**  
  Point d’entrée du front-end EJS, configure le rendu côté client si besoin.
- **.env**  
  Fichier d’environnement pour stocker les variables front-end (ex : URL d’API).

### Back-end

- **package.json**  
  Fichier de configuration Node.js (scripts, dépendances, type de module).
- **app/controllers/main.controller.js**  
  Contrôleur principal, gère la logique pour la page d’accueil.
- **app/middleware/not-found.middleware.js**  
  Middleware pour gérer les erreurs 404 (page non trouvée).
- **app/models/data-mapper.js**  
  Sert d’exemple pour la gestion des requêtes à la base de données (pattern data mapper).
- **app/models/database-client.js**  
  Initialise et exporte le client PostgreSQL pour la base de données.
- **app/router.js**  
  Définit les routes principales de l’application Express.
- **app/views/index.ejs**  
  Vue principale affichée à la racine (`/`), sert de page d’accueil côté serveur.
- **app/views/404.ejs**  
  Vue affichée pour les routes non trouvées, personnalisant la page d’erreur 404.
- **app/views/partial/**  
  Dossier pour les vues partielles EJS, réutilisables dans d’autres vues (ex : header, footer).

### Commandes EJS

La commande ```npm install``` n’a généralement pas besoin d’être relancée, car l’installation des dépendances a déjà été effectuée automatiquement lors du processus d’automatisation de création du projet.

```bash
npm install
npm run dev # Lance le serveur Express en mode développement
```

---

## React

### Front-end

- **src/components/test/Test.tsx**  
  Composant React de test affichant un message, pour vérifier le bon fonctionnement des composants.
- **src/main.tsx**  
  Point d’entrée de l’application React, configure le routage avec React Router et monte l’application.
- **src/style/**  
  Dossier pour les fichiers de styles CSS/SCSS du front-end.
- **src/@types/**  
  Dossier pour les définitions de types TypeScript personnalisées.
- **public/**  
  Dossier pour les fichiers statiques accessibles côté client (images, CSS, JS).
- **public/css/**  
  Feuilles de style CSS globales pour l’application.
- **public/image/**  
  Images utilisées dans l’application.
- **public/js/**  
  Scripts JavaScript additionnels.
- **.env**  
  Fichier d’environnement pour les variables front-end (ex : VITE_API_URL).
- **.env.example**  
  Exemple de fichier d’environnement à partager sans données sensibles.
- **package.json**  
  Fichier de configuration du projet React (scripts, dépendances, type de module).

### Back-end (API)

- **API/**  
  Dossier contenant toute la partie back-end (API Node.js/Express).
- **API/package.json**  
  Fichier de configuration du projet Node.js pour l’API (scripts, dépendances, type de module).
- **API/index.js**  
  Point d’entrée du serveur Express, configure les middlewares, routes, et lance le serveur.
- **API/app/router.js**  
  Définit les routes principales de l’API Express.
- **API/app/controllers/**  
  Dossier pour les contrôleurs Express (logique des routes).
- **API/app/middlewares/**  
  Dossier pour les middlewares Express (gestion des erreurs, authentification, etc.).
- **API/app/schemas/**  
  Dossier pour les schémas de validation ou de données.
- **API/data/sequelize-client.js**  
  Initialise et exporte le client Sequelize pour la connexion à la base de données PostgreSQL.
- **API/data/models/**  
  Dossier pour les modèles de données Sequelize.

### Commandes React

⚠️ Toutes les commandes ci-dessous doivent être lancées depuis le dossier racine du projet (là où se trouve le fichier package.json principal), et non depuis le dossier API.
Les scripts gèrent automatiquement le changement de dossier pour les opérations sur le back-end.
Une commande est présente dans le package.json dans le dossier permettant de le lancer si cela est nécessaire

Les commandes ```pnpm run install-front ``` et ```pnpm run install-back``` ne sont généralement pas nécessaires à relancer, car elles ont déjà été exécutées automatiquement lors du processus d’automatisation de création du projet.

#### Front-end
```bash
pnpm run dev             # Lance le serveur de développement React (Vite)
pnpm run front           # Alias pour le serveur de développement React
pnpm run build           # Construit le projet React pour la production
pnpm run lint            # Analyse le code avec ESLint
pnpm run preview         # Lance un serveur local pour prévisualiser le build
pnpm run install-front   # Installe les dépendances du front-end
```

#### Back-end (API)
```bash
pnpm run install-back    # Installe les dépendances du back-end (API)
pnpm run back            # Lance l'API Express en mode développement
```


## Fonctionnement

Cette section regroupe les commandes essentielles à exécuter pour lancer rapidement le front-end et le back-end des projets générés (EJS ou React).
Utilisez ces commandes pour démarrer votre application après l’automatisation, sans avoir à parcourir tout le guide.

### EJS
```bash
npm run dev    # Lance le serveur Express en mode développement
```

### React
```bash
pnpm run dev         # Pour le front-end
pnpm run back        # Pour le back-end (API)
```