# ========== LISTS ==========
li = [1, 2, 3, 4, 5]
li2 = [False, "hello", 1, 5]

# access index
print(li[3])

# list slicing
print(li[0:3])
print(li2[0:])

# matrix or multidimensional list
# this is a list of two dimensions
matrix = [[1, 2, 3], [2, 4, 6], [7, 8, 9]]

# assing elemetns to a list
li.append(100)
print(li)
li.insert(5, 50)
print(li)
li.extend([110, 120])
print(li)

# removing elemetns to a list
li.pop()
print(li)
li.pop(0)
print(li)
li.remove(4)
print(li)

# there are many more, you can research in the python documentation
li.index(100)
100 in li
li.count(100)

None  # represent the absense of value


# ========== DICTIONARY ==========
dictionary = {"a": 1, "b": 2, "name": "Karen", "age": 20, "isDev": True}
