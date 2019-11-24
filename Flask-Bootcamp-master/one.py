#one.py
print('top (global) level in one.py')

def func():
    print('running func in one.py')

if __name__ == '__main__':
    print('one.py is run directly')
else:
    print('one.py is imported')
