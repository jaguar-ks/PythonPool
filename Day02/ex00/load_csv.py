import pandas as pd
import numpy as np
import sys


def load(path: str) -> pd.DataFrame:
    try:
        pass
    except Exception as e:
        print('LoadError:', e)
        return None


def main() -> None:
    try:
        if len(sys.argv) != 2:
            raise ValueError('Invalide number of arguments!')
        ds = load(sys.argv[1])
        if not ds:
            raise ValueError('load error accured!')
    except Exception as e:
        print('Error:', e)


if __name__ == '__main__':
    main()
