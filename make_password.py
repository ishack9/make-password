# -*- coding: utf-8 -*-

from itertools import permutations
from tqdm import tqdm

BANNER = """
 __     ______     __  __     ______     ______     __  __    
/\ \   /\  ___\   /\ \_\ \   /\  __ \   /\  ___\   /\ \/ /    
\ \ \  \ \___  \  \ \  __ \  \ \  __ \  \ \ \____  \ \  _"-.  
 \ \_\  \/\_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/_/   \/_____/   \/_/\/_/   \/_/\/_/   \/_____/   \/_/\/_/ 
"""

def get_characters() -> list[str]:
    """Prompts the user for characters and validates input."""
    while True:
        raw = input("Enter characters (separated by spaces): ").strip().split()

        if len(raw) == 0:
            print("You must enter at least 1 character!")
        else:
            if len(raw) >= 9:
                print(f"⚠  WARNING: {len(raw)} characters will generate a very large list, this may take a long time!")
                confirm = input("Do you want to continue? (y/n): ").strip().lower()
                if confirm != "y":
                    continue
            return raw


def generate_permutations(chars: list[str]) -> set[str]:
    """Generates all permutations of the given characters."""
    results: set[str] = set()
    for length in range(1, len(chars) + 1):
        for perm in permutations(chars, length):
            results.add("".join(perm))
    return results


def save_to_file(words: set[str], filename: str = "password.txt") -> None:
    """Saves the generated passwords to a file with a progress bar."""
    sorted_words = sorted(words, key=lambda w: (len(w), w))
    with open(filename, "w", encoding="utf-8") as f:
        for word in tqdm(sorted_words, desc="Writing to file", unit="password"):
            f.write(word + "\n")


def main():
    print(BANNER)
    print("⚠  WARNING: Entering too many characters may result in a very large file and long processing time!")
    print()

    chars = get_characters()
    n = len(chars)

    print(f"\n[+] {n} character(s) detected. Generating permutations...\n")

    words = generate_permutations(chars)
    total = len(words)
    print(f"[+] {total:,} unique combinations generated.\n")

    save_to_file(words)

    print(f"\n✅ Done! {total:,} passwords written to 'password.txt'.")


if __name__ == "__main__":
    main()
