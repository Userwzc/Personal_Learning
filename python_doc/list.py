l = [1,2,3,4,5]

# append
l.append(6)
print(l)
# extend
l.extend([7,8,9])
print(l)
# insert
l.insert(0,0)
print(l)
# remove
l.remove(3)
print(l)
# pop
l.pop()
print(l)
l.pop(2)  # remove index 2
l.pop(0)
print(l)
# index
print(l.index(4))     # find index of value 4
# count
print(l.count(2))    # count occurrences of value 2
# sort
l.sort(reverse=True) # sort in descending order
print(l)
# reverse
l.reverse()      # reverse the list
print(l)
# copy
l2 = l.copy()    # shallow copy
print(l2)
# clear
l.clear()   # clear the list
print(l)


# queue

from collections import deque
queue = deque([1,2,3])
queue.append(4)   # enqueue
print(queue)
queue.popleft() # dequeue
print(queue)
queue.pop() # dequeue from right
print(queue)

# list comprehension
squares = [x**2 for x in range(10)]
print(squares)

squares_even = [x**2 for x in range(10) if x % 2 == 0]
print(squares_even)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

# Transpose a matrix
matrix = [[1,2,3], [4,5,6], [7,8,9]]
transposed = [ [row[i] for row in matrix] for i in range(3)]
print(transposed)
# equivalent to
transposed = []
for i in range(3):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

# zip 
transposed = list(zip(*matrix))
print(transposed)