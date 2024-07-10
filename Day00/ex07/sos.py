import sys


MourceCode = {
    ' ': '/',
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}


def main():
    """
    Converts a given string into Morse code.

    The function takes a single command-line argument and converts
    each character of the argument into its corresponding Morse code
    representation.
    The Morse code representation is printed as a space-separated string.

    Raises:
        AssertionError: If the number of command-line arguments is not
        equal to 2 or if the argument contains invalid characters.

    Example:
        $ python sos.py "Hello World"
        .... . .-.. .-.. --- / .-- --- .-. .-.. -..
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        r = ''
        for i in sys.argv[1]:
            if i.isalpha():
                i = i.upper()
            if i.isalnum() or i == ' ':
                r += MourceCode[i] + ' '
            else:
                raise AssertionError("the arguments are bad")
        print(r)
    except Exception as e:
        print('AssertionError:', e)


if __name__ == '__main__':
    main()
