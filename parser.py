import string
alphabet=list(string.ascii_lowercase)
title=""
text_list=[]
with open('test2.mrexpt') as moonreader_file:
    for line in moonreader_file:
        for letter in alphabet:
            if line.lower().startswith(letter):
                text_list.append(line)

title=text_list[2]
for txt in text_list[3:]:
    if txt!=title:
        print("* " + txt.rstrip().replace('<BR>',''))