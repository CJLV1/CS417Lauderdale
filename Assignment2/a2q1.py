import re
from collections import Counter
##problem 1

def load_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    words = re.findall(r"[A-Za-z']+", text)
    words = [w.lower().strip("'") for w in words]
    words = [w for w in words if w]  

    return words

def word_count(words):
    return Counter(words)


def print_word_count(counts, top_n=538):
    print(f"Total unique words: {len(counts)}")
    print(f"Total word count:   {sum(counts.values())}")
    print()
    print(f"Top {top_n} most frequent words:")
    print("-" * 30)
    for word, count in counts.most_common(top_n):
        print(f"{word:<15}{count}")
 
 
def main():
    filename = "declaration.txt"
    words = load_file(filename)
    counts = word_count(words)
 
    print_word_count(counts)
 
    # Specific question: how many times does "Rights" or "Right" show up?
    right_count = counts["right"] + counts["rights"]
    print()
    print(f'"Right" appears {counts["right"]} time(s).')
    print(f'"Rights" appears {counts["rights"]} time(s).')
    print(f'"Right" or "Rights" together appear {right_count} time(s).')
 
 
if __name__ == "__main__":
    main()