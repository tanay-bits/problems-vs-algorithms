word = "/"
parts = word.split("/")
print(parts)
while "" in parts:
    parts.remove("")
print(parts)

