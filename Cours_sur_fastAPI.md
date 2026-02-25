# A savoir

Le point d'entrée de notre app est le fichier : **main.py**

On importe :

- **HTTPException** pour rélever les erreurs propres à l'api
- **Query** et **parse** pour documenter parfaitement les paramètres d'entrés

Quand tu as un paramètre obligatoire **required** après un paramètre facultatif **Optionnal** alors tu dois mettre avant ça **un astérix**
**Exemple :** def get_student_by_name(*,name :Optional[str] = None, test : int) :

Sinon tu auras une erreur

## Différence entre Path Parameters et Query Parameters

- Path Parameters : ce sont les paramètres récuperés depuis l'url
**exemple :** /book/update/{id_du_livre}

- Query Parameters : ce sont les paramètres récuperés sans les passer par l'url
**exemple :** /book/search?nom_livre=le_nom_du_livre

## Connaissances

- SQLAlchemy est un ORM
- Alembic : Pour créer au niveau de la base de données les structures de modèles que j'aurai déclaré dans python
- Pydantic : bibliothèque python intégré à FastAPI pour valider les données entre le client et le serveur donc on va définir le type des données de nos modèles
Grace à pydantic je vais m'assurer que le client m'envoie ce dont j'ai besoin, si je m'attends à un **int** alors je dois avoir un **int** sinon pydantic va rejeter la donnée

## Structuration du projet

- main.py : c'est où on déclare l'instance de FastAPI et les routes principales
- schemas/ : c'est le dossier où on définit les modèles Pydantic | donc ça concerne la communication entre le serveur et le client (front-end)
- models/ : c'est le dossier où on définit les modèles SQLAlchemy | donc ça concerne la communication entre le serveur et la base de données
- crud/ : c'est le dossier où on définit les fonctions pour le CRUD (Create, Read, Update, Delete) ["cest pas une convention de faire ça il fait cela pour que main.js ne soit pas surcharger et que le code soit propre"]
- data/ : contient les fichiers de données
- requirements.txt : contient la liste des packages installés dans notre environnement pour reproduire notre environnement virtuel,
pour celà la commande qu'on fait est **pip freeze >  requirements.txt**
Donc en gros avec len fichier **requirements.txt** quand tu récupères un projet tu crées ton environnement virtuel, ensuite tu installes les packages de ce fichier en faisant : **pip install requirements.txt**

### Commandes à savoir

Pour voir la liste des packages installés dans ton environnement virtuel : **pip list** , si tu veux voir avec les versions : **pip freeze**

#### Pydantic : Gestion des modèles

Grace à lui :

- Définition des modèles de données
- Validation automatique des données entrantes en lien avec le modèle en question
- convertir les données dans le bon **type** si c'est possible genre il peut convertir "1"en 1 donc en int

#### Psycopg2

Elle sert à utiliser **PostgreSQL** dans un environnement Python

#### SqlAlchemy

c'est un ORM (Object-Relational Maping) il va nous permettre de manipuler la bdd avec des objets au lieu d'utiliser du SQL pure. Comme c'est Python on écrira en Python et il s'occupe de génerer le SQL correspondant
**Son role :** Il nous permettra de relier FastAPI et PostgreSQL, il nous évitera la possibilité de faire des injections SQL sur notre app car elle intègre des requetes préparées
```Ìnjection SQL``` : c'est lorsque
pour l'installer : **pip install sqlalchemy**

#### Alembic

C'est l'outil officiel d'Alembic qui permet de créer les tables dans nos bdd en fonction des modèles qu'on a défini et de versionner la structure de la bdd (comme git). Donc tu peux revenir à une version de ta bdd grace à lui si tu veux

Grace à lui les bdd et les modèles seront toujours cohérents

C'est bien d'utiliser **Alembic** avant de créer des tables à travers ton SGBD car sinon Alembic n'est pas au courant de ce que t'as créé et ne prend pas ça en compte et ça peut génerer des erreurs

pour l'installer : **pip install alembic**
Pour initialiser **alembic init alembic** on fait : **pip** ça veut dire que Alembic va créer son répertoire pour stocker les différentes versions
Après avoir installer **alembic** je vais à la ligne 89 du fichier 'alembic.ini' je remplace par les bonnes infos
**Ex :** sqlalchemy.url = postgresql://user_api_tache:1234@localhost:5432/api_tache
Nb : **Alembic** par défaut va prendre en compte les modèles qui héritent de la classe ````Base```
Ensuite je pars dans **env.py** j'importe mes modèles pour que Alembic puisse les prendre en compte et les génerer dans la bdd
**Ex :** from models.tache import Tache
Ensuite je vais à la ligne 22 de ce même fichier et je remplace**target_metadata = None** par : **target_metadata = Base.metadata** car je veux que Alembic prenne en compte tous les modèles qui héritent de la classe ```Base``` et pas seulement un modèle en particulier enfin de génerer ces tables dans la bdd
Dans le cmd, je fais :**alembic revision** ensuite **alembic revision autogenerate -m "le message que tu veux"** pour créer une nouvelle version de la bdd (un peu comme git) en fonction des modèles que j'ai défini
Pour voir ma migration comme "créer la table tache" je vais dans  alembi/versions/ et je vois le fichier de migration que je viens de créer

Ensuite je fais : **alembic upgrade head** pour appliquer les changements dans la bdd
