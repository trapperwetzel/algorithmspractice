# Binary Search of an array with 128 items

arr1 = []

for i in range(0,129):
    arr1.append(i)



def binarysearch(anarray):

    low = 0 
    high = len(arr1) - 1
    count = 0 
    # how many times does it take for you to search through the entire array? 


    while(low <= high):
        count += 1

        mid = (low + high) // 2
        low = mid + 1

    print(count)






binarysearch(arr1) 
print()
print() 

 