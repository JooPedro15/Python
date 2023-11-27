"""
order a list of tuples by the second index
"""
a = [(0, 2), (4, 3), (9, 9), (10, -2)]
a.sort(key=lambda index: index[1])
print(a)
