
new_dict ={"Name":"Kedar","Age":30,"Percentage":76.8}

print(new_dict)

print(new_dict["Name"])

new_dict["isActive"]=True

print(new_dict)

new_dict["Name"]="Manisha"

print(new_dict)

print("Old")

# # for index,(keys,value) in  enumerate(new_dict.items()):
# #
# #
# #     print(index,keys,value)
#
#
#
# for key in new_dict:
#     print(key)
#
# for index,key in enumerate(new_dict):
#     print(index,key)
#
#
# for index, (key,value) in enumerate(new_dict.items()):
#     print(index,key,value)
#
# print(len(new_dict))
# print(type(new_dict))
#

dict_data = {}

for index,(key, value) in enumerate(new_dict.items()):
    dict_data.update({key:value})


print(dict_data)

print("Name" in dict_data)
print("Age" not in dict_data)

print(dict_data["Age"] is 30)

print(dict_data["isActive"] is True)









# for i in new_dict:
#     print(i,new_dict[i])

# del new_dict["isActive"]
#
# print(new_dict)

