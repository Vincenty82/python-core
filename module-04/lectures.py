# scores = [4, 5, 5, 4, 5, 5, 5, 2]

# scores.sort(reverse=False)

# scores.append([42, 2*42])

# scores.extend([100, 200, 300])

# scores.insert(0, [100, 200])

# x = scores.pop()

# y = scores.count([100, 200])

# z = scores.index(5, 6 ,7)

# print(scores)
# scores.reverse()
# print(scores)
# print(f"pop x = {x}")
# print(f"count y = {y}")
# print(f"position z = {z}")

# import copy
# letters = ["a", "b", "c"]

# items = [1, 2, 3, letters]

# items_copy = items.copy()
# items_deepcopy = copy.deepcopy(items)

# letters.append("d")

# print(letters)
# print(items)
# print(items_copy)
# print(items_deepcopy)

phones = {
    "Bob Marley": "22-33-44",
    "Britney Spears": "33-44-55",
    "John Doe": "44-55-66",
    }

for key, value in phones.items():
    print(key, value)

print(phones.get("????", "Uknown key"))