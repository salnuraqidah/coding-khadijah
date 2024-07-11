(lambda name : print(f'hello {name}'))('salamah')
(lambda name : print(f'hello {name}'))('khadijah')

hello = lambda name, address: print(f'hello {name} from {address}')

hello('Susi', 'Jakarta')
hello('Rizky', 'Bali')
hello('Budi', 'Semarang')

is_even = lambda number : print('Even') if number % 2 == 0 else print('Odd')

is_even(2)
is_even(87)
is_even(39)
is_even(72)

addition = lambda num1,num2 : num1 + num2

print(addition(10,22))

