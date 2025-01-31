import sys
import string


def analyze_text(text: str):
    """
    Analyzes the text and counts different types of characters.
    Args:
        text (str): The input string to analyze.
    Returns:
        dict: A dictionary containing counts of character types.
    """
    analysis = {
        "total_characters": len(text),
        "upper_letters": sum(1 for char in text if char.isupper()),
        "lower_letters": sum(1 for char in text if char.islower()),
        "punctuation_marks": sum(1 for char in text if char in string.punctuation),
        "spaces": sum(1 for char in text if char.isspace()),
        "digits": sum(1 for char in text if char.isdigit()),
    }
    return analysis


def display_analysis(analysis: dict):
    """
    Prints the analysis results in the required format.
    Args:
        analysis (dict): The analysis result from analyze_text.
    """
    print(f"The text contains {analysis['total_characters']} characters:")
    print(f"{analysis['upper_letters']} upper letters")
    print(f"{analysis['lower_letters']} lower letters")
    print(f"{analysis['punctuation_marks']} punctuation marks")
    print(f"{analysis['spaces']} spaces")
    print(f"{analysis['digits']} digits")


def main():
    """
    Main function to handle input, validate arguments, and display results.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            text = input("What is the text to count?\n")

        analysis = analyze_text(text)
        display_analysis(analysis)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
