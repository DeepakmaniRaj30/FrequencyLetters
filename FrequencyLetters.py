test_str = "mississippi"
dict = {}
for keys in test_str:
    dict[keys] = dict.get(keys, 0) + 1
print (" characters in mississippi is : \n"+ str(dict))


