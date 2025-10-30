a = 7
b = 4
c = [3, 23, 6]
d = c

print('same: ', a == b)
print('not same: ', a != b)
print('greater: ', a > b)
print('less: ', a < b)
print('less equal: ', a <= b)
print('greater equal: ', a >= b)
print('o in John: ', 'o' in 'John')
print('o not in John: ', 'o' not in 'John')
print('c is d: ', c is d)
print('id(c), id(d): ', id(c), id(d))
print('int(False): ', int(False))
print('int(True): ', int(True))
print('bool(\'parrot\'): ', bool('parrot'))
print('bool(\' \'): ', bool(' '))
print('bool(\'\'): ', bool(''))
print('bool(42): ', bool(42))
print('bool(1): ', bool(1))
print('bool(0): ', bool(0))
print('42 + True: ', 42 + True)
print('42 + False: ', 42 + False)