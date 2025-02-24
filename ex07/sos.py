import sys

# Morse code dictionary
NESTED_MORSE = {
    " ": "/ ", "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
    "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
    "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
    "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ",
    "Z": "--.. ", "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
    "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ", "8": "---.. ",
    "9": "----. "
}


def encode_morse(text):
    """
    Encodes a given text into Morse Code.

    Args:
        text (str): The input string to encode.

    Returns:
        str: The encoded Morse Code string.
    """
    text = text.upper()

    if any(char not in NESTED_MORSE for char in text):
        raise AssertionError("AssertionError: the arguments are bad")

    return "".join(NESTED_MORSE[char] for char in text).strip()


def main():
    """Main function to handle argument validation and Morse Code
    conversion."""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("AssertionError: the arguments are bad")

        text = sys.argv[1]
        print(encode_morse(text), end="")

    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
