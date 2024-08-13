from load_csv import load
import sys
import pandas as pd
import matplotlib.pyplot as plt


def renderGraph(gdp: pd.DataFrame, le: pd.DataFrame) -> None:
    """
    Render a graph of life expectancy vs GDP per capita for the year 1900.

    Parameters:
        gdp_data (pd.DataFrame): The dataset containing GDP per capita.
        life_expectancy_data (pd.DataFrame): The dataset containing
        life expectancy.
    """
    try:
        plt.figure(figsize=(12, 6))
        plt.scatter(gdp['1900'], le['1900'])
        plt.xscale('log')
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expectancy')
        plt.title('1900')
        plt.xticks([300, 1000, 3000, 10000], ['300', '1k', '3k', '10k'])
        plt.xlim(300, 10000)
        plt.ylim(20, 55)
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
