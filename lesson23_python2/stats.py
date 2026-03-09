import re

from collections import Counter
from pprint import pprint
from typing import Any


def get_input() -> str:
    prompt = "Provide text to analyze: "

    while not (user_input := input(prompt).strip()):
        print("Empty prompt, please try again.\n")

    return user_input.lower()


def calculate_stats(text: str) -> dict[str, Any]:
    words = re.findall(r'\b\w+\b', text)
    sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
    
    length_with_spaces = len(text)
    length_without_spaces = len(re.sub(r"\s+", "", text))
    word_count = len(words)
    sentence_count = len(sentences)

    longest_word = max(words, key=len) if words else None
    word_counts = Counter(words)
    max_count = max(word_counts.values()) if word_counts else 0
    most_common_words = [word for word, count in word_counts.items() if count == max_count] if word_counts else []

    return {
        "length_with_spaces": length_with_spaces,
        "length_without_spaces": length_without_spaces,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "longest_word": longest_word,
        "most_common_words": most_common_words
    }


def main() -> None:
    user_input = get_input()
    stats = calculate_stats(user_input)

    pprint(stats)


if __name__ == "__main__":
    main()
