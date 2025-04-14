import pandas as pd
from load_csv import load
import sys
import matplotlib.pyplot as plt


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
        nds.rename(columns={106: 'Morocco'}, inplace=True)
        nds['Year'] = pd.to_numeric(nds['Year'], errors='coerce')
        nds.plot.line(x='Year',
                      ylabel='Population',
                      title='Population over the years of France and Morocco'
                      )
        # plt.show()
        plt.savefig("plot.png")
        # print(nds)
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
