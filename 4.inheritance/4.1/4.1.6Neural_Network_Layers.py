class Layer:
    """Основной класс нейронной сети
    Класс образует связи между слоями"""

    def __init__(self):
        self.next_layer = None
        self.name = 'Layer'

    def __call__(self, layer, *args, **kwargs):
        self.next_layer = layer
        return self.next_layer


class Input(Layer):
    """Класс для формирования входного слоя нейронной сети"""

    def __init__(self, inputs: int):
        super().__init__()
        self.inputs = inputs
        self.name = 'Input'


class Dense(Layer):
    """Класс для формирования полносвязного слоя нейронной сети"""

    def __init__(self, inputs: int, outputs: int, activation: str):
        super().__init__()
        self.name = 'Dense'
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    """Класс для итерирования (перебора) слоев нейронной сети"""

    def __init__(self, network: Layer):
        self.network = network

    def __iter__(self):
        tmp = self.network
        while tmp:
            yield tmp
            tmp = tmp.next_layer


network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))
for x in NetworkIterator(network):
    print(x.name)
