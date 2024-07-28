import pandas as pd
from load_csv import load
import sys
import matplotlib.pyplot as plt
import seaborn as sns


def renderGraph(ds: pd.DataFrame) -> None:
    """
    Render a graph of the dataset.

    Parameters:
        ds (pd.DataFrame): The dataset to render.
    """
    sns.lineplot(data=ds['Morocco']).set(
        xlabel='Years',
        ylabel='Life expectancy',
        title='Morocco life expectancy projection'
    )
    # ds['Morocco'].plot().lines[0].set_linestyle('-')
    plt.show()


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError('Invalide number of argumnets!')
        ds: pd.DataFrame = load(sys.argv[1])
        k = ds.T
        renderGraph(k)
        pass
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
