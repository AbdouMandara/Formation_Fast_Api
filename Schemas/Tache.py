from pydantic import BaseModel, Field
from enum import Enum

class Etat(str, Enum):
    AFAIRE = "A faire"
    TERMINE = "Terminé"
    EN_COURS= "En cours"
    
class Tache(BaseModel) :
    id : int
    titre : str = Field(min_length=1)
    description : str = Field(min_length=5)
    etat : Etat