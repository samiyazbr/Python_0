import sys
from ft_filter import ft_filter


def main():
    """Main function to validate arguments and filter words."""
    try:
        # Ensure exactly two arguments are passed
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments \
are bad")

        S, N = sys.argv[1], sys.argv[2]

        # Ensure the second argument is an integer
        if not N.isdigit():
            raise AssertionError("AssertionError: the arguments are bad")

        N = int(N)

        # Filter words longer than N
        words = S.split()
        filtered_words = list(ft_filter(lambda word: len(word) > N, words))

        print(filtered_words)

    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
