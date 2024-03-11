
def count_word_occurrences(text):
    words = text.split()
    word_count = {}
    max_word_length = max(len(word) for word in words)

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    sort_word_count = sorted(word_count.items())

    for word, count in sort_word_count:
        print(f"{word:{max_word_length}} : {count}")

user_input = input("Enter a string: ")
count_word_occurrences(user_input)
