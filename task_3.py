import collections
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{1,4}$'
count = 0
lista = []

# Opening the file and validating it
f = open('emails/emails3.txt', 'r')  # Change the file being read at this point and below
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
file = open('emails/emails3.txt', 'r')  # Change to the same file as on line 9
file_lines = file.read()
full_lista = file_lines.split('\n')
print(full_lista)
print('\n')

#  Removal of incorrect e-mails
lista_with_out_inccorects = [e for e in full_lista if e not in converted_list]
print(lista_with_out_inccorects)

#  Removal of duplicates from the list
list_out_of_duplications = []
for i in lista_with_out_inccorects:  # Removal of duplicates
    if i not in list_out_of_duplications:
        list_out_of_duplications.append(i)
print(list_out_of_duplications)
print('\n')

# Save the list to a file
with open('data_3.txt', 'w') as f:
    for item in list_out_of_duplications:
        f.write("%s\n" % item)

# Grouping of emails into domains
domain = []
for i in list_out_of_duplications:
    index = i.index("@")
    s_id = i[index + 1:]
    domain.append(s_id)
print(sorted(domain))
print('\n')

# Counting the occurrences of a given domain
res = {}
for i in domain:
    res[i] = domain.count(i)
print(res)
print('\n')

# Alphabetical arrangement of domains
od = collections.OrderedDict(sorted(res.items()))
print(od)
print('\n')

# Saving the domain name, its instances and full e-mail addresses to the file
with open('task_3_answer.txt', 'w') as f:
    for k, v in od.items():
        print(f"Domain {k} ({v}):")
        f.write(f"Domain {k} ({v}):" + '\n')
        for i in list_out_of_duplications:
            if (re.search(k, i)):
                print(i)
                f.write('\t' + i + '\n')


