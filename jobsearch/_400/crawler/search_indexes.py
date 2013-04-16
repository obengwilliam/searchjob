

def add_to_search_index(keyword,url,title,body,location,count):
  '''
    (str(),str(),str(),str(),str(),str())->
  '''  
  try:
        
        from pymongo import MongoClient
        
        connection=MongoClient()
        db=connection.jobsdbs
        assert db.connection==connection
        
       
  except:
        print 'connection problem'

  
        

  
  page_id=''
  
  if  not db.crawler_page_info.find_one({'url':url}):
      		page=db.crawler_page_info.insert({'title':title,'body':body,'url':url})
                page_id=page
  else:
             page_id=db.crawler_page_info.find_one({'url':url})['_id']
              
  if not db.crawler_index.find_one({'keyword':keyword}):
        
        db.crawler_index.insert({'keyword':keyword,'doc':[{'id':page_id,'location':[location],'count':count}]},safe=True)
   
  
  elif db.crawler_index.find_one({'keyword':keyword,'doc.id':page_id}) 	:
	
        db.crawler_index.update({"keyword":keyword, 'doc.id':page_id},{"$addToSet":{"doc.$.location":location}},safe=True)
  elif db.crawler_index.find_one({'keyword':keyword}):
       
         

        db.crawler_index.update({'keyword':keyword},{'$addToSet':{'doc':{'location':[location], 'count':count, 'id':page_id}}},safe=True)

  



    
#except:
#   print 'problem making index'  
