from typing import List


class Model:
    data = ''

    def query(self, **kwargs):
        self.data = ', '.join(f'{item[0]} = {item[1]}' for item in kwargs.items())

    def __str__(self):
        if not self.data:
            return "Model"
        return 'Model: ' + self.data


model = Model()
model.query(field_1='value_1', field_2='value_2')
model2 = Model()
print(model, model2)
