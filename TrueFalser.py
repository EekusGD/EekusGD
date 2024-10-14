print('Type something, and i will turn it into False or True. ')
k = True
while k == True:
    x = input('- $ ')
    def start():
        y = x.lower().isdigit()
        if y == False:
            print('False (chance 97.72839)')
        elif y == True:
            print('True (chance 85.02837)')
        else:
            print('NULL (chance 0.0019)')
    def error():
        k = False
        y = 'jsjwjsjd'
        x = ''
        while True:
            print('ERROR: WRONG NULL FOUND')
            print(f"FOR SOME REASON y = {y}")
    if (x):
        start()
    else:
        error()