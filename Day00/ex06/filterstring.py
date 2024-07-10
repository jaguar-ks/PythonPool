from ft_filter import ft_filter
import sys


def main():
    """
    This function takes two command-line arguments and filters a list
    of strings based on a given length.

    Args:
        None

    Returns:
        None
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        else:
            for i in sys.argv[2]:
                if not i.isdigit():
                    raise AssertionError("the arguments are bad")
            nbr = int(sys.argv[2])
            print(ft_filter(lambda s: len(s) > nbr, sys.argv[1].split()))
            # print(ft_filter.__doc__)
    except Exception as e:
        print('AssertionError:', e)


if __name__ == '__main__':
    main()
