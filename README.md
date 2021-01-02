# 100daysofpythoncode
Document all the useful links and tips in my python learning journey
https://docs.python-guide.org/writing/tests/ -> for pytest

Generalized List Comprehension Structure - https://dbader.org/blog/list-dict-set-comprehensions-in-python
- (values) = [(expression) for (value) in (collection)]
values = []
for value in collection:
    values.append(expression)
- values = [expression for value in collection if condition]
values = []
for value in collection:
    if condition:
        values.append(expression)
        
 **While Loops:** 
 - Single like while loop: while n > 0: n -= 1; print(n)
 while <condition>: statement1 ; statement2
 
 **Boiler Plate template for Decorators**

_More details on decorators can be found in Day22 folder_  

    import functools
    def decorator(func): 
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator        

