def calc(*args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = 0
    for item in items:
        if type(item) in (int, float):
            result += item
    return result