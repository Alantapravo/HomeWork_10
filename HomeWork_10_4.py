text = input("Введіть текст: ")
result = ''.join([i for i in text if not i.isdigit()])
print(result)