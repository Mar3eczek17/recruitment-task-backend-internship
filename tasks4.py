import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{1,4}$'
count = 0
lista = []

# Otwarcie pliku i jego walidacja
f = open('emails/email-pack-1.txt', 'r')  # Zmiana odczytywanego pliku w tym miejscu i poniżej
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
print('\n')

converted_list = []
for element in lista:
    converted_list.append(element.strip())
print(converted_list)
print('\n')

# Otwarcie tego samego pliku w celu pozyskania danych do usunięcia nieprawidłowych maili i duplikatów
file = open('emails/email-pack-1.txt', 'r')  # Zmienić na taki sam plik jaki jest w linii nr 8
file_lines = file.read()
full_lista = file_lines.split('\n')
print(full_lista)

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

# Odczytanie logów z pliku (maili) i zapisanie ich do listy
regexx = "[a-z0-9]+[\._]?[a-z0-9]+@[a-z\.]+"
f = open('email-sent.logs', 'r')
logs = re.findall(regexx, f.read())
print(list(set(logs)))
print(sorted(list(set(logs))))
print('\n')

# Jeśli maila z pliku txt nie ma w pliku logs, to go odejmujemy
# i drukujemy i zapisujemy do plku txt z odpowiedzią do zadania nr 4
answer_task_4 = sorted([item for item in list_out_of_duplications if item not in logs])
print(answer_task_4)
print('\n')

# Zapisanie odpowiedzi do pliku
amount_of_not_sent_emails = len(answer_task_4)
with open('task_4_answer.txt', 'w') as f:
    f.write(f'Emails not sent ({amount_of_not_sent_emails}):' + '\n')
    for x in answer_task_4:
        print(x)
        f.write('\t' + x + '\n')
