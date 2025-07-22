print(""""

Lambda functions, also called anonymous functions, are small, inline functions that can be created on the fly without a formal def statement. They are a powerful feature in Python that enables functional programming patterns.

Key points:

Anonymous: They don't have a name unless assigned to a variable

Single expression: Can only contain one expression (no statements or multiple lines)

First-class objects: Can be passed as arguments, returned from functions, etc.

Temporary: Typically used where you need a small function for a short period.

""")
def sq(x=0):
    x ** 2
    return
sq1 = lambda x: x ** 2
print(sq(5))
print(sq1(5))
num = [1,2,3,4]
squ = list(map(lambda x: x**2, num))
print(squ)
# When to use Lambda Functions.As arguments to higher-order functions (like map()), filter() sorted() fro simpler operations that dont need a named function When you need a throwaway function that wonbe reused in callback functions for event-driven programming.      
# Applies function to every item in iterable Returns an iterater (map object) that yields the results can accept mutiple iterables if the function takes multiple arguments lazy evaluation - dosent compute values until iterated over
a = [1,2,3]
b = [4,5,6]
r = map(lambda x,y: x+y,a,b)
print(list(r))
"""
the zip function aggregates elemanets from each of the itera
"""







names = ["alice", "Bob", "Charlie" ]
ages = [25,30,35]
zipped = zip(names,ages)
print(list(zipped))
z_d = [("Alice" , 25) ,("Bob", 30),("Charlie" ,35) ]
names,ages = zip(*z_d)
print(f"{names} \n  {ages}")
p = map(lambda pair: pair[0] * pair[1] , zip(a,b))
print(list(p))