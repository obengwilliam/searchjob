from math import tanh
from pymongo import MongoClient

def dtanh( y):
            return 1.0-y*y

class nn:

       

        def __init__(self):
          self.db=MongoClient().jobsdbs
	#The slope of the function
	#for any output value is specified by this function

        

        #this method is responsible for getting the weight if it exist
        #getting strength for each layer
        #note welll layer 0 respresent the word layer
	def getstrength(self,fromid,toid,layer):
	       if layer==0: 
                       res=self.db.search_wordhidden.find_one({'fromid':fromid,'toid':toid})
		       if res==None:
                                #Now if connection does exist we set default strength for each
				if layer==0: return -0.2
			#if connection exist just return their strength	
		       return res['strength']
	       else: 
		    res=self.db.search_hiddenurl.find_one({'fromid':fromid,'toid':toid})
		    if res==None:
			#if connection does not exist we return 0
			if layer==1: return 0
                    #if connection exist we just return it strength
		    return res['strength']


	#this method is for checking if a connection really exist
	def setstrength(self, fromid,toid,layer,strength):
             
	     if layer==0:
                
                res=self.db.search_wordhidden.find_one({'fromid':fromid,'toid':toid})
               
               
                if res==None:
			self.db.search_wordhidden.insert({'fromid':fromid,'toid':toid,'strength':strength})
                	
		else:
                      
			rid=res['_id']
                        a=self.db.search_wordhidden.update({"_id":rid},{"$set":{"strength":strength}},safe=True)
                        
             else: 
		 
                res=self.db.search_hiddenurl.find_one({'fromid':fromid,'toid':toid})
                if res==None:
			self.db.search_hiddenurl.insert({'fromid':fromid,'toid':toid,'strength':strength})
                	
		else:    
                        
			rid=res['_id']
                        self.db.search_hiddenurl.update({"_id":rid},{"$set":{"strength":strength}},safe=True)

		
	def generatehiddennode(self,wordid,urls):
		if len(wordid)> 3: return None
		#checking if we have a node 
		createkey='_'.join(sorted([str(wi) for wi in wordid]))
		res=self.db.search_hiddennode.find_one({'create_key':createkey})
	        
                #if we dont have a hidden node for it
		if res==None:
                        #creating a hidden node for it and returns the id for it
			cur=self.db.search_hiddennode.insert({'create_key':createkey})
			hiddenid=cur
	        
		
			#Put in some default weights
			for wordi in wordid:
				self.setstrength(wordi, hiddenid,0, 1.0/len(wordid))

			for urlid in urls:

			      self.setstrength(hiddenid,urlid,1,0.1)


        #This function finds all
        #nodes from the hidden layer that are relevant to a specific query
	#to do this we obtain ids from the wordhidden and hiddenurl

	def getallhiddenids(self,wordids,urlids):
		l1={}
		for wordid in wordids:
                        
             		cur=self.db.search_wordhidden.find({'fromid':wordid},{'toid':1})
	                
	                for row in cur: l1[row['toid']]=1

		for urlid in urlids:
             		cur=self.db.search_hiddenurl.find({'toid':urlid},{'fromid':1})
	
                        for row in cur: l1[row['fromid']]=1
                
        	return l1.keys( )



	# The function below is responsible for obtaining the relevant networks based on the weight 
	#This function sets a lot of instance variables for this class 
	#that includes the words,query nodes and urls, the output level of every node , and  using 
	# the functions that are defined earlier.

	def setupnetwork(self,wordids,urlids):
		#value lists
		self.wordids=wordids
		self.hiddenids=self.getallhiddenids(wordids,urlids)
		self.urlids=urlids

		# node outputs
		self.ai = [1.0]*len(self.wordids)
		self.ah = [1.0]*len(self.hiddenids)
		self.ao = [1.0]*len(self.urlids)


		# create weights matrix
		self.wi = [[self.getstrength(wordid,hiddenid,0) for hiddenid in self.hiddenids] for wordid in self.wordids ]
		self.wo = [[self.getstrength(hiddenid,urlid,1) for urlid in self.urlids ]  for hiddenid in self.hiddenids ]
	
	def feedforward(self):
		# the only inputs are the query words
		for i in range(len(self.wordids)):
			self.ai[i] = 1.0
		# hidden activations
                
		for j in range(len(self.hiddenids)):
			sum = 0.0
                           
			for i in range(len(self.wordids)):
                        	
		        	sum = sum + self.ai[i] * self.wi[i][j]
                 
			self.ah[j] = tanh(sum)*10
             
		# output activations
		for k in range(len(self.urlids)):
			sum = 0.0
                       
			for j in range(len(self.hiddenids)):
                                
				sum = sum + self.ah[j] * self.wo[j][k]
                        
			self.ao[k] = tanh(sum)

		return self.ao[:]



 	# function that will set up the network and use feedforward
	#to get the outputs for a set of words and URLs:

	def getresult(self,wordids,urlids):
                
		self.setupnetwork(wordids,urlids)
		return self.feedforward( )


	def backPropagate(self, targets, N=0.5):
                # calculate errors for output
		output_deltas = [0.0] * len(self.urlids)
		for k in range(len(self.urlids)):
			error = targets[k]-self.ao[k]
			output_deltas[k] = dtanh(self.ao[k]) * error
		# calculate errors for hidden layer
		hidden_deltas = [0.0] * len(self.hiddenids)
		for j in range(len(self.hiddenids)):
		 	error = 0.0
		        for k in range(len(self.urlids)):
				error = error + output_deltas[k]*self.wo[j][k]
		        hidden_deltas[j] = dtanh(self.ah[j]) * error

	

		# update output weights
		for j in range(len(self.hiddenids)):
			for k in range(len(self.urlids)):
				change = output_deltas[k]*self.ah[j]
				self.wo[j][k] = self.wo[j][k] + N*change




		# update input weights
		for i in range(len(self.wordids)):
			for j in range(len(self.hiddenids)):
				change = hidden_deltas[j]*self.ai[i]
				self.wi[i][j] = self.wi[i][j] + N*change

	def trainquery(self,wordids,urlids,selectedurl):
			# generate a hidden node if necessary
			self.generatehiddennode(wordids,urlids)
			self.setupnetwork(wordids,urlids)
			self.feedforward( )
			targets=[0.0]*len(urlids)
			targets[urlids.index(selectedurl)]=1.0
			error = self.backPropagate(targets)
			self.updatedatabase()
			


	def updatedatabase(self):
                       
			# set them to database values
			for i in range(len(self.wordids)):
				for j in range(len(self.hiddenids)):
					self.setstrength(self.wordids[i],self. hiddenids[j],0,self.wi[i][j])
				
			for j in range(len(self.hiddenids)):
				for k in range(len(self.urlids)):
					self.setstrength(self.hiddenids[j],self.urlids[k],1,self.wo[j][k])
					
					





if __name__=="__main__":
	def getresult(self,wordids,urlids):
			setupnetwork(wordids,urlids)
                        return feedforward( )





	
