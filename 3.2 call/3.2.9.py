class RenderDigit:

    # HARDCODING
    # def __call__(self, instance, *args, **kwargs):
    #     if instance is None: return None
    #     elif isinstance(instance, int): return instance
    #     if isinstance(instance, str):
    #         if instance.isdigit(): return int(instance)
    #         elif instance.isalnum(): return None
    #         elif len(instance.split('.')) > 1: return None
    #         else: return int(instance)

    def __call__(self, instance, *args, **kwargs):
        try:
            return int(instance)
        except ValueError:
            return None


class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            return [self.render(i) for i in func().split()]
        return wrapper


input_dg = InputValues(RenderDigit())(input)
res = input_dg()
print(res)
