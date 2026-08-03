a = 10
b = 5

"""
This is the example of Lambda usage which is a one-line command that work like a function
We use it if we don't want to define a function
Lambda is needed in Tkinter because we cannot pass a value
for the function used in the command parameter of the widget created
It can take zero or more than one arguments (left side) but there can be only one expression (right side)
"""
c = lambda x : print(x + x)
d = lambda x : x - x
e = lambda x,y : x * y
c(a)

#print(c(a))
print(d(a))
print(e(a,b))
