import sys
import time


def ft_tqdm(lst: range):
    """
    A custom implementation of tqdm using yield.

    Args:
        lst (range): A range object to iterate over.

    Yields:
        int: The next value in the range while displaying a progress bar.
    """
    total = len(lst)
    start_time = time.time()

    for i, elem in enumerate(lst, 1):
        progress = (i / total) * 100
        bar_length = 50
        filled_length = int(bar_length * progress / 100)
        bar = "=" * filled_length + ">" + " " * (bar_length - filled_length)

        elapsed_time = time.time() - start_time
        # iterations per second
        speed = i / elapsed_time if elapsed_time > 0 else 0

        sys.stdout.write(f"\r{progress:.0f}%|[{bar}]| {i}/{total} [\
{elapsed_time:.2f}s, {speed:.2f}it/s]")
        sys.stdout.flush()

        yield elem

    print()  # Move to the next line after completion
