"""Text Cleanup — Starter

You are processing a short list of words from a form.
Implement without mutating inputs.
"""
from typing import List

def unique_words_preserve_order(words: List[str]) -> List[str]:
    result = []
    seen = []
    for w in words:
        if w not in seen:
            seen.append(w)
            result.append(w)
    return result


def top_k_frequent_first_tie(words: List[str], k: int) -> List[str]:
    if k <= 0:
        raise ValueError("k must be positive")

    freq = {}
    order = []
    for w in words:
        if w not in freq:
            freq[w] = 1
            order.append(w)  # remember first appearance
        else:
            freq[w] += 1

    # sort based on frequency first, then order of appearance
    sorted_words = sorted(order, key=lambda x: (-freq[x], order.index(x)))

    return sorted_words[:k]


def redact_words(words: List[str], banned: List[str]) -> List[str]:
    result = []
    for w in words:
        if w in banned:
            result.append("***")
        else:
            result.append(w)
    return result
