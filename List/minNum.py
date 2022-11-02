#Method 1
def minNum(a,b):
    if(a<b):
        return a
    else:
        return b

#Method 2
def minNum2(a,b):
    return min(a,b)

#method 3 
def minNum3(a,b):
    return((b,a)[a<b])

#method 4
def minNum4(a,b):
    return(a if a < b else b)
a=2
b=4
#method 5
def minNum5(a,b):
    return ((lambda: b,lambda: a)[a<b]())

print("min number is:",minNum(a,b)) 
print("min Number using inbuilt function in python",minNum2(a,b))
print("min number using ternary condition operator",minNum3(a,b))
print("min Number using ternary condition2 ",minNum4(a,b))
print("min Number using Lambda function",minNum5(a,b))