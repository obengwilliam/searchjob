from django_cron import cronScheduler, Job

from crawler.start_crawler import start


print 'hello this is django cron'

class startcrawler(Job):
      run_every = 1


      def job(self):
          print 'crawler__processing.... '
          print 'will sync crawle one of these days'






cronScheduler.register(startcrawler)
