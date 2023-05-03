address = input('Введіть електронну пошту: ')
checked = True
symbols_count = 0
symbols_point = 0

for i in address:
    symbols_count += 1 if i == '@' else 0
for i in address:
    symbols_point += 1 if i == '.' else 0

if symbols_count and symbols_point == 1:
    print('YES')
else:
    print('NO')