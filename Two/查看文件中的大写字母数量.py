import os

os.chdir('G:\\PCC2')
with open('11.txt') as today:
    count=0
    for i in today.read():
        if i.isupper():
            count+=1
print("hah:",count)