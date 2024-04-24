from learningProject import settings
from pymongo import MongoClient


DB_DETAILS = settings.DATABASES["default"]
# DB_USERNAME = DB_DETAILS["CLIENT"]["username"]
# DB_PASSWORD = DB_DETAILS["CLIENT"]["password"]
DB_HOST = DB_DETAILS["CLIENT"]["host"]
DB_PORT = str(DB_DETAILS["CLIENT"]["port"])
CONNECT = MongoClient(host=DB_HOST, port=int(DB_PORT))
# username= DB_USERNAME, password= DB_PASSWORD
DB = CONNECT[DB_DETAILS["NAME"]]

def if_email_already_exist(email):
    global DB
    table= DB["users"]
    result= table.find_one({"email": email})
    if result!= None:
        return True
    else: 
        return False