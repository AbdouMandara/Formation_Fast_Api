# A savoir

Pour se connecter à PostgreSQL
**psql -U postgres** , ensuite tu entres le mot de passe dans ton cadre [Abdou] c'est ``1234``, le nom du user par défaut est : postgres

Pour voir les bases de données que j'ai crée , je fais : ```\l``` après le **#**

Pour créer une base de données : **create database nom_de_la_bdd;**

Pour se connecter à une bdd je fais : **\c nom_de_la_bdd**

Je vais me connecter à ma bdd pas en superadmin qui est **postgre** mais je vais créer un user qui n'a accès qu'à cette bdd
**create user nom_du_user with password 'mot_de_passe_de_ton_choix_qui_est_compliqué';**
NB : si ta bdd s'appelle : 'api_tache' mets comme nom de user 'api_tache_user'

Pour voir les users qui existent sur cette bdd, je fais :
**\du**

Pour donner les droits de connexion à mon nouveau user sur cette bdd :
**grant connect on database "nom_de_la_bdd_en_question" to nom_du_user_à_qui_je_veux_attribuer_ce_droit;**

Pour donner les droits d' utilisation à un user sur une bdd précisement sur schema  :
**grant usage on schema public to nom_user;**

Pour donner les droits de création à un user sur une bdd précisement sur schema  :
**grant create on schema public to nom_user;**

Pour donner les privilèges (insert, delete, select, create) à un user sur une bdd précisement sur schema  :
**grant all privileges on all tables in schema public to nom_user;**
Pour donner les droits sur les séquences à un user sur une bdd précisement sur schema  :
**grant all privileges on all sequences in schema public to nom_user;**
Pour donner les droits sur les  fonctions à un user sur une bdd précisement sur schema  :
**grant all privileges on all functions in schema public to nom_user;**

Pour donner les privilèges (insert, delete, select, create) à un user sur une bdd précisement sur les nouvelles tables qui vont etre ajouter  :

**alter default privileges in schema public grant all privileges on tables to nom_user;**
Pour donner les droits sur les sequences à un user sur une bdd précisement sur les nouvelles tables qui vont etre ajouter  :

**alter default privileges in schema public grant all privileges on sequences to nom_user;**
Pour donner les droits sur les fonctions à un user sur une bdd précisement sur les nouvelles tables qui vont etre ajouter  :

**alter default privileges in schema public grant all privileges on functions to nom_user;**

-----------------------------
Maintenant pour me connecter en tant que le nouveau user créer sur nouveau cmd:
**psql -U nom_user -d nom_bdd_à_laquelle_il_a_le_droit_de_se_connecter_uniquement**

EX : psql -U user_api_tache -d api_tache
**NB :** le mot de passe de **user_api_tache** est ````1234```

Etant connecter sur cette bdd pour voir les tables ou relations : **\d** après le **#**

Pour voir le contenu de la table **tache** je fais : \d "tache" créé à partir de mon modèle SQLAlchemy
