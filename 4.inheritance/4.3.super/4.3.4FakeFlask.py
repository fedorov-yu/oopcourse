class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


# здесь объявляйте декоратор Callback
class Callback:
    def __init__(self, path: str, router_cls: Router):
        self.path = path
        self.router_cls = router_cls

    def __call__(self, func, *args, **kwargs):
        if not self.router_cls.get(self.path):
            return self.router_cls.add_callback(self.path, func)


@Callback('/about', Router)
def about():
    return '<h1>About</h1>'


route = Router.get('/about')
ret = route()
assert ret == '<h1>About</h1>', "декорированная функция вернула неверные данные"

route = Router.get('/')
assert route is None, "Класс Router, при вызове метода get, вернул неверные данные"