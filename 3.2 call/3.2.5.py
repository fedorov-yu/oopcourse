class RenderList:
    def __init__(self, type_list, ):
        if type_list not in ('ul', 'ol'):
            type_list = 'ul'
        self.__type_list = type_list

    def __call__(self, *args, **kwargs):
        return f"<{self.__type_list}>" + "\n" + '\n'.join(
            f'<li>{i}</li>' for i in args[0]) + "\n" + f"</{self.__type_list}>"


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
lst = ['item1', 'item2', 'item3']
render = RenderList("opl")
html = render(lst)
print(html.replace(' ','').replace('\n','').strip())
