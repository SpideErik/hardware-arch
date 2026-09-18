a = 3
b = 5

c = a & b
print(f'  a {a:04b}')
print(f'  b {b:04b}')
print(f'a&b {c:04b}')
print(f'{a} & {b} = {c}') 
print()

c = a | b
print(f'  a {a:04b}')
print(f'  b {b:04b}')
print(f'a|b {c:04b}')
print(f'{a} | {b} = {c}') 
print()

c = a ^ b
print(f'  a {a:04b}')
print(f'  b {b:04b}')
print(f'a^b {c:04b}')
print(f'{a} ^ {b} = {c}') 
print()

# Импликация a -> b == ~a | b
# ограничим число бит 4
c = (~a | b) & 0xf
print(f'   a {a:04b}')
print(f'   b {b:04b}')
print(f'a->b {c:04b}')
print(f'(~{a} | {b}) & 0xf = {c}') 
print()


