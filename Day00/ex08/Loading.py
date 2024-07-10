from datetime import datetime
from datetime import timedelta
import shutil
# from time import sleep
# from tqdm import tqdm


def ft_tqdm(lst: range) -> None:
    """
    A custom implementation of tqdm (progress bar) for iterating over a range.

    Args:
        lst (range): The range to iterate over.

    Returns:
        None
    """
    total = len(lst)
    start_time = datetime.now()

    def show(j):
        t_w = shutil.get_terminal_size().columns
        b_l = t_w-len(f'{j}/{total} [00:00:00<00:00:00, 000.00it/s]')-10
        p = 100 * (j / float(total))
        f_l = int(b_l * j // total)
        bar = '█' * f_l + ' ' * (b_l - f_l)
        e_t = datetime.now() - start_time
        e_s = e_t.total_seconds()
        i_p_s = j / e_s if e_s > 0 else 0
        r_t = (total - j) / i_p_s if i_p_s > 0 else 0
        eta = timedelta(seconds=r_t)
        print(f'\r{p:.0f}%|{bar}| {j}/{total}',
              f'[{str(e_t).split(".")[0]}<{str(eta).split(".")[0]},',
              f'{i_p_s:.2f}it/s]', end='\r')

    show(0)
    for i, item in enumerate(lst):
        yield item
        show(i + 1)
    print()

# Example usage
# for item in ft_tqdm(range(333)):
#     sleep(0.005)

# for item in tqdm(range(333)):
#     sleep(0.005)
