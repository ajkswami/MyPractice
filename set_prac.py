
set_list = {55,-100,22,3}
#print(set_list)

set_list.add(5)
#print(set_list)

set_list.remove(5)
print(set_list)

set_list_2= {12,1,5,55,3}

set_list_3 = set_list.union(set_list_2)
print(set_list_3)
set_list_4 = set_list.intersection(set_list_2)
print(set_list_4)

set_list_5 = set_list.symmetric_difference(set_list_2)
print(set_list_5)

print("New")

new_set = set()

for i in set_list:
    new_set.add(i)

print(new_set)




