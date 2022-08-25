from itertools import zip_longest
import json


with open('users.csv', 'r', encoding='utf-8') as file:
    users = []
    for i in file:
        users.append(''.join(i.split()))


with open('hobby.csv', 'r', encoding='utf-8') as file:
    hobbies = []
    for i in file:
        hobbies.append(' '.join(i.split()))

if len(users) < len(hobbies):
    print('1')
    exit()

users_hobbies = {user: hobby for user,hobby in zip_longest(users, hobbies)}


with open('users_hobbies.csv', 'w', encoding="utf-8") as file:
    json.dump(users_hobbies, file)

with open('users_hobbies.csv', 'r', encoding='utf-8') as file:
    output = json.load(file)

print(output)
