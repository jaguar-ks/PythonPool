import pandas as pd
import numpy as np
import sys


def load(path: str) -> pd.DataFrame:
    try:
        ds: pd.DataFrame = pd.read_csv(path)
        print('Loading a dataset of dimensions of', ds.shape)
        
        return ds
    except Exception as e:
        print('LoadError:', e)
        return None


def main() -> None:
    try:
        if len(sys.argv) != 2:
            raise ValueError('Invalide number of arguments!')
        ds = load(sys.argv[1])
        if ds is None or ds.empty:
            raise ValueError('load error accured!')
        print(ds)
    except Exception as e:
        print('Error:', e)


if __name__ == '__main__':
    main()
