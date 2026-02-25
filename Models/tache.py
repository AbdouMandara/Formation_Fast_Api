# dans ce modèle on fait le lien avec la bdd
from sqlalchemy import Column, Integer,String, Date # je récupères des types 

# J'importe la variable Base créé dans database.py car elle sera la base de tous les modèles
from database.database import Base

class Tache(Base) :
    __tablename__ = "Tache" # Nom de la table
    # Je définis une colonne pour ma table en utilisant Column()
    id = Column(Integer, primary_key=True, index=True) #on met index = True pour mettre un index dessus car on va faire la recherche par rapport à l'id
    titre = Column(String)
    etat = Column(String)
    date_echeance = Column(Date)
    date_creation = Column(Date)
    date_mise_a_jour = Column(Date)