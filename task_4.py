import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{1,4}$'
count = 0
lista = []

# Opening the file and validating it
f = open('emails/email-pack-1.txt', 'r')  # Change the file being read at this point and below
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

converted_list = []
for element in lista:
    converted_list.append(element.strip())
print(converted_list)
print('\n')

# Opening the same file to retrieve data to delete invalid e-mails and duplicates
file = open('emails/email-pack-1.txt', 'r')  # Change to the same file as on line 8
file_lines = file.read()
full_lista = file_lines.split('\n')
print(full_lista)

# Removal of incorrect e-mails
lista_with_out_inccorects = [e for e in full_lista if e not in converted_list]
print(lista_with_out_inccorects)

# Removal of duplicates from the list
list_out_of_duplications = []
for i in lista_with_out_inccorects:  # Removal of duplicates
    if i not in list_out_of_duplications:
        list_out_of_duplications.append(i)
print(list_out_of_duplications)
print('\n')

# Reading logs from the file (e-mails) and saving them to the list
regexx = "[a-z0-9]+[\._]?[a-z0-9]+@[a-z\.]+"
f = open('email-sent.logs', 'r')
logs = re.findall(regexx, f.read())
print(list(set(logs)))
print(sorted(list(set(logs))))
print('\n')

# If the email from the txt file is not in the logs file, we subtract it, print it and
# save it to the txt file with the answer to the problem no.4
answer_task_4 = sorted([item for item in list_out_of_duplications if item not in logs])
print(answer_task_4)
print('\n')

# Save the response to a file
amount_of_not_sent_emails = len(answer_task_4)
with open('task_4_answer.txt', 'w') as f:
    f.write(f'Emails not sent ({amount_of_not_sent_emails}):' + '\n')
    for x in answer_task_4:
        print(x)
        f.write('\t' + x + '\n')
