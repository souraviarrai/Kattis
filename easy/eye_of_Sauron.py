user_input = input()
bars = user_input.split('()')
if len(bars[0]) == len(bars[1]):
    print('correct')
else:
    print('fix')