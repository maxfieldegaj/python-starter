corrupt_file = 'corrupt_file.txt'
test_file='test_file.txt'

try:
    f = open(corrupt_file)
    # if f.name == 'corrupt_file.txt':
    #     raise Exception
except FileNotFoundError:
    print('Sorry, this file doesn\'t exist')
except Exception:
    print('Sorry something went wrong')
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally... shut \'er down')
    pass