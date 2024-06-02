# BaseModel définir des modèles de données dans FastAPI
from pydantic import  BaseModel

class  Todo(BaseModel):
    name: str
    description: str
    complete: bool
