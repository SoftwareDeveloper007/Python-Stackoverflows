import string

alphabets = string.ascii_lowercase

alphabets = string.ascii_uppercase

for i in alphabets:
    print(i)

alphabets_list = []
for c in alphabets:
    alphabets_list.append("'{}'".format(c))
alphabets_str = ", ".join(alphabets_list)
print(alphabets_str)
