def stringMath(s):
    operators = ['+', '-', '*', '/']
    ops = []
    numbers = []
    number = ''
    for i, x in enumerate(s):
        if x in operators:
            numbers.append(int(number))
            number = ''
            ops.append(x)
        elif i == len(s)-1:
            number += x
            numbers.append(int(number))
        else:
            number += x
    print(numbers)
    print(ops)
    while '*' in ops or '/' in ops:
        for i, op in enumerate(ops):
            if op == '/':
                numbers[i] = numbers[i] / numbers[i+1]
                numbers.pop(i+1)
                ops.pop(i)
            if op == '*':
                numbers[i] = numbers[i] * numbers[i+1]
                numbers.pop(i+1)
                ops.pop(i)
    for op in ops:
        if op == '+':
            numbers[0] = numbers[0] + numbers[1]
            numbers.pop(1)
        if op == '-':
            numbers[0] = numbers[0] - numbers[1]
            numbers.pop(1)
    print(numbers[0])


s1 = "5+5"
s2 = "10-5+5*2/2+10"

stringMath(s2)