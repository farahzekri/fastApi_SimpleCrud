import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupérer le mot de passe à partir des variables d'environnement
password = os.getenv("MONGO_PASSWORD")

# Construire l'URI de connexion avec le mot de passe
uri = f"mongodb+srv://admin:{password}@cluster0.8hkywny.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Accéder à la base de données spécifique
db = client.todo_db

# Accéder à une collection spécifique dans cette base de données
collection_name = db["todo_collection"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
