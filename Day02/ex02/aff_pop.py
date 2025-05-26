import pandas as pd
from load_csv import load
import sys
import matplotlib.pyplot as plt


def convert_to_num(val: str) -> float:
    """
    Convert from an str representation of a number to
    the actual folat number

    Args:
        val (str): the str representation of a number

    Returns:
        the actual float number
    """
    if 'M' in val:
        return float(val.replace('M', '')) * 1_000_000
    elif 'k' in val:
        return float(val.replace('k', '')) * 1_000
    else:
        return float(val)


def renderGraph(ds: pd.DataFrame) -> None:
    """
    Renders a graph of Population over the years for
    France and Morocco.

    Args:
        ds (pd.DataFrame): The input DataFrame containing
        population data.

    Returns:
        None
    """
    try:
        nds = ds.loc[ds.country.isin(['Morocco', 'France']),
                     '1800':'2050']
        nds = nds.T
        nds.reset_index(inplace=True)
        nds.rename(columns={'index': 'Year'}, inplace=True)
        nds.rename(columns={58: 'France'}, inplace=True)
        nds.rename(columns={108: 'Morocco'}, inplace=True)
        nds['Year'] = pd.to_numeric(nds['Year'], errors='coerce')
        nds['Morocco'] = nds['Morocco'].apply(convert_to_num)
        nds['France'] = nds['France'].apply(convert_to_num)
        print(nds.head())
        nds.plot.line(x='Year',
                      ylabel='Population',
                      title='Population over the years of France and Morocco'
                      )
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
