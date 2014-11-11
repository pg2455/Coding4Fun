from pythonds.basic.queue import Queue

def hot_pot(names, num):
    # create a Queue
    q  =  Queue()
    _ = [q.enqueue(i) for i in names]
    count = 0
    while q.size()!=1:
        while count !=num:
            q.enqueue(q.dequeue())
            count +=1
        q.dequeue()
    return q.dequeue()

def main():
    names = ['prateek','esteban', 'anil','vugar','gaurabh']
    print hot_pot(names,10)
    
