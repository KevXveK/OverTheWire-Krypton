import string
import sys


# Approximate English letter frequencies (%)
ENGLISH_FREQUENCY = {
    'a': 8.17,
    'b': 1.49,
    'c': 2.78,
    'd': 4.25,
    'e': 12.70,
    'f': 2.23,
    'g': 2.02,
    'h': 6.09,
    'i': 6.97,
    'j': 0.15,
    'k': 0.77,
    'l': 4.03,
    'm': 2.41,
    'n': 6.75,
    'o': 7.51,
    'p': 1.93,
    'q': 0.10,
    'r': 5.99,
    's': 6.33,
    't': 9.06,
    'u': 2.76,
    'v': 0.98,
    'w': 2.36,
    'x': 0.15,
    'y': 1.97,
    'z': 0.07
}


def read_file(filename):
    """Read and return the contents of a text file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def count_letters(text):
    """Count occurrences of each letter in the alphabet."""

    alphabet_dict = dict.fromkeys(string.ascii_lowercase, 0)

    for char in text.lower():
        if char in alphabet_dict:
            alphabet_dict[char] += 1

    return alphabet_dict


def calculate_frequencies(letter_counts):
    """Calculate the relative frequency of each letter."""

    total_letters = sum(letter_counts.values())

    if total_letters == 0:
        return dict.fromkeys(string.ascii_lowercase, 0)

    frequency_dict = {}

    for char, count in letter_counts.items():
        frequency_dict[char] = round(
            (count / total_letters) * 100,
            2
        )

    return frequency_dict


def sort_frequencies(frequency_dict):
    """Sort letters from most frequent to least frequent."""

    return dict(
        sorted(
            frequency_dict.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )


def compare_with_english(frequency_dict):
    """Compare observed frequencies with English frequencies."""

    comparison = {}

    for char in string.ascii_lowercase:
        observed = frequency_dict[char]
        expected = ENGLISH_FREQUENCY[char]

        comparison[char] = {
            'observed': observed,
            'expected': expected,
            'difference': round(observed - expected, 2)
        }

    return comparison


def print_analysis(letter_counts, frequency_dict, comparison):
    """Display the frequency analysis."""

    total_letters = sum(letter_counts.values())

    print("\n========== FREQUENCY ANALYSIS ==========\n")

    print(f"Total letters: {total_letters}\n")

    print(
        f"{'Letter':<8}"
        f"{'Count':<10}"
        f"{'Observed':<12}"
        f"{'Expected':<12}"
        f"{'Difference':<12}"
    )

    print("-" * 54)

    ordered = sort_frequencies(frequency_dict)

    for char in ordered:
        observed = comparison[char]['observed']
        expected = comparison[char]['expected']
        difference = comparison[char]['difference']

        print(
            f"{char:<8}"
            f"{letter_counts[char]:<10}"
            f"{observed:<12.2f}"
            f"{expected:<12.2f}"
            f"{difference:+.2f}"
        )

    print("\n========== FREQUENCY RANKING ==========\n")

    for rank, (char, frequency) in enumerate(ordered.items(), start=1):
        print(
            f"{rank:>2}. "
            f"{char} -> "
            f"{letter_counts[char]} occurrences "
            f"({frequency:.2f}%)"
        )


def main():

    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        file_contents = read_file(filename)

    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
        sys.exit(1)

    except PermissionError:
        print(f"Error: permission denied when reading '{filename}'.")
        sys.exit(1)

    letter_counts = count_letters(file_contents)

    frequency_dict = calculate_frequencies(letter_counts)

    comparison = compare_with_english(frequency_dict)

    print_analysis(
        letter_counts,
        frequency_dict,
        comparison
    )


if __name__ == "__main__":
    main()

