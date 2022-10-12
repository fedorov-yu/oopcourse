class Handler:
    def __init__(self, methods=("GET")):
        self.__methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            req = request.get("method", "GET")
            if req in self.__methods:
                method = req.lower()
                return self.__getattribute__(method)(func, request)

        return wrapper

    def get(self, func, request):
        return f"GET: {func(request)}"

    def post(self, func, request):
        return f"POST: {func(request)}"


@Handler(methods=('GET', 'POST'))
def contact(request):
    return "cdsmcms"


res = contact({"method": "GET", "url": "contact.html"})
print(res)
