# factorial 


def fact(x): 


    if x == 1:
        return x 

    else:
        return x * fact(x -1 ) 



result1 = fact(3)
result2 = fact(5)
result3 = fact(6) 


print(result1)
print()
print(result2)
print()
print(result3) 