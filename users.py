from pymongo.mongo_client import MongoClient
import requests

uri = "mongodb+srv://mdbuser:h0FlUMAFTQ5l0Sgt@tgusers.er3ttn0.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client['TeleUsers']
collection = db['TeleAuth']
# user login

def is_auth(uname):
    query = {"_id": uname}
    result = collection.find_one(query)
    return result

def login(uname, api_key):
    d_check=is_auth(uname)
    if d_check == None:
        document = {'_id': uname,'api_key': api_key}
        collection.insert_one(document)
        return True
    else:
        return False
    
def logout(uname):
    query={'_id': uname}
    result = collection.find_one(query)
    if result != None:
        collection.delete_one(query)
        return True
    else:
        return False

# link generator 
def link_gen(uname, long_link):
    if is_auth(uname) != None:
        query={"_id":uname}
        res=collection.find_one(query)
        api_key=res['api_key']
        url=f"https://tgshortener.com/api?api={api_key}&url={long_link}&format=text"
        resp=requests.get(url)
        return resp.text
    else:
        return "Please Login First"





