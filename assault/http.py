def fetch(url):
    """ Make the request and return the results """
    pass

def worker(name, queue, results):
    """ A function to take unmake requests from a queue and perform the work then add results to the results list. """
    pass

def distrubute_work(url, requests, concurrency, results):
    """ Divide up the work into batches and collect the final results """
    pass

def assault(url, requests, concurrency):
    """ Entrypoint to making requests """
    pass