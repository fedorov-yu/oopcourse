class InputDigits:
    def __init__(self, input_digits):
        self.input_digits = input_digits

    def __call__(self, *args, **kwargs):
        return list(int(i) for i in self.input_digits().split())

# @InputDigits
# def input_dg(dig):
#     return dig
input_dg = InputDigits(input)
res = input_dg()
print(res)