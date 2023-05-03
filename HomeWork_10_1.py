slovo = (input("Введіть слово поліндром: "))
a = slovo[::-1]
if slovo == a:
  print("+")
else:
  print("-")
