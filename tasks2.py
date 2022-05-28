import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{1,4}$'
count = 0
lista = []
with open('emails/emails3.txt', 'r') as f:  # zmienić odczytywany plik tu i poniżej
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

print("------------")

full_lista = []
with open('emails/emails3.txt', 'r') as f:  # zmienić odczytywany plik
    for line in f:
        full_lista.append(line)
    # print(full_lista)
for x in full_lista:
    print(x)

print("+++++++++++++++")

lista_with_out_inccorects = [e for e in full_lista if not e in lista]
print(lista_with_out_inccorects)
newlist = []
for i in lista_with_out_inccorects:
    if i not in newlist:
        newlist.append(i)
print(newlist)

print("Write your string argument below:")
user_input = input()

filter_object = filter(lambda a: user_input in a, newlist)
b = (len(list(filter_object)))
print(f"Found emails with '{user_input}' in email ({b}):")
filter_object = filter(lambda a: user_input in a, newlist)
# print(list(filter_object))

# Zapisywanie do pliku
with open('task_2_answer.txt', 'w') as f:
    f.write(f'Found emails with "{user_input}" in email ({b}):' + '\n')
    for x in filter_object:
        print(x, end='')
        f.write('\t' + x)