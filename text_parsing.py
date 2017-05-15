# -*- coding: utf-8 -*-

import re

f = open('F:/python3/testcase1.txt','r').read()
r = open('F:/python3/testcase1.txt','r').readlines()

tables = re.findall('<TABLE>.*?<\/TABLE>',f,re.DOTALL)
print('No of Tables in Document: ' + str(len(tables)))

caption=[]
for table in tables:
    table_split = table.split('\n')
    i =0
    a=[]
    while(i < len(table_split)):
        i+=1
        try:
            while(table_split[i].strip() !='<CAPTION>'):
                a.append(table_split[i])
                i+=1
            caption.append(' '.join(a))
        except Exception as e:
            cap = re.findall('<LEGEND>.*?<\/LEGEND>',f,re.DOTALL)[0]
            cap = cap.replace('<LEGEND>','')
            cap = cap.replace('</LEGEND>','')
            caption.append(cap)
        break

column_contents=[]
for table in tables:
    table_split = table.split('\n')
    try:
        index1= table_split.index('<CAPTION>') +1
    except ValueError:
        index1 = 0
    for j in range(index1,len(table_split)):
        if '<S>' in table_split[j]:
            index2 = j
            column_contents.append(table_split[index1:index2])
            break
        else:
            pass

def clean_content(contents):
    clean_content=[]
    for content in contents:
        a=[]
        for cont in content:
            if '--' in cont.strip() or len(cont.strip())< 1:
                pass
            else:
                a.append(cont)
        clean_content.append(a)
    return clean_content
 
clean_column_content = clean_content(column_contents)      

columns=[]

for content in clean_column_content:
    b = content[-2:]
    try:
        bs1 = re.split(r'\s{3,}', b[0])
        bs2 = re.split(r'\s{3,}', b[1])
        bs1.remove(bs1[0])
        bs2.remove(bs2[0])
        if len(bs1) == len(bs2):
            lenbs = len(bs1)
            a = []
            for j in range(0,lenbs):
                a.append(bs1[j] + ' ' + bs2[j])
            columns.append(a)
        elif len(bs1) != len(bs2):
            if len(bs2) > len(bs1):
               a =[]
               for i in range(0,len(bs2)):
                   a.append(bs2[i])
               columns.append(a)
    except IndexError:
        columns.append(['Summary'])

actual_content=[]
for table in tables:
    table_split = table.split('\n')
    for i in range(0,len(table_split)):
        if '<S>' in table_split[i] and '<C>' in table_split[i]:
            index=i+1
            actual_content.append(table_split[index:len(table_split)-1])
            break
        else:
            pass

clean_actual_content = clean_content(actual_content) 

        
    
