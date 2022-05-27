import collections
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{1,4}$'
count = 0
lista = []
f = open('emails/emails3.txt', 'r')  # zmienić odczytywany plik tu i poniżej
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
    print(x, end='')
converted_list = []
for element in lista:
    converted_list.append(element.strip())
print(converted_list)

# print(lista)
print("------------")

# full_lista = []
# with open('emails/emails3.txt', 'r') as f:  # zmienić odczytywany plik
#     for line in f:
#         print(line, end='')
# # for x in full_lista:
# #     print(x)
# print("\n+++++++++++++++")

file = open('emails/emails3.txt', 'r')
file_lines = file.read()
full_lista = file_lines.split('\n')
print(full_lista)

#  usunięcie niepoprawnych maili
lista_with_out_inccorects = [e for e in full_lista if e not in converted_list]
print(lista_with_out_inccorects)

#  usunięcie duplikatów z listy
list_out_of_duplications = []
for i in lista_with_out_inccorects:  # usunięcie duplikatów
    if i not in list_out_of_duplications:
        list_out_of_duplications.append(i)
print(list_out_of_duplications)

# zapisanie listy do pliku
with open('dane.txt', 'w') as f:
    for item in list_out_of_duplications:
        f.write("%s\n" % item)

print("================")
#  grupuj maile przez domenę
domain = []
for i in list_out_of_duplications:
    index = i.index("@")
    s_id = i[index + 1:]
    domain.append(s_id)
    # print(s_id)
    # print(f"Domain {s_id}:")
print(sorted(domain))

res = {}
for i in domain:
    res[i] = domain.count(i)
print(res)

od = collections.OrderedDict(sorted(res.items()))
print(od)

with open('task_3_answer.txt', 'w') as f:
    for k, v in od.items():
        # print(k, v)
        print(f"Domain {k} ({v}):")
        f.write(f"Domain {k} ({v}):" + '\n')
        for i in list_out_of_duplications:
            if (re.search(k, i)):
                print(i)
                f.write('\t' + i + '\n')


