Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class PetFriends:
...     '''Библиотека содержит API запросы к приложению PetFriens'''
...     def __init__(self):
...         # self.base_url = 'https://petfriends.skillfactory.ru/'
...         self.base_url = 'https://petfriends.skillfactory.ru//'
... 
...     def get_app_key(self, email: str, password: str) -> json:
...         '''Метод делает get запрос к API  сервера с емейлом и паролем
...          в header запроса и возвращает код статуса запроса и секретный
...           ключ для в формате json либо виде строки'''
...         headers = {
...             'email': email,
...             'password': password
...         }
...         res = requests.get(self.base_url + 'api/key', headers=headers)
... 
...         status = res.status_code
...         result = ''
...         try:
...             result = res.json()
...         except:
...             result = res.text
