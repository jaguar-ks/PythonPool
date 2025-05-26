from load_csv import load
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def renderGraph(gdp: pd.DataFrame, le: pd.DataFrame) -> None:
    """
    Render a graph of life expectancy vs GDP per capita for the year 1900.

    Parameters:
        gdp_data (pd.DataFrame): The dataset containing GDP per capita.
        life_expectancy_data (pd.DataFrame): The dataset containing
        life expectancy.
    """
    try:
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=gdp['1900'], y=le['1900'])
        plt.xscale('log')
        plt.title('1900')
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expectancy')
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
        plt.xlim(300, 10100)
        plt.show()
    except Exception as e:
        print('Rendering the Graph:', e)


if __name__ == '__main__':
    try:
        gdp = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
        le = load('life_expectancy_years.csv')
        renderGraph(gdp, le)
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
