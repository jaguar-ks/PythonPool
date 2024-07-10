import sys

if __name__ == '__main__':
    try:
        if len(sys.argv) > 2:
            raise AssertionError('more than one argument is provided')
        elif len(sys.argv) == 2:
            for i in sys.argv[1]:
                if not i.isdigit():
                    raise AssertionError('argument is not an integer')
            print('I\'m Even' if int(sys.argv[1]) % 2 == 0 else 'I\'m Odd')
    except Exception as e:
        print('AssertionError:', e)
        sys.exit(1)