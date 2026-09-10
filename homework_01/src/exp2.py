print('| a | b | c | r |')
print('|--|--|--|--|')
for a in range(2):
    for b in range(2):
        for c in range(2):
            r = (a & b) | (~b & c)
            # нам нужен только младший бит (потому что ~ инвертирует все биты)
            r &= 1
            print(f'| {a} | {b} | {c} | {r} |')
