def my_function(x: list) -> list:
    x.append(5)
    print(id(x))
    return x


x = [1, 2, 3]
print(id(x))
y = my_function(x)

print(y)
