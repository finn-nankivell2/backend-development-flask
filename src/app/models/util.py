def resourcemethod(*fields: list[str]):
    """
    Method decorator for Models, listing the properties that should be returned as a json resource.
    Should be used to decorate a function, and the Model's properties that the function should return should be passed to the decorator.
    The decorated function receives the resulting data, and can modify it before it is returned.
    """
    if len(fields) == 1 and callable(fields[0]):
        raise TypeError("fields must be a list of strings, not a callable. Did you forget brackets on the decorator?")

    def outer(func):
        def inner(self, *args, **kwargs):
            data = {}
            for field in fields:
                data[field] = getattr(self, field)

            val = func(self, data, *args, **kwargs)
            if val is not None and isinstance(val, dict):
                data = val
            return data

        return inner

    return outer
