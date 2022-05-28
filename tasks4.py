import collections
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{1,4}$'
count = 0
lista = []
f = open('emails/email-pack-1.txt', 'r')  # zmienić odczytywany plik tu i poniżej
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

file = open('emails/email-pack-1.txt', 'r')
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
# with open('dane_4.txt', 'w') as f:
#     for item in list_out_of_duplications:
#         f.write("%s\n" % item)
print("================")

# Odczytanie logów z pliku (maili) i zapisanie ich do listy
regexx = "[a-z0-9]+[\._]?[a-z0-9]+@[a-z\.]+"

f = open('email-sent.logs', 'r')
logs = re.findall(regexx, f.read())
print(list(set(logs)))
print(sorted(list(set(logs))))


# Jeśli maila z pliku txt nie ma w pliku logs, to go odejmujemy
# i drukujemy i zapisujemy do plku txt z odpowiedzią do zadania nr 4
answer_task_4 = [item for item in list_out_of_duplications if item not in logs]
print(answer_task_4)
amount_of_not_sent_emails = len(answer_task_4)

# Zapisanie odpowiedzi do pliku
with open('task_4_answer.txt', 'w') as f:
    f.write(f'Emails not sent ({amount_of_not_sent_emails}):' + '\n')
    for x in answer_task_4:
        print(x, end='')
        f.write('\t' + x + '\n')