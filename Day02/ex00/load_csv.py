import pandas as pd
import sys


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Parameters:
        path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded dataset as a pandas DataFrame,
        or None if an error occurs.
    """
    try:
        ds: pd.DataFrame = pd.read_csv(path)
        print('Loading a dataset of dimensions of', ds.shape)
        return ds
    except Exception as e:
        print('LoadError:', e)
        return None


def main() -> None:
    """
    Entry point of the program.

    This function loads a CSV file specified as a command line
    argument and prints its contents.
    If any error occurs during the loading process, an error
    message is printed.
    """
    try:
        if len(sys.argv) != 2:
            raise ValueError('Invalid number of arguments!')
        ds = load(sys.argv[1])
        if ds is None or ds.empty:
            raise ValueError('Load error occurred!')
        print(ds)
    except Exception as e:
        print('Error:', e)


if __name__ == '__main__':
    main()
