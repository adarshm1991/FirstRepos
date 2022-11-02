#Method 1
def maxNum(a,b):
    if(a>b):
        return a
    else:
        return b

#Method 2
def maxNum2(a,b):
    return max(a,b)

#method 3 
def maxNum3(a,b):
    return((b,a)[a>b])

#method 4
def maxNum4(a,b):
    return(a if a > b else b)
a=2
b=4
#method 5
def maxNum5(a,b):
    return ((lambda: a,lambda: b)[a<b]())

print("Max number is:",maxNum(a,b)) 
print("Max Number using inbuilt function in python",maxNum2(a,b))
print("Max number using ternary condition operator",maxNum3(a,b))
print("Max Number using ternary condition2 ",maxNum4(a,b))
print("Max Number using Lambda function",maxNum5(a,b))