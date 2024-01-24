import numpy as np
a = np.array([ [1,1], [1,1]])
b = np.array([ [1,1], [1,1]])
total = a.dot(b)
print(total)


a = np.array([ [1, 2], [3, 4]])
b = np.array([ [5,6], [7,8] ])
total = a.dot(b)
print(total)

#Завдання
#Обчисли аналітично, а потім створи програмне розв'язання.

c = np.array([ [4, 6], [3, 2]])
d = np.array([ [8,2], [3,1] ])
total = c.dot(d)
print(total)

print("-----")

e = np.array([ [2, 3], [6, 1]])
f = np.array([ [2,5], [1,3] ])
total = e.dot(f)
print(total)

print("-----")

g = np.array([ [9, 2], [7, 3]])
h = np.array([ [5,4], [1,1] ])
total = g.dot(h)
print(total)

print("-----")

a = np.array([ [1, 2], [3, 4], [5, 6]])
b = np.array([ [7, 8, 9], [10, 11, 12] ])
total = a.dot(b)    
print(total)

print("-----")

a = np.array([ [1, 1], [2, 2], [3, 3], [4, 4], [5,5]  ])
b = np.array([ [1,1,1], [2,2,2] ])
print(f"a:", a)
print(f"b:", b)
total = a.dot(b)
print(total)