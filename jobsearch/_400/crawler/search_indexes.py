

def add_to_search_index(keyword,url,title,body):
  
  try:
        
        from pymongo import MongoClient
        
        connection=MongoClient()
       
  except:
        print 'connection problem'
  db=connection.jobsdbs
  
  

  
#try:    
  if db.crawler_index.find_one({'keyword':keyword}):
        db.crawler_index.update({"keyword":keyword},{"$addToSet":{"urls":url}})
  else:
        db.crawler_index.insert({'keyword':keyword,'urls':[url]})
  if  not db.crawler_page_info.find_one({'url':url}):
      db.crawler_page_info.insert({'title':title,'body':body,'url':url})
    
#except:
#   print 'problem making index'  
