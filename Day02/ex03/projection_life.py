from . import load
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError('Invalid number of arguments!')
        ds: pd.DataFrame = load(sys.argv[1])
        pass
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
