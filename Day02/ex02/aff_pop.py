import pandas as pd
from load_csv import load
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def renderGraph(ds: pd.DataFrame) -> None:
    """
    Renders a line graph showing the life expectancy projection
    for Morocco and Monaco over the years.

    Args:
        ds (pd.DataFrame): The input DataFrame containing
        the life expectancy data.

    Returns:
        None
    """
    try:
        ds = ds.T
        ds.reset_index(inplace=True)
        ds.rename(columns={'index': 'Year'}, inplace=True)
        ds['Year'] = pd.to_numeric(ds['Year'], errors='coerce')
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='Year', y='Morocco', data=ds).set(
            xlabel='Years',
            ylabel='Life expectancy',
            title='Morocco life expectancy projection'
        )
        sns.lineplot(x='Year', y='Monaco', data=ds)
        plt.xticks(ticks=np.arange(1800, 2100, 20), rotation=45)
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
