import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{1,4}$'
count = 0
lista = []

# Otwarcie pliku i jego walidacja
with open('emails/emails3.txt', 'r') as f:
    for row in f:
        if not "@" in row:
            count += 1
            lista.append(row)
        elif row[0] == '@':
            count += 1
            lista.append(row)
        elif '.@' in row:
            count += 1
            lista.append(row)
        elif '@.' in row:
            count += 1
            lista.append(row)
        elif not (re.search(regex, row)):
            count += 1
            lista.append(row)
print(f"Invalid emails ({count}):")

#  Zapisywanie odpowiedzi do pliku
with open('task_1_answer.txt', 'w') as f:
    f.write(f'Invalid emails ({count}):' + '\n')
    for x in lista:
        print(x, end='')
        f.write('\t' + x)