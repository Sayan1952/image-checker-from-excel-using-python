import os
import pandas as pd
#directing to the folder where images are placed
images = os.listdir('images/')
my_list = []
an_list =[]
count = 0
#extracting image name aka student id
for i in images:
    img = i.split('.')[0]
    my_list.append(img)
    count+=1
#loading csv file for comparison
exl = pd.read_csv('RMA _ Membership Registration for 20 Batch (Responses) - Form Responses 1.csv')
#print(exl["Student ID"])

clm = exl["Student ID"]
for i in clm:
    an_list.append(i)

print(len(an_list))
print(len(my_list))
my_new_list = []
left = []
#comparing,the left out data are stored in left list
for i in my_list:
    my_new_list.append(int(i))
for i in range(217):
    if an_list[i] in my_new_list:
        pass
    else:
        left.append(an_list[i])


print(left)