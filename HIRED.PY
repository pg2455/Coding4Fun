
class Stack():
    def __init__(self):
        self.list =[]

    def push(self, data):
        self.list.append(data)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)

def check_braces(expressions):
    # Write your code here
    # To print results to the standard output you can use print
    # Example print "Hello wor
    d = {'(' :  0, '[' :  1, '{' : 2,')' : 0, ']' : 1, '}' :2}
    opp = {')' : '(', '}' : '{', ']':'['}
    out = [1]*len(expressions)
    for x,string in enumerate(expressions):
        stacks = [Stack(), Stack(), Stack(), Stack()]
        i=0
        while i < len(string):
            #print i, string, d
            if string[i] in ['(','[','{']:
                stacks[d[string[i]]].push(string[i])
                stacks[3].push(string[i])
            else:
                if stacks[d[string[i]]].size() == 0:
                    out[x] = 0
                    break
                popped =  stacks[3].pop()
                pdb.set_trace()
                if stacks[3].size() >0 and popped != opp[string[i]]:
                    out[x] = 0
                    break

                _ = stacks[d[string[i]]].pop()
            i+=1

    for i in out:
        print i

def checkAll(stacks):
    return all([stack.isEmpty() for stack in stacks])
