import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

def make_html(tag):
    def decorator_make_html(func):
        @functools.wraps(func)
        def wrapper_make_html(*args, **kwargs):
            # Do something before using arg_1, ...
            value = func(*args, **kwargs)
            # Do something after using arg_1, ...
            return f'<{tag}>{value}</{tag}>'
        return wrapper_make_html
    return decorator_make_html

@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text

#print(get_text())