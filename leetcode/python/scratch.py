clés = ["a", "b", "c"]
valeurs = [1, 2, 3]

# d = dict(zip(clés, valeurs))
# print(d)


for x, y in zip(clés, range(len(clés))):
    print(x, y)