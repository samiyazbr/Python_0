import sys
import time
import shutil


def ft_tqdm(lst: range):
    """
    A custom implementation of tqdm that closely mimics the original tqdm.

    Args:
        lst (range): A range object to iterate over.

    Yields:
        int: The next value in the range while displaying a progress bar.
    """
    total = len(lst)
    start_time = time.time()

    for i, elem in enumerate(lst, 1):
        elapsed_time = time.time() - start_time
        speed = i / elapsed_time if elapsed_time > 0 else 0  # Iterations per second
        eta = (total - i) / speed if speed > 0 else 0  # Estimated Time Remaining

        # Get terminal width dynamically
        terminal_width = shutil.get_terminal_size((80, 20)).columns
        bar_length = max(30, terminal_width - 40)  # Adjust width for text space

        # Progress percentage
        progress = (i / total)
        filled_length = int(bar_length * progress)
        empty_length = bar_length - filled_length

        # Progress bar visualization
        bar = "█" * filled_length + " " * (empty_length - 1)

        # Formatting elapsed time and ETA like tqdm
        elapsed_str = time.strftime("%M:%S", time.gmtime(elapsed_time))
        eta_str = time.strftime("%M:%S", time.gmtime(eta)) if eta > 0 else "00:00"

        if i > 1:
            sys.stdout.write(
                f"\r{progress * 100:3.0f}%|{bar}| {i}/{total} [{elapsed_str}<{eta_str}, {speed:.2f}it/s]"
            )
            sys.stdout.flush()

        yield elem

    print()  # Move to the next line after completion
