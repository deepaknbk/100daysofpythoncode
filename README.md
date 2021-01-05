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
    
     def name(arg_1, ...):
        def decorator_name(func):
            @functools.wraps(func)
            def wrapper_name(*args, **kwargs):
                # Do something before using arg_1, ...
                value = func(*args, **kwargs)
                # Do something after using arg_1, ...
                return value
            return wrapper_name
        return decorator_name
        
###### Regular Expressions: 
https://docs.python.org/3.7/howto/regex.html#regex-howto
cool online tool to test the regex - https://regex101.com/#python
   

