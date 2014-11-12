from pythonds.basic.queue import Queue


## hot potato simulation
## one who ends up holding potato after num passes is going to leave the queue
## guess who will be the winner?
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
    
