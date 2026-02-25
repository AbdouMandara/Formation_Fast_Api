# Ici ça concerne la connexion à la base de données
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# declarative_base est l'objet de base utilisé pour créer les modèles de bdd car chaque est une classe pour pas partire de zéro je l'utilise

# syntaxe de l'url de connexion : "nom_sgbd://nom_user_de_cette_bdd:son_mot_de_passe@l'ordi_sur_lequel_je_me_connecte:numero_du_port_du_sgbd_sur_lequel_il_tourne/nom_de_la_bd_sur_laquelle_je_veux_me_connecter"
DATABASE_URL = "postgresql://user_api_tache:1234@localhost:5432/api_tache" # ne fais jamais ainsi en prod ou quand tu commit
engine = create_engine(DATABASE_URL) # C'est pour établir la connexion

# Chaque fois que je fais un select ou un insert etc ... eh, bien je vais créer une session, pour en créer une : 
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind=engine, # Donc chaque fois qu'une session est effectué alors c'est la bdd relié à la variable "engine" qui est utilisée
)

# Je crées une classe de base pour ne pas partir de 0 chaque fois
Base = declarative_base()