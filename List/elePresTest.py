list = test_list = [1, 6, 3, 5, 3, 4]
input = 3
isPresent = 0 

#Method 1 - using for loop
for i in test_list:
    if(i == input):
        isPresent = 1
        break
    
if(isPresent):
    print("Element is present in the list",input)
else:
    print("Element is not present in the list",input)

#Method 2: using naive method
#

if input in test_list:
    print("Using Naive method- Element is present in list",input)
else:
    print("Using Naive method - Element is not present in list",input) 


#Method 3 : using any method to check if list is not empty
empList = []
result = any(input in empList for input in empList)

print("using any method to check for list empty or not "+str(bool(result)))

#method4: using count method

res = test_list.count(input)
if(res > 0):
    print("how many times input is present in test_list")
else:
    print("input is not present in test_list")

