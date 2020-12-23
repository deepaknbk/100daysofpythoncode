# 100daysofpythoncode
Document all the useful links and tips in my python learning journey
https://docs.python-guide.org/writing/tests/ -> for pytest

Generalized List Comprehension Structure 
- (values) = [(expression) for (value) in (collection)]
values = []
for value in collection:
    values.append(expression)
- values = [expression for value in collection if condition]
values = []
for value in collection:
    if condition:
        values.append(expression)
