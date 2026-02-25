from fastapi import FastAPI, Path
from Schemas.Tache import Tache
from sqlalchemy.orm import Session 
from fastapi import Depends
from database.database import SessionLocal
#Ici on gère géneralement les endpoints

#Cette fonction sert à gérer toute la session de la bdd
def get_db() :
    db = SessionLocal() # cette variable contient la sesion de connexion à la bdd
    try :
        yield db # c'est comme return dans une fonction, la dfférence est que return stoppe le script après avoir retourner le résultat alors que yield retourne le résultat sans arreter le script
    finally :
        db.close() # quand j'ai fini d'utiliser la bdd je ferme la connexion        
        
        
app = FastAPI(
    title = "Api de gestion des taches",
    description="""Cette API permet de faire un CRUD complet sur les taches"""
)


"""
db : Session = Depends(get_db)
c'est pour dire que la variable db que j'ai déclaré est un param que je vais utiliser dans ma fonction
db sera une Session qui depend de la fonction get_db qui gère la connexion à la bdd

"""
@app.get("/home")
def get_all_taches(db : Session = Depends(get_db)):
    return {"Message" : "Toutes mes taches"}
@app.get("/")
def index():
    return {"message": "hello je suis FastAPI"}

@app.get("/taches/{tache_id}",
                    summary="Cette route sert à recuperer une tache précise", # Bref résumé de ce que fait cette route
                    description="Pour récuperer les infos d'une tache précise selon son ID", #Description de notre route
                    response_description="Infos d'une tache au format JSON" # Description de ce qu'on doit avoir comme reponse
                    )
def get_taches(tache_id : int =Path(description="ID de la tache")):
    return {
        "id de la tache" : tache_id,
        "Titre de la tache": f"Tache {tache_id}"
    }
    
@app.get("/taches")
def create_tache(t : Tache):
    return{
        "Message" : "tache reçu",
        "La tache est : " : t
    }

@app.put("/taches/{tache_id}")
def update_tache(tache_id : int, t : Tache):
    return {
        "Message" : f"Je vais modifier le num de la tache {tache_id}",
        "Nouvelle valeur " : t
    }
    
@app.delete("/taches/{tache_id}")
def delete_tache(tache_id : int):
    return {
        "Message" : f"Je vais supprimer la tache de num {tache_id}"
    }