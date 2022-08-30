import pymongo

client = pymongo.MongoClient("mongodb+srv://Pranit:Pranit2000@pranit.rhzdita.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"pranit",
    "email" : "anappranit@gmail.com",
    "surname" : "anap"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )

