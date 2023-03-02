# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
info = {
    "id": 2223,
    "category": {"id": 2, "name": "Cat"},
    "name": "Polina",
    "photoUrls": ["string"],
    "tags": [{"id": 0,"name": "string"}],
    "status": "available"
}
res_post_addNewPet = requests.post(f"https://petstore.swagger.io/v2/pet",
                                   headers={'accept':'application/json', 'Content-Type': 'application/json'},
                                   data=json.dumps(info, ensure_ascii=False))
print(f"Статус ответа от сервера на POST запрос добавление питомца: {res_post_addNewPet.status_code}")