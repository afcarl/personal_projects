from multiprocessing import Process,Queue
import pickle

class SimpleQueue:
    def __init__(self):
        self.internal_list = []
    def put(self,data):
        self.internal_list.append(data)
    def get(self):
        if self.internal_list != []:
            data = self.internal_list[0]
            del self.internal_list[0]
            return data
        else:
            return None

#To Do - write method that creates parallell definition of function that changes all return statements to q.put(result)

def process_elements(listing,func,q,num_workers=4,reduce=False):
    results = []
    for elem in listing:
        p = Process(target=func,args=(elem,q,))
        p.start()
        results.append(q.get())
    return results

def serializable_type(obj):
    types = [str(),int(),float(),bool()]
    types = [type(typ) for typ in types]
    if any([typ == type(obj) for typ in types]):
        return True
    else:
        return False

def main(listing,func,num_workers=4):
    q = Queue()
    sq = SimpleQueue()
    if all([serializable_type(elem) for elem in listing]): 
        results = process_elements(listing,func,q,num_workers=num_workers)
    else:
        results = process_elements(listing,func,sq,num_workers=num_workers)
    pickle.dump(results,open("results.pickle","w"))
