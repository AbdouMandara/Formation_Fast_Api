from pydantic import BaseModel, Field
from enum import Enum
from datetime import date as Date

class Etat(str, Enum):
    AFAIRE = "A faire"
    TERMINE = "Terminé"
    EN_COURS= "En cours"
    
class TacheCreation(BaseModel) :
    id : int
    titre : str = Field(min_length=1)
    etat : Etat
    date_echeance : Date
    date_creation : Date = Date.today()
    date_mise_a_jour: Date = Date.today()
    description : str = Field(min_length=5)