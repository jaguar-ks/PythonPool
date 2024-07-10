import sys
from string import punctuation


def main():
    """
    This function takes user input or command line argument
    and performs character analysis on it.
    It counts the number of upper letters,
    lower letters, punctuation marks, spaces,
    and digits in the input string.
    """

    s = ''
    try:
        if len(sys.argv) > 2:
            raise AssertionError('more than one argument is provided')
        elif len(sys.argv) == 1 or sys.argv[1] == '':
            s = input('Enter your string here: ')
        else:
            s = sys.argv[1]
        print(f"The test contains {len(s)} characters:")
        print(f"{sum(1 for i in s if i.isupper())} upper letters")
        print(f"{sum(1 for i in s if i.islower())} lower letters")
        print(f"{sum(1 for i in s if i in punctuation)} punctuation marks")
        print(f"{s.count(' ')} spaces")
        print(f"{sum(1 for i in s if i.isdigit())} digits")
    except Exception as e:
        print('AssertionError:', e)
        sys.exit(1)


if __name__ == '__main__':
    main()
