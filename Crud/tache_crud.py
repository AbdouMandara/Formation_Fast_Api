from fastapi import HTTPException
from Schemas.TacheCreation import TacheCreation
from Schemas.Tache_mise_a_jour import TacheMiseAJour
from Models.tache import Tache
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select #ça va servir au niveau de l'affichage des données de la bdd
# Je mets db car j'ai besoin de la bdd
def create_tache(t : TacheCreation, db : Session):
    try : 
        db_tache = Tache(
            titre = t.titre,
            etat = t.etat.value, #car etat est un enum
            date_echeance = t.date_echeance,
            date_mise_a_jour = t.date_mise_a_jour,
            date_creation = t.date_creation,
            description = t.description
        )
        db.add(db_tache) #SQLAlchemy va faire en arrière-plan le "insert into"
        db.commit() # je valide la transaction pour que l'insert soit dispo dans la bdd
        db.refresh(db_tache) #il va automatiquement remplir les infos non mentionnées comme id car c'est auto_increment
        return {
            "Succès" : "Tache crée avec succès"
        }
    except SQLAlchemyError as e :
        db.rollback() # pour annuler la transaction en cours et revenir à l'état précédent de la bdd
        print("Erreur lors de la création de la tache : ", e)
        raise
    
def update_tache(id : int, t : TacheMiseAJour, db : Session):
    try : 
                
        # M-à-j
        db_tache = Tache(
            titre = t.titre,
            etat = t.etat.value, #car etat est un enum
            date_echeance = t.date_echeance,
            date_mise_a_jour = t.date_mise_a_jour,
            description = t.description
        )
        pass
    except SQLAlchemyError as e:
        db.rollback() # pour annuler la transaction en cours et revenir à l'état précédent de la bdd
        print("Erreur lors de la mise à jour de la tache : ", e)
        raise
        

def get_taches(db : Session): #Pour récuperer toutes les taches
    resultats = db.execute(select(Tache).order_by(Tache.date_creation.desc()))
    Taches = [row[0] for row in resultats.all()] #pour stocker les taches dans une liste
    
    taches_data =[]
    for tache in Taches :
        taches_data.append(
            {
                "id" : str(tache.id),
                "titre" : str(tache.titre),
                "description" : str(tache.description),
                "date_echeance" : tache.date_echeance,
                "date_creation" : tache.date_creation,
                "date_mise_a_jour" : tache.date_mise_a_jour,
            }
        ) 
    return taches_data
"""
def get_tache(id : int, db : Session): #elle va permettre de récuperer une tâche grace à l'id
    pass

"""
def delete_tache(id : int, db : Session):
    try : 
        tache_id = id #on récupère l'id du user pris en paramètre
        result = db.execute(select(Tache).where(Tache.id == tache_id))
        tache = result.scalars().first()
        
        if not tache :
            raise HTTPException(status_code = 404, detail ="Tache non existante")
        db.delete(tache)
        db.commit()
        return{
            "Succès" : f"Suppression de tache {id} avec succès"
        }
    except SQLAlchemyError as e:
        print (f"Erreur de création {e}")