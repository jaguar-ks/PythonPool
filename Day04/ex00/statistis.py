from typing import Any
import numpy as np
import pandas as pd


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    ds = pd.Series(args)
    d = ds.describe()
    for k in kwargs.values():
        if ds.empty:
            print('ERROR')
            continue
        if k=='quartile':
            print(k, ':', d.loc[['25%', '75%']].to_list())
            pass
        if hasattr(ds, k):
            method = getattr(ds, k)
            print(k, ':', method())

if __name__ == '__main__':
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")
