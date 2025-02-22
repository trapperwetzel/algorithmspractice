# Binary Search Function
def binarysearchfornumber(anarray, target):
    low = 0 
    high = len(anarray) - 1
    count = 0 
    
    while (low <= high):
        count += 1 
        mid = (high + low) // 2
        guess = anarray[mid]
        if (guess == target):
            return mid, count 
        if (guess > target):
            high = mid - 1 
        elif (guess < target):
            low = mid + 1
    return None 

arr1 = []
for i in range(0,129):
    arr1.append(i)

userinput = ""
while(userinput != "quit"):
    print()
    userinput = input("Press enter to start or type quit to exit\n") 
    usernum = int(input("Enter number to binary search for!\n"))
    result,count = binarysearchfornumber(arr1,usernum)
    print(f"Is your number {result}? If so, then the number was found properly due to binary search! It took {count} tries to get there!") 

 