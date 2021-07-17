import math

def PascalCal(n, k):
    if k == 0 or n == k:
        return 1
    elif n == k-1 or k == 1:
        return n
    else:
        return (math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

def PrintRow(n, cmd : bool):
    txt = ''
    for i in range(n):
        txt += (str(int(PascalCal(n-1 ,i))) + ' ')
    if cmd:
        print(txt)
    return txt

def PrintPascal(n):
    range_ = range(n[0], n[1]) if len(n) > 1 else range(n[0])
    txt = PrintRow(n[-1], False)
    space = len(txt)
    for i in range_:
        txt = PrintRow(i+1, False)
        print(txt.center(space))

if __name__ == '__main__':
    cmd = (True if chr(ord(input('Full or only row (f/r) : ')[0].lower())) == 'f' else False)
    if cmd:
        full_cmd = input('How much Row Do you want? (1 input for full, 2 inputs for start/stop): ').split()
        PrintPascal(list(map(int, full_cmd)))
    else:
        PrintRow(int(input('Which Row Do you want? : ')), True)