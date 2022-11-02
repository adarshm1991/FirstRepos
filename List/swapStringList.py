# Initializing list
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

#printing the original list
print("original list before swapping",str(test_list))

res = [sub.replace('G','-').replace('e','G').replace('-','e') for sub in test_list]

#printing list
print("List after performing swap of characters: "+str(res))
