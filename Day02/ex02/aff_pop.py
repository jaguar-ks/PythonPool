import pandas as pd
from load_csv import load
import sys
import matplotlib.pyplot as plt
import numpy as np


def renderGraph(ds: pd.DataFrame) -> None:
    """
    Renders a graph of life expectancy over the years for
    Belgium and Morocco.

    Args:
        ds (pd.DataFrame): The input DataFrame containing
        life expectancy data.

    Returns:
        None
    """
    try:
        ds = ds.T
        ds.reset_index(inplace=True)
        ds.rename(columns={'index': 'Year'}, inplace=True)
        ds['Year'] = pd.to_numeric(ds['Year'], errors='coerce')
        plt.yticks(ticks=np.arange(min(ds['Belgium']),
                                   max(ds['Belgium']),
                                   20),
                   rotation=45)
        plt.xticks(ticks=np.arange(1800, 2050, 40))
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.plot(ds['Year'], ds['Belgium'], label='Belgium')
        plt.plot(ds['Year'], ds['Morocco'], label='Morocco')
        plt.legend()
        plt.show()
        pass
    except Exception as e:
        print('Rendering the Graph:', e)


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError('Invalide number of argumnets!')
        ds: pd.DataFrame = load(sys.argv[1])
        renderGraph(ds)
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
