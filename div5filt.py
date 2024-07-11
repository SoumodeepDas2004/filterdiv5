def divfive(n):
    """Divides a number by 5 and returns the result"""
    if (n%5==0):
        return n

l=[20,113,41,53,70,299,10,15,50,80,75]
result=list(filter(divfive,l))
print(result)