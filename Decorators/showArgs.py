from functools import wraps

def show_args(fn):
    @wraps(fn)
    def call_do_nothing(*args, **kwargs):
        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return fn(*args, **kwargs)
    return call_do_nothing

@show_args
def do_nothing(*args, **kwargs):
    pass

print(do_nothing(1, 2, 3,a="hi",b="bye"))    