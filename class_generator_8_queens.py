__metaclass__ = type


def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        #Every element in state and its index represent the position in the table.
        #e.g. state(0)=1, means the queue's position is at cell(1,0). index is for Y axis, value is for X axis
        #the expression represents
        #if the nextX are equals to any existing queue's X(state(i)), then conflict occur
        #if the distance on Y axis(state(i) - nextX) equals to the distance on X axis(nextY - i), then conflict occurs
        if abs(state[i] - nextX) in (0, nextY-i):
            return True
    return False
            
            
def queen(num, state=()):
    for i in range(num):
        if not conflict(state, i): #valid position found
            if len(state) == num - 1:
                yield (i,)
            else:
                for result in queen(num, state + (i,)):
                    yield (i,) + result
         

def prettyPrint(state):
    length = len(state)
    for i in range(length):
        print '.' * (state[i]) +repr(state[i])+ '.'* (length - state[i]-1)

        
        
queen4 = queen(4)
state = queen4.next()
print state
prettyPrint(state)

prettyPrint(state)
#print list(queen(10))

queen10 = queen(10)
state1 = queen10.next()
print state1+
prettyPrint(state1)
                
            
