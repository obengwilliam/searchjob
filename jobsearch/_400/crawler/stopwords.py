from pymongo import MongoClient

connection=MongoClient()
db=connection.jobsdbs
collection=db.crawler_stopword
import csv

with open('stopwords.csv','rb') as sw:
     read=csv.reader(sw)
     for i in read:
         stopword={"words":''.join(i)}
         print stopword
         collection.insert(stopword)
         
