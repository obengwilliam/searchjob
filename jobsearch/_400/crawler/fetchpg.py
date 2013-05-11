from urllib2 import urlopen,Request,URLError,HTTPError
import  robotexclusionrulesparser as parse_robot
from urlparse import urlparse ,urljoin
from bs4 import BeautifulSoup as soup
from httplib import BadStatusLine
from urllib import quote

from responses import check_response
from pymongo import MongoClient
from bson.objectid import ObjectId



import socket
import sys
import traceback

# timeout in seconds
timeout = 10
socket.setdefaulttimeout(timeout)



try:
	'''
        	Making a global connection to the Mongodb database
	'''
        from pymongo import MongoClient
        
        connection=MongoClient()

        db=connection.jobsdbs
	
 	assert db.connection==connection
       
except:
        print 'connection problem in start_Crawler.py'


 
def get_page(url):
        try:
            
            parse_dict=urlparse(url)
           
            if parse_dict.scheme:
            
                base_url=parse_dict.scheme + '://'+ parse_dict.netloc
                robot_url=urljoin(base_url,'/robots.txt')
                parse_robot.user_agent='jooble 1.1(http://about.me/jooble)'
            
                robot_parse=parse_robot.RobotFileParserLookalike()
                
                robot_parse.set_url(robot_url)
            
                
                robot_parse.read()
            
        
                if not robot_parse.can_fetch('jooble1.1 http://about.me/jooble', url):
                    print "This seed page can not be crawled based on robot.txt"
                    db.crawler_web_statistic.update({"_id":ObjectId("517dc20440ade61b20becb7d")},{"$inc":{"Number_of_excluded_urls":1}},safe=True)
                    return soup('','lxml'),''
                
                else:
                        #counting number of robot.txt accepted
                        db.crawler_web_statistic.update({"_id":ObjectId("517dc20440ade61b20becb7d")},{"$inc":{"Number_of_robotstxt_request":1}},safe=True)


	
                        # This is where we count the number of urls that did not allow us not to crawl
                        useragent='jobcrawler 1.1 http://about.me/jooble'
                        #headers={'User-Agent':useragent}
                        ##quote(url, safe="%/:=&?~#+!$,;'@()*[]" does not really work well
                        request=Request(url)
                        request.add_header('User-Agent', useragent)
                        
                        try:response=urlopen(request)
                        except URLError: response=urlopen(quote(url, safe="%/:=&?~#+!$,;'@()*[]" ))

		        #updating the database on http request made
			if response:
                        	db.crawler_web_statistic.update({"_id":ObjectId("517dc20440ade61b20becb7d")},{"$inc":{"Number_of_Http_Request":1}},safe=True)
                        else:
				db.crawler_web_statistic.update({"_id":ObjectId("517dc20440ade61b20becb7d")},{"$inc":{"Number_of_Http_Request":1}},safe=True)


				
                        
                        if response.info().type not in ['text/html']:
                            return soup('','lxml'),''
                        the_page=response.read()
                        
                      
                        return soup(the_page,'lxml'),url
                    
                        
                    
                    
              
        
        except URLError as connection_error:
            
             print 'FAILED TO REACH SERVER::'+url,
             	
             db.crawler_http_status_errors.update({"_id":ObjectId("5180bfa440ade62017d1120c")},{"$inc":{"Url_errors":1}},safe=True)

             db.crawler_error_log.insert({'error_type':str(sys.exc_info()),'from_module':str(__file__)})
             return soup('','lxml'),''


        except HTTPError as _400_to_500:
                        print "The server coudnot fulfill the request"
                        print 'Error code:',check_response(_400_to_500.code),_400_to_500.reason
                        db.crawler_http_status_errors.update({"_id":ObjectId("5180bfa440ade62017d1120c")},{"$inc":{"from_400_500":1}},safe=True)
                        db.crawler_error_log.insert({'error_type':str(sys.exc_info()),'from_module':str(__file__)})
                        return soup('','lxml'),''

        except BadStatusLine:
                        print "BadStatusline...................Status Code is unknown"
                        db.crawler_error_log.insert({'error_type':str(sys.exc_info()),'from_module':str(__file__)})
                        db.crawler_http_status_errors.update({"_id":ObjectId("5180bfa440ade62017d1120c")},{"$inc":{"Bad_status_line":1}},safe=True)
                        return soup('','lxml'),''
        except socket.timeout:
                        print "SocketTimeout...................Fail"
                 
                        db.crawler_http_status_errors.update({"_id":ObjectId("5180bfa440ade62017d1120c")},{"$inc":{"Socket_time_out":1}},safe=True)
                        return soup('','lxml'),''
        
                     
                     
                     
        except:
            print 'Check url again ',traceback.print_exc()
            db.crawler_http_status_errors.update({"_id":ObjectId("5180bfa440ade62017d1120c")},{"$inc":{"Ungrouped":1}},safe=True)
            db.crawler_error_log.insert({'error_type':str(sys.exc_info()),'from_module':str(__file__)})
          
            
            return soup('','lxml'),''

        else:
             db.crawler_http_status_errors.update({"_id":ObjectId("5180bfa440ade62017d1120c")},{"$inc":{"ok_200":1}},safe=True)
             print 'ok'
        
        #  print 'Error from fetchpg'
        
    
#we will write seperate models that will fetch urls fetch and insert into models
if __name__=='__main__':
    print get_page('http://gh.3wjobs.com/j__s__Banking and Finance.html')   
else:
    pass   
            
