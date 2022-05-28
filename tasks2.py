import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{1,4}$'
count = 0
lista = []

# Opening the file and validating it
with open('emails/emails3.txt', 'r') as f:  # Change the file being read at this point and below
    for row in f:
        if not "@" in row:
            count += 1
            lista.append(row)
        elif row[0] == '@':
            count += 1
            lista.append(row)
        elif '.@' and '@.' in row:
            count += 1
            lista.append(row)
        elif not (re.search(regex, row)):
            count += 1
            lista.append(row)
print(f"Invalid emails ({count}):")

for x in lista:
    print(x, end='')
print('\n')

# Open the same file to retrieve data to delete invalid mails and duplicates
full_lista = []
with open('emails/emails3.txt', 'r') as f:  # Zmienić na taki sam plik jaki jest w linii nr 8
    for line in f:
        full_lista.append(line)
for x in full_lista:
    print(x, end='')
print('\n')

# Removing duplicates and incorrect e-mails from the list
lista_with_out_inccorects = [e for e in full_lista if e not in lista]
print(lista_with_out_inccorects)

# Remove duplicates from the list
list_out_of_dupications = []
for i in lista_with_out_inccorects:
    if i not in list_out_of_dupications:
        list_out_of_dupications.append(i)
print(list_out_of_dupications)
print('\n')

# Enter the name of the searched domain
print("Write your string argument below:")
user_input = input()
print('\n')

# Searching the list for emails with the correct domain
filter_object = filter(lambda a: user_input in a, list_out_of_dupications)
the_number_of_e_mails_found = (len(list(filter_object)))
print(f"Found emails with '{user_input}' in email ({the_number_of_e_mails_found}):")
filter_object = filter(lambda a: user_input in a, list_out_of_dupications)

# Save to file
with open('task_2_answer.txt', 'w') as f:
    f.write(f'Found emails with "{user_input}" in email ({the_number_of_e_mails_found}):' + '\n')
    for x in filter_object:
        print(x, end='')
        f.write('\t' + x)
