import numpy as np
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
    # Transpose the DataFrame if not already done
    ds = ds.T

    # Reset index to make 'Years' a column
    ds.reset_index(inplace=True)
    ds.rename(columns={'index': 'Year'}, inplace=True)

    # Convert index to numeric if necessary (optional)
    ds['Year'] = pd.to_numeric(ds['Year'], errors='coerce')

    # Plot the data
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Year', y='Morocco', data=ds).set(
        xlabel='Years',
        ylabel='Life expectancy',
        title='Morocco life expectancy projection'
    )

    # Customize the x-axis ticks
    plt.xticks(ticks=np.arange(1800, 2100, 20), rotation=45)

    # Display the plot
    plt.show()


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError('Invalide number of argumnets!')
        ds: pd.DataFrame = load(sys.argv[1])
        # k = ds.T
        renderGraph(ds)
        pass
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
