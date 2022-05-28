import collections
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{1,4}$'
count = 0
lista = []

# Otwarcie pliku i jego walidacja
f = open('emails/emails3.txt', 'r')  # Zmiana odczytywanego pliku w tym miejscu i poniżej
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

for x in lista:
    print(x, end='')
print('\n')

converted_list = []
for element in lista:
    converted_list.append(element.strip())
print(converted_list)
print('\n')

# Otwarcie tego samego pliku w celu pozyskania danych do usunięcia nieprawidłowych maili i duplikatów
file = open('emails/emails3.txt', 'r')  # Zmienić na taki sam plik jaki jest w linii nr 9
file_lines = file.read()
full_lista = file_lines.split('\n')
print(full_lista)
print('\n')

#  Usunięcie niepoprawnych maili
lista_with_out_inccorects = [e for e in full_lista if e not in converted_list]
print(lista_with_out_inccorects)

#  Usunięcie duplikatów z listy
list_out_of_duplications = []
for i in lista_with_out_inccorects:  # usunięcie duplikatów
    if i not in list_out_of_duplications:
        list_out_of_duplications.append(i)
print(list_out_of_duplications)
print('\n')

# zapisanie listy do pliku
with open('dane_3.txt', 'w') as f:
    for item in list_out_of_duplications:
        f.write("%s\n" % item)

#  Grupowanie maili na domeny
domain = []
for i in list_out_of_duplications:
    index = i.index("@")
    s_id = i[index + 1:]
    domain.append(s_id)
print(sorted(domain))
print('\n')

# Policzenie wystąpień danej domeny
res = {}
for i in domain:
    res[i] = domain.count(i)
print(res)
print('\n')

# Ułożenie alfabetyczne domen
od = collections.OrderedDict(sorted(res.items()))
print(od)
print('\n')

# Zapisywanie do pliku nazwy domeny, jej wystąpień i pełnych adresów e-mail
with open('task_3_answer.txt', 'w') as f:
    for k, v in od.items():
        print(f"Domain {k} ({v}):")
        f.write(f"Domain {k} ({v}):" + '\n')
        for i in list_out_of_duplications:
            if (re.search(k, i)):
                print(i)
                f.write('\t' + i + '\n')


