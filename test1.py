numbers=[int(number) for number in input("enter numbers: ").split()]
sum=print("sum is :",sum(numbers))
maximum=print("max is :",max(numbers))
minimum=print("min is :",min(numbers))
numbers.sort()
print("sorted:",numbers)
numbers.reverse()
print("reverse:",numbers)
