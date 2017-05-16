# -*- coding: utf-8 -*-

import re
import string

f = open('U:/python/testcase1.txt','r').read()
#r = open('U:/python/testcase1.txt','r').readlines()

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

print(caption[8])


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
        columns.append(['SUMMARY'])

print(columns[8])

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

def trim(wordlist):
    new_list=[]
    for word in wordlist:
        if len(word) < 2:
            pass
        else:
            new_list.append(word)
    return new_list

overall_content=[]
for content in clean_actual_content:
    content1=[]
    for i in range(0,len(content)):
        word1= trim(re.split(r'\s{3,}', content[i]))
        content1.append(word1)
    overall_content.append(content1)

leno = len(overall_content)
for i in range(0,len(overall_content[leno-1])):
    if '<S>' in overall_content[leno-1][i]:
        index = i+1
        break
    else:
        pass

add_overall = overall_content[(leno-1)][index : len(overall_content[leno-1])]
overall_content.remove(overall_content[leno-1])
overall_content.append(add_overall)
print(overall_content[8])
#print(overall_content[8])
save_tables = open('U:/python/testcase_result.tsv','w')

for i in range(0,len(tables)):

    save_tables.write('\nTABLE NO - ' + str(i+1) + '\n')
    save_tables.write(caption[i] + '\t' + '\t'.join(columns[i]) + '\n')
    for j in range(0,len(overall_content[i])):
        save_tables.write('\t'.join(overall_content[i][j]) + '\n')




# def space_count_list(content_list):
#     space_len=[]
#     for i in range(0,len(content_list)):
#         for char in content_list[i]:
#             if char[0] in list(string.ascii_letters):
#                 space_len.append(0)
#                 break
#             else:
#                 a=[]
#                 for char in content_list[i]:
#                     a.append(char)
#                 space=[]
#                 j =-1
#                 while(j<len(a)-1):
#                     j+=1
#                     while(a[j] == ' '):
#                         space.append(a[j])
#                         j+=1
#                     break
#                 space_len.append(len(space))
#                 break
#
#     return space_len
#
#
# print(clean_actual_content[7])
# space_len = space_count_list(clean_actual_content[7])
#
# print(space_len)
#
#
# def size_reduction1(clean_content):
#     space_len = space_count_list(clean_content)
#     contents_table=[]
#     j=0
#     try:
#         while (j< len(clean_content)):
#             if space_len[j] == space_len[j+1] ==0 :
#                 contents_table.append(clean_content[j])
#                 j+=1
#             elif space_len[j+1] > space_len[j] and space_len[j]!=0:
#                 a=[]
#                 count=0
#                 while(space_len[j+1] > space_len[j]):
#                     a.append(clean_content[j] + ' ' + clean_content[j+1].strip())
#                     j+=1
#                     count+=1
#                 contents_table.append(' '.join(a))
#                 j=j+count
#             elif space_len[j] == space_len[j+1]:
#                 contents_table.append(clean_content[j])
#                 contents_table.append(clean_content[j+1])
#                 j+=2
#             else:
#                 contents_table.append(clean_content[j])
#                 j+=1
#     except Exception as e:
#         pass
#
#     return contents_table
#
# content_table = size_reduction1(clean_actual_content[7])
# space_size = space_count_list(clean_actual_content[7])
# space_size2 = space_count_list(content_table)
# print(space_size2)
# print(content_table)
#
#
# def size_reduction2(contents_table,space_table_content):
#     contents_table12=[]
#     try:
#         j=0
#         while (j< len(space_table_content)):
#             if space_table_content[j+1] > space_table_content[j]:
#                 index = j
#                 try:
#                     a=[]
#                     while (space_table_content[index] != space_table_content[j+1]):
#                         a.append(contents_table[index]  + contents_table[j+1])
#                         j+=1
#                 except Exception as e:
#                     pass
#                 for elem in a:
#                     contents_table12.append(elem)
#                 j= j+1
#             else:
#                 contents_table12.append(contents_table[j])
#                 j+=1
#
#     except Exception as e:
#         pass
#     return contents_table12
#
#
# print(contents_table12)

# space_table_content = space_count_list(clean_actual_content[7])
# print(space_table_content)

# contents_table = size_reduction2(clean_actual_content[7],space_len)
# print(contents_table)
# print(len(contents_table))



#for i in range(0,len(contents_table)):

