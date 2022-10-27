class Validator:
    def is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def is_valid(self, data):
        return type(data) == float and self.min_value <= data <= self.max_value

    def __call__(self, *args, **kwargs):
        return self.is_valid(args[0])

class IntegerValidator(Validator):
    pass


class FloatValidator(Validator):
    pass
