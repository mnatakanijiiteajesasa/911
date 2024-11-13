from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://<dbunew>:<L7Dk1UjrdgMYyYOw>@diggy.rug2w.mongodb.net/?retryWrites=true&w=majority&appName=Diggy"

# new client and connection to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)