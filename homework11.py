define = lambda number: 'Ноль' if number == 0 else 'парное' if number % 2 == 0 else 'не парное'

number = 5

result = define(number)

print(f'Число {number} является {result}')
