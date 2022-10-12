class HandlerGET:
    def __init__(self, func):
        self.fn = func

    def __call__(self, request, *args, **kwargs):
        req = request.get("method", 'GET')
        if not req or req != "GET":
            return None
        return self.get(self.fn, request)

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"


@HandlerGET
def contact(request):
    return "cdsmcms"


res = contact({"method": "GET", "url": "contact.html"})
print(res)
