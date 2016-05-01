import requests

# res = requests.get('https://docs.python.org/3.5/')  # возвращает класс Response
# print(res.status_code)
# print(res.headers['Content-Type'])
# print(res.content)  # binary по умолч
# print(res.text)  # если уверенны, что это текст

print('-----------------------')

# res1 = requests.get('https://docs.python.org/3.5/_static/py.png')

# print(res1.status_code)
# print(res1.headers['Content-Type'])
# print(res1.content)  # binary по умолч

# записали бинарник в файл и получили изображение
# with open('python.png', 'wb') as f:
#     f.write(res1.content)

print('-----------------------')

# запрос в поисковик(или другой ресурс)
# лучше не составлять такие запросы самим
res3 = requests.get('https://yandex.ru/search/',
                    params={'text': 'Stepic',
                            'test': 'test1',
                            'name': 'Name With Spaces',
                            'list': ['test1', 'test2']
                            })

print(res3.status_code)
print(res3.headers['Content-Type'])
print(res3.url)
# print(res3.text)
