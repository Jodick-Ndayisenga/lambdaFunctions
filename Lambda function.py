def x(a): return a + 10


print(x(5))
# the result will here be 15 since at every input we add 10.
# we can also use it inside a function as well


def raja(y):
    return lambda a: a * y


x = raja(3)
# here we assign def raja to a variable x which means that 3 is an argument for the function
print(x(15))
# if we this function, we expect to see two outputs. One 15 and another 45
