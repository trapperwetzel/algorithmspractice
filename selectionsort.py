# selection sort
# tw 
def findSmallest(arr):

    smallest = arr[0]
    smallest_index = 0

    for i in range (1,len(arr)):

        if (arr[i] < smallest):

            smallest = arr[i]
            smallest_index = i 
    
    return smallest_index



def selectionSort(arr):

    newArr = []

    for i in range(len(arr)):

        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    
    return newArr




arr1 = [1,2,3,4,5,10,11,15,20,6,7,8,9,12,13,14,16,19,17,18,19,19,21,23,22] 


result = selectionSort(arr1) 

for i in result:
    print(i)

