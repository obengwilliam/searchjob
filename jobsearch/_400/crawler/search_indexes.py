
print 1

def add_to_search_index(keyword,url):
  
  try:
        
        from pymongo import MongoClient
        
        connection=MongoClient()
       
  except:
        print 'connection problem'
  db=connection.jobsdbs
  
  

  
try:    
  if db.crawler_index.find_one({'keyword':keyword}):
        db.crawler_index.update({"keyword":keyword},{"$addToSet":{"urls":url}})
  else:
        db.crawler_index.insert({'keyword':keyword,'urls':[url]})
    
except:
    print 'problem making index'  
