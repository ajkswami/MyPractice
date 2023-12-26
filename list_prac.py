import math
from functools import reduce


num_list = [100,55,112,-5,95,1,78]




print(num_list)

#print(len(num_list))

num_list.append(23)
#print(num_list)
num_list.remove(23)
#print(num_list)

num_list.insert(3,99)
#print(num_list)

#num_list.pop()
#print("List removed val",num_list.pop())
#print(num_list)

# num_list.extend([23,1000,-9,0.9])
print(num_list)

removable_list = [95,100,1]

for item in removable_list:
    num_list.remove(item)

print(num_list)

addable_list = [95,100,1]

for item in addable_list:
    num_list.extend([item])



print(num_list)









# num_list.remove([23,1000,-9,0.9])
# print(num_list)




num_list = [100,55,112,-5,95,1,78]

pre_old_list = []

for item in num_list:
    pre_old_list.append(item)

print(pre_old_list)




print(f"Old  list is {num_list}")
#pre_old_list = num_list
to_remove=[112,95]

for item in to_remove:
    num_list.remove(item)


new_list = num_list

new_list.append(95)
print(new_list)
old_list = new_list

addable_item = [100,75]

for item in addable_item:
    new_list.extend([item])

print(new_list)



new_list.sort()
print(new_list)

new_list.sort(reverse=True)
print(f"new_list is {new_list}")

print(f"old list is {pre_old_list}")


print(sum(new_list))

mul_list= [1,2,3,4,5]

prod = 1

for item in mul_list:
    prod *=item
#print(prod)



prod = reduce(lambda x, y : x*y ,mul_list )

minus = reduce(lambda x,y: x-y,mul_list)

result = reduce(lambda x, y: x - y, mul_list[1:], mul_list[0])

avg_result = reduce(lambda x, y: x + y, mul_list) / len(mul_list)


avg_result = reduce(lambda x,y :x+y,mul_list)/len(mul_list)


print(mul_list)
print(prod)
print(minus)
print(result)


print(avg_result)

print(new_list)

print(max(new_list))
print(min(new_list))

avg_val = reduce(lambda x,y : x+y , new_list )/len(new_list)

len_val = len(new_list)
mid_val = len_val/2
print(mid_val)

print(f"Mid val of list {new_list} is {new_list[3]}")

print(avg_val)

str_list = ["Sam","Manisha", "Raju","kedar","lucky"]





