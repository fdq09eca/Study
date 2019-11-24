#two.py
print('top (global) in two.py here')

import one

def func():
    print('running func from two.py here.')

one.func()

if __name__ == '__main__':
    print('two.py is run directly')
else:
    print('two.py is imported')
