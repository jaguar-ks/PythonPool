from typing import Any
import pandas as pd


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    ds = pd.Series(args)
    d = ds.describe()
    for k in kwargs.values():
        if ds.empty:
            print('ERROR')
            continue
        if k == 'quartile':
            print(k, ':', d.loc[['25%', '75%']].to_list())
            pass
        if hasattr(ds, k):
            method = getattr(ds, k)
            print(k, ':', method())
