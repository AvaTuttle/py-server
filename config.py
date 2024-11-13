import pymongo
import certifi

con_string = "mongodb+srv://tnt8me:test@cluster0.b5kex.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(con_string, tlsCAFile=certifi.where())
db = client.get_database("organika")