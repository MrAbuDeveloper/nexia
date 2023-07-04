
##set

# set_1 = set()
# set_1 = {1, 2, 3, 4, 5, 6, 1, 2, 4, 5, 6}
# set_2 = {}
# print(set_1)
# print(type(set_2))

### list.append()
### set.add()
### copy()
### clear()
# set_1 = {1, 2, 3}
# set_2 = {4, 2, 3, 5}
# print(set_1.difference(set_2))
###pop()

# set_1 = {1, 2, 3, 4, 5, 6, 7}
# list_1 = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 1, 2, 1, 2, 3, 7]
# result = []
# for item in list_1:
#     if item not in result:
#         result.append(item)
# print(result)
# print(set_1.__sizeof__())
# print(list_1.__sizeof__() + result.__sizeof__())

###dict

# dict_1 = {}
# dict_2 = dict()
### dict = {"kalit": "qiymat"}
#
# komp_1 = 'Shoxruz'
# komp_3 = 'Ismoil'
# students = {"komp_1": "Shohruz", "komp_2": "Avazbek", "komp_3": "Ismoil", "komp_4": "Akmal"}
#
# print(students["komp_1"])
# print(students["komp_2"])
# print(students["komp_3"])

# managers = {
#     "0000888": "Ikrom",
#     "1234453": "Janna",
#     "7888213": "Malika"
# }

# print(managers["0000888"])
# managers["0000888"] = "Abdurayim"
# print(managers)

# managers["7777777"] = "Kolya"
# print(managers)

# users = {
#     1: {
#         "name": "Bobur",
#         "lastname": "Murtazoyev",
#         "age": 23
#     },
#     2: {
#         "name": "Ismoil",
#         "lastname": "Murodov",
#         "age": 18
#     }
# }
# print(users[2]['lastname'])

### dict method

# dct = {'key1': 'value1', 'key2': 'value2'}
# dct_2 = {'key3': 'value3', "key4": 'value4'}
# dct.clear()
# print(dct)
# copy = dct.copy()
# print(copy)
# print(dct.get('key1'))
# print(dct['key1'])

# dct.pop('key1')
# print(dct)
# dct.update(dct_2)
# print(dct)

# print(dct.values())

# for item in dct:
#     print(item)
# for key in dct.keys():
#     print(key)
# for value in dct.values():
#     print(value)

# for item in dct.items():
#     print(item)
# for key, value in dct.items():
#     print(key, value)

# items = ('key', 'value')
# keys, values = items
# print(keys, values)
# print(keys)

# a = 13
# b = 23
# a, b = 13, 23
# print(a)
# print(b)
# _, a = 13, 12
# print(a)
# print(_)

# user1 = {
#     'id': 1,
#     'name': "Vasya",
#     "lastname": 'Ivanov'
# }
#
# user2 = {
#     'id': 2,
#     'name': "Sasha",
#     "lastname": 'Kim'
# }
# user3 = {
#     'id': 3,
#     'name': "Jovlon",
#     "lastname": 'Raimov'
# }
# users = [user1, user2, user3]
#
# for user in users:
#     print(f"Userni id = {user['id']} ismi: {user['name']} familiyasi: {user['lastname']}")
