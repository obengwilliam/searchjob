def compute_ranks(graph):
    """
    The dumping factore depicts that there is an 80% chance that
    a user will continue on links at each page.
    """
    d = 0.8 # damping factor
    '''
    This iteration helps reduce the initialized pageranks into the actual page ranks
    '''
    numloops = 25
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node] / len(graph[node]))
            
            newranks[page] = newrank
        ranks = newranks
    return ranks




if __name__=='__main__':
   print compute_ranks({'http://www.google.com':['http:www.google.com/k','http:www.google.com/e']})
