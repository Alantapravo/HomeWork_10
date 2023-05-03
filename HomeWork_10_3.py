text = input('Введіть текст: ')
if text.startswith('abc'):
    new_text = 'www' + text[3:]
else:
    new_text = text + 'qqq'
print(new_text)