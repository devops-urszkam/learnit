import re
from collections import Counter
from pprint import pprint


def get_input() -> str:
    prompt = "Provide text to analyze: "

    while not (user_input := input(prompt).strip()):
        print("Empty prompt, please try again.\n")

    return user_input.lower()


def calculate_stats(text: str) -> dict:
    words = re.findall(r'\b\w+\b', text)
    sentences = re.split(r'[.!?]+', text)
    
    length_with_spaces = len(text)
    length_without_spaces = len(text.replace(" ", ""))
    word_count = len(words)
    sentence_count = len(sentences)
    longest_word = max(words, key=len)
    most_common_word = Counter(words).most_common(1)[0][0]

    return {
        "length_with_spaces": length_with_spaces,
        "length_without_spaces": length_without_spaces,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "longest_word": longest_word,
        "most_common_word": most_common_word
    }


def main() -> None:
    user_input = get_input()
    stats = calculate_stats(user_input)

    pprint(stats)


if __name__ == "__main__":
    main()