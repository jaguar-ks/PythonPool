import pandas as pd
from load_csv import load
import sys
import matplotlib.pyplot as plt

if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError('Invalide number of argumnets!')
        ds: pd.DataFrame = load(sys.argv[1])
        pass
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
