def distmap(func, i):
    for _ in i:
        yield func(_)


def dist(install, *outer_args, **outer_kwargs):
    """
    decorator for distributed function

    :param install: function to perform configuration of the instance/docker image
    :return: decorated function
    """

    def wrapper(func):
        def wrapper2(*args, **kwargs):
            print(install, outer_args)
            print(outer_kwargs)
            return func(*args, **kwargs)

        return wrapper2

    return wrapper
