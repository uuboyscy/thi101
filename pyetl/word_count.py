"""How to count each word?"""

word_list = [
    "aaa",
    "bbb",
    "aaa",
    "ccc",
    "...",
    "test",
]

print(word_list.count("aaa"))
word_count_dict = {}
for word in word_list:
    word_count_dict[word] = word_list.count(word)
    # print(
    #     word,
    #     word_list.count(word),
    # )
print(word_count_dict)

word_count_dict = {}
for word in word_list:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

print(word_count_dict)

