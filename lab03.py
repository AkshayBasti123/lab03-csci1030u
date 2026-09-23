# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Replace each `pass` with your code, and use `return` to send the answer
# back (not `print`).


def pig_latin(word):
    "Return the word translated into simple Pig Latin."
    if word[0] in "aeiou":
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"


def word_lengths(sentence):
    "Return the lengths of the words in a sentence."
    words = sentence.split()
    lengths = []

    for word in words:
        lengths.append(len(word))

    return lengths


def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)


def letter_counts(text):
    counts = {}

    for char in text:
        if char.isalpha():
            char = char.lower()

            if char in counts:
                counts[char] = counts[char] + 1
            else:
                counts[char] = 1

    return counts


def main():
    # Optional scratch space - use this to try your functions with sample values.
    # print(pig_latin("banana"))                    # ananabay
    # print(word_lengths("the quick brown fox"))    # [3, 5, 5, 3]
    # print(reverse_words("the quick brown fox"))   # fox brown quick the
    # print(letter_counts("hello"))                 # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    pass


if __name__ == "__main__":
    main()
