from pythonds.basic import Stack

#converting number in decimal to other bases; stack version
# there is no problem of maximum depth of recursion
def toStr(n, base):
    convertString = '0123456789ABCDEF' # can cover base upto 16
    rStack = Stack()
    while n >0:
        if n<base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n= n // base
    res = ''
    while not rStack.isEmpty():
        res = res + rStack.pop()
    return res


# implicit stacks for recursion
def toStr(n,base):
    convertString = '0123456789ABCDEF' # can cover base upto 16
    #base case
    if n<base:
        return convertString[n]
    else:
        # changing state of the recursion function
        return toStr(n//base, base) + convertString[n%base]

# turtle tutorial
import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, linelin):
    if linelin >0 :
        myTurtle.forward(linelin)
        myTurtle.right(90)
        drawSpiral(myTurtle,linelin-4)


drawSpiral(myTurtle,100)
myWin.exitonclick()



## understanding recursion with the help of turtle

def tree(branchlen, t):
    if branchlen > 5:
        t.forward(branchlen)
        t.right(20)
        tree(branchlen - 5, t)
        t.left(40)
        tree(branchlen-5, t)
        t.right(20)
        t.backward(branchlen)

def main():
    t = turtle.Turtle()
    myWin =  turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    tree(40,t)
    myWin.exitonclick()

main()


####### Sirepinski triangle
import turtle

def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    # base case
    if degree > 0:
        #changing state in each recursion
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints,3,myTurtle)
   myWin.exitonclick()

main()






#################### DP minCoins ######################
#non recursive
def giveChange(coinValueList, change, minCoins):
    for i in range(change+1):
        if i==0:
            minCoins[i] = 0
        elif i in coinValueList:
            minCoins[i] = 1
        else:
            minCoins[i] = 1 + min([minCoins[i-j] for j in coinValueList if i-j>0])
    return minCoins[change]

def main():
    minCoins = defaultdict(int)

    print giveChange([1,2,5,10,21], 63,minCoins)
    print minCoins

def backtrace(coinValueList, change, minCoins):
    coins = []
    while change >0:
# check where minCoins[change -i ] == minCoins[change] -1 for i in coinValueList if change - i >0
# append that to coins and change  = change - i
        for i in coinValueList:
            if minCoins[change - i] == minCoins[change] -1:
                break
        coins.append(i)
        change =  change  - i
    return coins
