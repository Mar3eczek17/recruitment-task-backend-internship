import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{1,4}$'
count = 0
lista = []
with open('emails/emails3.txt', 'r') as f:
    for row in f:
        if not "@" in row:
            count += 1
            lista.append(row)
            # print(row)
        elif row[0] == '@':
            count += 1
            lista.append(row)
            # print(row)
        elif '.@' in row:
            count += 1
            lista.append(row)
            # print(row)
        elif '@.' in row:
            count += 1
            lista.append(row)
            # print(row)
        elif not (re.search(regex, row)):
            count += 1
            lista.append(row)
            # print(row)
print(f"Invalid emails ({count}):")

for x in lista:
    print(x)

