list_append = [1, 2, 3]
print(list_append)
list_append.append(4)
print ("append num 4 to list =" ,list_append)
list_append.append(5)
print ("append num 5 to list =" ,list_append)

list_extend = [4, 5, 6]
print(list_extend)
list_extend1 = [7, 8, 9]
list_extend.extend(list_extend1)
print("extend list with 7 ,8 ,9 =" ,list_extend)
x = list_extend.index(6)
print ('find index of num 6 =', x)

x1 = len(list_append)
print("find length of first list =" ,x1)

