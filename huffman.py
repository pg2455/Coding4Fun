## taken from gensim's word2vec implementation

import numpy as np
import heapq
from six import itervalues
import pdb

class counter(object):
    def __init__(self,**kwargs):
        self.count = 0
        self.__dict__.update(**kwargs)


# array of random integers
A = numpy.random.randint(5, size =10)
A = [i for i in A]

#or with words
A= ['and','by','all','all','all','by','kill','him']

# count occurences
counts = dict()
for i in A:
    if i not in counts:
        counts[i] = counter(count = A.count(i))

# make a heap; priorirty queue on key = value and priority as minimum value
heap = list(itervalues(counts))
heapq.heapify(heap)

# build huffman tree
for i in xrange(len(counts)-1):
    min1, min2 = heapq.heappop(heap),heapq.heappop(heap) # pop elements with least freq
    heapq.heappush(heap, counter(count= min1.count + min2.count,\
    index = i+len(counts), left = min1, right =min2)) # push new element with freq combined min1 +min2 at index


# recurse through down the tree assigning codes
if heap:
    max_depth, stack = 0, [(heap[0],[],[])]
    while stack:
        pdb.set_trace()
        node, codes, points = stack.pop()
        if node.index < len(counts):
            #reached the leaf nodes in binary huffman tree : where longest codes need to be assigned
            node.code, node.points = codes, points
            max_depth = max(len(codes), max_depth)
        else:
            # still some inner node in the tree
            points = np.array(list(codes) + [node.index - len(counts)], dtype = np.uint32)
            stack.append((node.left, np.array(list(codes) + [0], dtype=np.uint8), points))
            stack.append((node.right, np.array(list(codes) + [1], dtype=np.uint8), points))
