def swapPositions(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list

def swapPos2(List,pos1,pos2):
    first = List.pop(pos1)
    second = List.pop(pos2-1)

    List.insert(pos1,second)
    List.insert(pos2,first)

    return List



input=[1,2,3,4,5]
pos1,pos2 = 1,3
print(swapPositions(input,pos1-1,pos2-1))
print(swapPos2(input,pos1-1,pos2-1))