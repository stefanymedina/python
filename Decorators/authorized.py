from functools import wraps

def ensure_authorized(fn):
    @wraps(fn)
    def inner(*args, **kwarg):
        if kwarg.get("role") == 'admin':
            return fn(*args, **kwarg)
        return "Unauthorized"
    return inner

@ensure_authorized
def show_secrets(*arg, **kwarg):
    return "Shh! Don't tell anybody!"

print(show_secrets(a="admin"))