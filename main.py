from math import expm1
from pprint import pprint
import csv
import re

with open('phonebook_raw.csv',encoding='utf-8') as f:
    rows = csv.reader(f,delimiter=",")
    contact_list = list(rows)


for contact in contact_list:
    person = " ".join(contact[:3])
    new_contact = person.split()
    while len(new_contact)<3:
        new_contact.append("")
    contact[:3] = new_contact

pprint(contact_list)

phone_pattern = r"(\+7|8)?\s?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s*]?(\d{2})(?:\s*\(?\s*доб\.?\s*(\d+)\s*\)?)?"
def format_phone(match):
    base = f'+7({match.group(2)}){match.group(3)}-{match.group(4)}-{match.group(5)}'
    ext = match.group(6)
    if ext:
        return f'{base} доб.{ext}'
    return base

for contact in contact_list:
    contact[5] = re.sub(phone_pattern,format_phone,contact[5])
pprint(contact_list)

person = {}
for contact in contact_list[1:]:
    key = (contact[0],contact[1])
    if key not in person:
        person[key] = contact[:]
    else:
        old = person[key]
        new = contact
        for i in range(len(old)):
            if not old[i] and new[i]:
                old[i] = new[i]
new_contact_list = [contact_list[0]]
for value in person.values():
    new_contact_list.append(value)
pprint(new_contact_list)

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contact_list)






