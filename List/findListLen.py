#Method 1 using native method
#Initialize the list
test_list = [1, 4, 5, 7, 8]

#Print the test list
print("the list is :" + str(test_list))

#Find the lenght of list
counter=0
for i in test_list:
    #increment the counter
    counter = counter + 1

print("the length of list is :" + str(counter))

#Method using len method
print("the length of list using len method is :", len(test_list))

