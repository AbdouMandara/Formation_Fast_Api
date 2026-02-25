from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
dict_students = {
    1 : {
        "nom" : "Abdou",
        "age" : 18,
        "annee" : "Niv 2",
    },
    2 : {
        "nom" : "Lass",
        "age" : 10,
        "annee" : "Niv 2"
    },
    3 : {
        "nom" : "Akko",
        "age" : 22,
        "annee" : "Niv 2",
    }
}

@app.get("/")
def index():
    return {"nom" : "Premier nom"}

# path parameters
@app.get("/get-student/{student_id}")
def get_student(student_id:int = Path(description="L'id du student qu'on veut voir", gt=0, lt=10)):
    #**gt** veut dire que la valeur de student_id doit etre plus grand que 0 et ls veut dire moins que grand que 2
    return  dict_students[student_id]

# Query parameters
@app.get("/get-by-name")
def get_student_by_name(*,name :Optional[str] = None, test : int) : # :Optional[str] = None sert à rendre ce paramètre facultatif donc on peut executer une action sur cette endpoint sans donner de valeur à name c'est la méthode recommandé par FastAPI
    for student_id in dict_students :
        if dict_students[student_id]["nom"] == name :
            return dict_students[student_id]
    return {"Message" : "Utilisateur non trouvé"}

# Combinaison des path parameters et des query parameters
@app.get("/get-by-name/{student_id}")
def get_student_by_path_and_query_parameters(*,student_id: int,name :Optional[str] = None, test : int) : # :Optional[str] = None sert à rendre ce paramètre facultatif donc on peut executer une action sur cette endpoint sans donner de valeur à name c'est la méthode recommandé par FastAPI
    for student_id in dict_students :
        if dict_students[student_id]["nom"] == name :
            return dict_students[student_id]
    return {"Message" : "Utilisateur non trouvé"}

# Request Body and post method*
class Student(BaseModel) :
    name : str
    age : int
    annee : str
    
@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student) :
    if student_id in dict_students :
        return {"Erreur" : "Etudiant existe"}
    dict_students[student_id] = student # Y A erreur signalé à cause de l'extension mais ça marche
    return dict_students[student_id]

# Methode Put : ça sert à mettre à jour une ressource qui existe
class UpdateStudent(BaseModel) :
    # On a créé cette class car on veut pas forcément tout mettre à jour chez le student
    name : Optional[str] = None
    age :  Optional[int] = None
    annee :  Optional[str] = None
    
@app.put("/update-students/{student_id}")
def update_student(student_id : int, student : UpdateStudent):
    if student_id not in dict_students :
        return {"Erreur" : "Ce user n'existe pas"}
    
    if student.name != None:
        dict_students[student_id]["nom"] = student.name
    if student.age != None:
        dict_students[student_id]["age"] = student.age
    if student.annee != None:
        dict_students[student_id]["annee"] = student.annee
    return dict_students[student_id]

# La méthode Delete
@app.delete("/delete-student/{student_id}")
def delete_student(student_id : int):
    if student_id not in dict_students : 
        return {"Erreur" : "Ce user n'existe pas"}
    del dict_students[student_id]
    return{"Message" : "Ce user a été supprimé avec succès"}
