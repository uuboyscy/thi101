test_list = [1, 2, 3, 4, 5]

new_list = [x * 10 for x in test_list]
new_list_generator = map(
    lambda x: x * 10,
    test_list,
)

print(new_list)
print(new_list_generator)
print()
# for i in new_list_generator:
#     print(i)

print()
print(list(new_list_generator))
